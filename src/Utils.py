#coding = utf-8

from selenium import webdriver

class utils():
    def isExits (self,driver,css):
        self.driver =driver
        try:
            self.driver.find_element_by_css_selector(css)
            return True
        except:
            return False
