from Crypto.Cipher import AES
import base64
import requests
import unittest
import json
import chardet

# 以下涉及较多的编解码
# 编码是把人可见的str变成机器可见的unicode
# 解码是把机器可见的unicode变成人可见的str
# ascii-一个字节  unicode-4个字节 utf-8：变长，英文是1个字节，等同于asciibi编码
# chardet可对已编码的bytes进行检测，不能用于对str检测
# ps: 编解码的最佳实践是三明治原则

class AESTest(unittest.TestCase):

    def setUp(self):
        BS = 16
        self.pad = lambda s:s+(BS - len(s)%BS) * chr(BS-len(s)%BS)  # 通过匿名函数对字符串补足，使长度是16的倍数
        self.base_url = 'http://127.0.0.1:8000/api/sec_get_guest_list/'
        self.app_key = b'W7v4D60fds2Cmk2U'  # app_key是密钥，只有合法的调用者才知道

    def encryptBase64(self, src):
        return base64.urlsafe_b64encode(src)

    def encryptAES(self, src, key):
        """生成AES密文"""
        iv = b'1172311105789011'
        cryptor = AES.new(key, AES.MODE_CBC, iv)
        src = self.pad(src)  # key, 传输内容, iv都需要是bytes类型
        src = src.encode('utf-8')
        ciphertext = cryptor.encrypt(src)
        return self.encryptBase64(ciphertext)

    def test_aes_interface(self):
        """test aes interface"""
        payload = {'eid':'1','phone':'123456'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode() # decode()将bytes转化为str

        r = requests.post(self.base_url, data={'data':encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')

    def test_get_guest_list_eid_null(self):
        """eid参数为空"""
        payload = {'eid':'','phone':''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.post(self.base_url, data={'data': encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10011)
        self.assertEqual(self.result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        """根据eid查询结果为空"""
        payload = {'eid': '901', 'phone': ''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.post(self.base_url, data={'data': encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10005)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        """根据eid查询结果成功"""
        payload = {'eid': '1', 'phone': ''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.post(self.base_url, data={'data': encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['realname'],'alen')
        self.assertEqual(self.result['data'][0]['phone'],'123456')

    def test_get_event_list_eid_phone_null(self):
        """根据eid和phone查询结果为空"""
        payload = {'eid': '1', 'phone': '111'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.post(self.base_url, data={'data': encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10005)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        """根据eid和phone查询成功"""
        payload = {'eid': '5', 'phone': '123458'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()
        r = requests.post(self.base_url, data={'data': encoded})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['realname'],'tom')
        self.assertEqual(self.result['data']['email'],'tom@email.com')




if __name__=='__main__':
    payload = {'eid': '1', 'phone': '13811111111'}
    payload = json.dumps(payload)
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    src = pad(payload)
    print(src)
    src = src.encode('utf-8')
    print(src)
    print(chardet.detect(src))
    iv = b'1172311105789011'
    key = b'W7v4D60fds2Cmk2U'
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cryptor.encrypt(src)
    print(ciphertext)
    print(chardet.detect(ciphertext))
    ciphertext = base64.urlsafe_b64encode(ciphertext)
    print(ciphertext)
    print(chardet.detect(ciphertext))
    print(type(ciphertext))
    decoded = ciphertext.decode()
    print(decoded)
    print(type(decoded))


