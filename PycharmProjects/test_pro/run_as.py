#coding:utf-8
#__author__ =='xuxu'
import unit
import requests
from config.config import header, host, logger
import unittest
from test.alumni_book import Test_Alumni_book
import os
from HTMLTestRunner import HTMLTestRunner
import sys
report_path = os.path.join(os.getcwd(),'test_report')
print(report_path)
import time

def suite():
    test_alumni_book =unittest.makeSuite(Test_Alumni_book, 'test')
    Test =unittest.TestSuite([test_alumni_book])
    return Test







if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M')



    filename = os.path.join(report_path,'api_test' + now + '.html')



    fp = open(filename, 'wb+')



    runner = HTMLTestRunner(stream=fp,title = '接口测试',description='描述',verbosity=1)
    runner.run(suite())


