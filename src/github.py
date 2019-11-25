#coding = utf-8

from selenium import webdriver
from Utils import utils
from src.Utils import utils
from selenium.webdriver.support import expected_conditions as EC


def isExits (driver, css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False

class AsktestfanLogin(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://ask.testfan.cn/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)



    def login(self):
        find_email = self.driver.find_element_by_css_selector("input[name='email']")
        find_email.clear()
        find_email.send_keys('15254587271@163.com')
        find_password = self.driver.find_element_by_css_selector("input[name='password']")
        find_password.clear()
        find_password.send_keys('3739157abc')
        self.driver.find_element_by_tag_name('button').click()
        # self.driver.find_element_by_css_selector('#unread_messages').click()
        #assertis = self.driver.find_element_by_css_selector('#unread_messages')
        if(isExits(self.driver,'#unread_messages')):
            print('登录pass')
        else:
            print('登录fail')

        self.driver.close()

aa = AsktestfanLogin()
aa.login()