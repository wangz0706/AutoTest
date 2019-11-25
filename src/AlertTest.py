#coding = utf-8
from argparse import Action


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class Browser():
    driver = webdriver.Chrome()
    sleep(3)
    # #只有确认弹框
    # driver.get('https://www.w3school.com.cn/tiy/t.asp?f=js_alert')
    # driver.switch_to.frame('iframeResult')
    # driver.find_element_by_tag_name('button').click()
    # sleep(2)
    # alert = driver.switch_to.alert.accept()
    driver.close()


    # #有确认和取消
    # driver.get('https://www.w3school.com.cn/tiy/t.asp?f=js_confirm')
    # driver.switch_to.frame('iframeResult')
    # driver.find_element_by_tag_name('button').click()
    # sleep(2)
    #driver.find_element_by_tag_name('button')click()
    # alert = driver.switch_to.alert.accept()
    # sleep(3)
    # driver.find_elemtch_to.alert
    # alert.dismiss()

    #有提示语的输入框
    # driver.get('https://www.w3school.com.cn/tiy/t.asp?f=js_alert_2')
    # driver.switch_to.frame('iframeResult')
    # driver.find_element_by_tag_name('button').click()
    # sleep(2)
    # alert = driver.switch_to.alert
    # print(alert.text)
    # driver.close()

    #尝试pt登录??????
    driver.get('https://uniauth-demo.corp.dianrong.com/#/login')
    driver.switch_to_alert()
    driver.find_element_by_css_selector('#root').send_keys(Keys.ENTER)

    # alert = driver.switch_to.alert
    # print(alert.text)
    # alert.accept()
    sleep(3)


    #下拉框https://www.w3school.com.cn/tiy/t.asp?f=html_input_checkbox
    # driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')
    # driver.switch_to.frame('iframeResult')
    # #要先定位到下拉框
    # s = driver.find_element_by_tag_name('select')
    # Select(s).select_by_index(2)
    # sleep(2)
    # Select(s).select_by_value('audi')
    # sleep(2)
    # Select(s).select_by_visible_text('Saab')
    # sleep(2)
    # driver.close()
    # driver.page_source
    # driver.find_element_by_css_selector()


    driver.execute_script()
    driver.save_screenshot()
    driver.find_element_by_and











