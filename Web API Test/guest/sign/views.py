from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username, 3600)
            return response
        else:
            return render(request, 'index.html', {'error':'username or password error!'})


# 注释@login_required装饰器，便于测试函数顺利运行
#@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request, 'event_manage.html',{'user':username,'events':event_list})


#@login_required
def search_event_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains = search_name)
    return render(request, 'event_manage.html', {'user':username, 'events':event_list})


#@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all().order_by('id')
    paginator = Paginator(guest_list,3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    return render(request, 'guest_manage.html',{'user':username,'guests':contacts})


#@login_required
def search_guest_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    guest_list = Guest.objects.filter(realname__contains = search_name).order_by('id')
    paginator = Paginator(guest_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    return render(request, 'guest_manage.html',{'user':username,'guests':contacts,'search_name':search_name})


#@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html',{'event':event})


#@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone','')
    all_guests = Guest.objects.all().count()
    signed_guests = Guest.objects.filter(sign=True).count()

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html',{'event':event,'hint':'phone error.',
                                                  'all_guests':all_guests,'signed_guests':signed_guests})

    result = Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request, 'sign_index.html',{'event':event,'hint':'event id or phone error.',
                                                  'all_guests': all_guests, 'signed_guests': signed_guests})

    result = Guest.objects.get(phone=phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html',{'event':event,'hint':'user has sign in.',
                                                  'all_guests': all_guests, 'signed_guests': signed_guests})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success!','guest':result,
                                                 'all_guests': all_guests, 'signed_guests': signed_guests})


#@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response