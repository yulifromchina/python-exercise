from django.contrib import auth as django_auth
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import hashlib
import base64
import sign.views_if as views_if
import time
import json
from Crypto.Cipher import AES
from sign.models import Guest


# 用户认证
def user_auth(request):
    # request.META是一个python字典，包含了本次HTTP请求的header信息，比如用户认证/IP地址/用户agent
    # HTTP_AUTHORIZATION用于获取http authorization
    get_http_auth = request.META.get('HTTP_AUTHORIZATION','')
    auth = get_http_auth.split()
    try:
        auth_parts = base64.b64decode(auth[1]).decode('iso-8859-1').partition(':')
    except IndexError:
        return 'null'
    userid, password = auth_parts[0],auth_parts[2]
    user = django_auth.authenticate(username=userid,password=password)
    if user is not None and user.is_active:
        django_auth.login(request, user)
        return 'success'
    else:
        return 'fail'



# 发布会接口查询---增加用户认证
def get_event_list_sec(request):
    auth_result = user_auth(request)
    if auth_result == 'null':
        return JsonResponse({'status':10015,'message':'user auth null'})

    if auth_result == 'fail':
        return JsonResponse({'status':10016,'message':'user auth fail'})

    return views_if.get_event_list(request)


# 用户签名+时间戳
def user_sign(request):

    client_time = request.POST.get('time','')
    client_sign = request.POST.get('sign','')
    if client_time =='' or client_sign=='':
        return 'sign null'

    # 服务器时间
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"

    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"  # 客户端时间戳拼接密钥成新的字符串
    sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
    md5.update(sign_bytes_utf8) # 生成新字符串的md5
    sever_sign = md5.hexdigest()
    if sever_sign != client_sign:
        return 'sign error'
    else:
        return 'sign right'


# 添加发布会接口---增加签名和时间戳
def add_event_sec(request):
    sign_result = user_sign(request)
    if sign_result == 'sign null':
        return JsonResponse({'status':10017,'message':'user sign null'})
    elif sign_result == 'timeout':
        return JsonResponse({'status':10018,'message':'user sign timeout'})
    elif sign_result == 'sign error':
        return JsonResponse({'status':10019,'message':'user sign error'})

    return views_if.add_event(request)


# ========================AES加密算法======================================

BS =16
unpad = lambda s:s[0:-ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def decryptAES(src,key):
    """解析AES密文"""
    src = decryptBase64(src)
    iv = b'1172311105789011'
    cryptor = AES.new(key,AES.MODE_CBC,iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)


def aes_decryption(request):

    app_key = b'W7v4D60fds2Cmk2U'
    if request.method=='POST':
        data = request.POST.get('data','')

    decoded = decryptAES(data, app_key)
    dict_data = json.loads(decoded)  # json.loads将str变成dict
    return dict_data

# 嘉宾查询接口---AES算法
def get_guest_list_sec(request):
    dict_data = aes_decryption(request)

    try:
        eid = dict_data['eid']
        phone = dict_data['phone']
    except KeyError:
        return JsonResponse({'status':10001,'message':'parameter error'})

    if eid=='':
        return JsonResponse({'status':10011,'message':'eid cannot be empty'})

    if eid!='' and phone=='':
        datas=[]
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200,'message':'success','data':datas})
        else:
            return JsonResponse({'status':10005,'message':'query result is empty'})

    if eid!='' and phone !='':
        guest = {}
        try:
            result = Guest.objects.get(phone = phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10005,'message':'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200,'message':'success','data':guest})