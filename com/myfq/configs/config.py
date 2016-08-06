#coding:utf-8
'''
Created on 2016年8月6日

@author: ldl
'''
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

CONNECT = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.weizq',
    'appActivity': 'com.zztzt.android.simple.app.MainActivity',
    'baseUrl': 'http://127.0.0.1:4723/wd/hub',
    'app': PATH('../apks/csdapp.apk')
}
