#coding:utf-8
'''
Created on 2016年8月6日

@author: ldl
'''
import unittest

from appium import webdriver

from ..configs import config


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': config.CONNECT['platformName'],
            'platformVersion': config.CONNECT['platformVersion'],
            'deviceName': config.CONNECT['deviceName'],
#             'appPackage': config.CONNECT['appPackage'],
#             'appActivity': config.CONNECT['appActivity'],
            'app': config.CONNECT['app']
            
        }
        
        self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)


    def tearDown(self):
        self.driver.close()

