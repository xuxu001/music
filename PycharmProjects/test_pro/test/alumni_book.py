#coding:utf-8
#__author__ =='xuxu'
import unittest
import requests
from config.config import header, host, logger

class Test_Alumni_book(unittest.TestCase):

    #同学录接口测试
    @classmethod
    def setUpClass(cls):
        print('-*-----')
    def setUp(self):
        self.url = host + '/student/page/alumni/book'
        self.header = header
        self.url2 = host + '/student/update/642'

    def tearDown(self):
        pass
    def test_alumni_book(self):

        url = self.url
        header = self.header
        payload = {"page":1,"pageSize":20,"openId":"o8kH70a0j3EoUNHBnIfw8OlUqmLI"}
        expect = True
        res = requests.get(url=url,params=payload)
        r = res.json()['data']['list'][0]['isHideInfo']
        self.assertEqual(r,expect)

    @classmethod
    def tearDownClass(cls):
        print('--------------')