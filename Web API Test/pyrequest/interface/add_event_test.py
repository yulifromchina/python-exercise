import unittest
import requests
import os, sys
import time
import hashlib
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    """添加发布会"""

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        """所有参数为空"""
        payload = {'eid':'','':'','limit':'','address':'','start_time':'','status':1}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10001)
        self.assertEqual(self.result['message'],'parameter error')

    def test_add_event_eid_exists(self):
        """id已经存在"""
        payload = {'eid':1, 'name':'一加4手机发布会','limit':2000,
                   'address':'深圳宝体','start_time':'2019','status':1}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10002)
        self.assertEqual(self.result['message'],'event id already exists')

    def test_add_event_name_exists(self):
        """名称已经存在"""
        payload = {'eid':131,'name':'红米Pro发布会','limit':2000,
                   'address':'北京水立方','start_time':'2019','status':1}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10003)
        self.assertEqual(self.result['message'],'event name already exists')

    def test_add_event_type_error(self):
        """日期格式错误"""
        payload = {'eid':121, 'name':'一加4手机发布会2','limit':2000,
                   'address':'北京水立方','start_time':'2019','status':1}

        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10004)
        self.assertIn('start_time format error',self.result['message'])

    def test_add_event_success(self):
        """添加成功"""
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,
                   'address':'北京水立方','start_time':'2019-01-01 00:00:00','status':1}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'add event success')


class AddEventTestSecurity(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/sec_add_event/'
        self.api_key = '&Guest-Bugmaster'

        now_time = time.time()
        self.client_time = str(now_time).split('.')[0]

        md5 = hashlib.md5()
        sign_str = self.client_time +self.api_key  # 待加密的字符串为时间+密钥
        sign_str_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_str_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_sign_null(self):
        """签名参数为空"""
        payload = {'eid':1,'':'','limit':'','address':'','start_time':'','time':'','sign':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10017)
        self.assertEqual(self.result['message'],'user sign null')

    def test_add_event_time_out(self):
        """请求超时"""
        now_time=str(int(self.client_time)-61)
        payload = {'eid':1,'limit':'','address':'','start_time':'',
                   'time':now_time, 'sign':'abc'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10018)
        self.assertEqual(self.result['message'],'user sign timeout')

    def test_add_event_sign_error(self):
        """签名错误"""
        payload = {'eid':1,'limit':'','address':'','start_time':'',
                    'time':self.client_time, 'sign':'abc'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10019)
        self.assertEqual(self.result['message'],'user sign error')

    def test_add_event_success(self):
        """添加成功"""
        payload = {'eid':22,'name':'华为荣耀8手机发布会','limit':2000,
                   'address':'成都体育馆','start_time':'2019-01-01 00:00:00',
                   'time':self.client_time, 'sign':self.sign_md5,'status':1}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'add event success')


if __name__=='__main__':
    test_data.init_data()
    unittest.main()
