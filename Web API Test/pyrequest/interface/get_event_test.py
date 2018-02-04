import unittest
import requests


class GetEventListTest(unittest.TestCase):
    """查询发布会信息（带用户认证）"""

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/sec_get_event_list/'
        self.auth_user = ('admin','yuli1234')

    def tearDown(self):
        print(self.result)

    def test_get_event_list_auth_null(self):
        """auth为空"""
        r = requests.get(self.base_url,params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],10015)
        self.assertEqual(self.result['message'],'user auth null')

    def test_get_event_list_auth_error(self):
        """auth 错误"""
        r = requests.get(self.base_url,auth = ('abc','123'),params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],10016)
        self.assertEqual(self.result['message'],'user auth fail')

    def test_get_event_list_eid_null(self):
        """eid 为空"""
        r = requests.get(self.base_url,auth=self.auth_user, params={'eid':''})
        self.result=r.json()
        self.assertEqual(self.result['status'],10001)
        self.assertEqual(self.result['message'],'parameter error')

    def test_get_event_list_success(self):
        """根据eid 查询成功"""
        r = requests.get(self.base_url,auth=self.auth_user,params={'eid':'1','phone':'111'})
        self.result= r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')