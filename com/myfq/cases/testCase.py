#coding:utf-8
'''
Created on 2016年8月6日

@author: ldl
'''

from baseTestCase import BaseTestCase
from ..pages.page import LoginPage
from ..pages.pageElement import login_page

class TestCase(BaseTestCase):
    
    def test_login(self):
        LoginPage().find_element(login_page['go_button'])