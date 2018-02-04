from django.test import TestCase
from sign.models import Event, Guest
from django.test import Client
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name='oneplusthree event', status=True, limit=2000,address='深圳',
                             start_time='2018-09-10 10:10:10')
        Guest.objects.create(id=1, event_id=1, realname='alen',phone='13618331833',email='alen@email.com',sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplusthree event')
        self.assertEqual(result.address, '深圳')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13618331833')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)


class IndexPageTest(TestCase):
    """测试index登陆首页"""

    def text_index_page_renders_index_template(self):
        """测试index视图"""
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    """测试登陆函数"""

    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123')
        self.c = Client()

    def test_login_action_username_password_null(self):
        """用户名密码为空"""
        test_data = {'username':'','password':''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!',response.content)

    def test_login_action_username_password_error(self):
        """用户名密码错误"""
        test_data={'username':'abc','password':'123'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        """登陆成功"""
        test_data = {'username':'admin','password':'admin123'}
        response = self.c.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,302)


class EventManageTest(TestCase):
    """发布管理"""

    def setUp(self):
        Event.objects.create(id=2,name='小米5',limit=2000,status=True, address='北京',start_time=datetime(2018,5,5,1,1,1))
        self.c = Client()

    def test_event_manage_success(self):
        """测试小米5发布会"""
        response = self.c.post('/event_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn(bytes("小米5",encoding='utf8'), response.content)
        self.assertIn(bytes("北京",encoding='utf8'),response.content)

    def test_event_manage_search_success(self):
        """测试发布会搜索"""
        response = self.c.post('/search_event_name/',{'name':'小米5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes("小米5",encoding='utf8'),response.content)
        self.assertIn(bytes("北京",encoding='utf8'),response.content)


class GuestManageTest(TestCase):
    """嘉宾管理"""

    def setUp(self):
        Event.objects.create(id=1, name='小米5', limit=2000,
                             address="北京",status=1, start_time=datetime(2018,5,5,5,5,5))
        Guest.objects.create(realname='余力',phone='123456',email='alen@email.com', sign=0,event_id=1)
        self.c=Client()

    def test_guest_manage_success(self):
        """测试嘉宾信息"""
        response = self.c.post('/guest_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn(bytes("余力",encoding='utf8'),response.content)
        self.assertIn(b'123456', response.content)

    def test_guest_manage_search_success(self):
        """测试嘉宾搜索"""
        response = self.c.post('/search_guest_name/',{'name':'余力'})
        self.assertEqual(response.status_code,200)
        self.assertIn(bytes('余力',encoding='utf8'),response.content)
        self.assertIn(b'123456',response.content)


class SignIndexActionTest(TestCase):
    """发布会签到"""

    def setUp(self):
        Event.objects.create(id=1, name="小米5",limit=2000,address='北京',
                             status=1,start_time=datetime(2018,10,10,10,10,10))
        Event.objects.create(id=2,name='小米6',limit=2000,address='深圳',
                             status=1,start_time=datetime(2018,5,5,5,5,5))
        Guest.objects.create(realname='余力',phone='123',
                             email='yuli@email.com',sign=0,event_id=1)
        Guest.objects.create(realname='alen',phone='456',
                             email='alen@email.com',sign=1,event_id=2)
        self.c = Client()

    def test_sign_index_action_phone_numm(self):
        """手机号为空"""
        response = self.c.post('/sign_index_action/1/',{'phone':''})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'phone error',response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        """手机号或发布会id错误"""
        response = self.c.post('/sign_index_action/2/',{'phone':'123'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b'event id or phone error', response.content)

    def test_sign_index_action_sign_success(self):
        """用户已签到"""
        response = self.c.post('/sign_index_action/1/',{'phone':'456'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in', response.content)

    def test_sign_index_action_sign_success(self):
        """签到成功"""
        response = self.c.post('/sign_index_action/1/', {'phone':'123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success', response.content)


