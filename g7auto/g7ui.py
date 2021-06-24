
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from kivy.app import App
from kivy.uix.button import Button


class AutoExe():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))

  
  def exec(self):
    self.driver.get("http://deppon-g7s.co.huoyunren.com/#home.html")
    self.driver.maximize_window()
    # self.driver.find_element(By.ID, "username").click()
    # self.driver.find_element(By.ID, "username").send_keys("DP_dlyy127")
    # self.driver.find_element(By.ID, "passwd").click()
    # self.driver.find_element(By.ID, "passwd").send_keys("DP_dlyy127")
    # self.driver.find_element(By.ID, "form_button").click()
    #div.enjoyhint_close_btn
    # self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) .menu-item-parent").click()
    # self.driver.find_element(By.LINK_TEXT, "报警中心").click()
    # self.vars["window_handles"] = self.driver.window_handles
    # self.driver.find_element(By.LINK_TEXT, "实时风险监控台new").click()
    # self.vars["win6292"] = self.wait_for_window(2000)
    # self.driver.switch_to.window(self.vars["win6292"])
    # self.driver.find_element(By.CSS_SELECTOR, ".filter-item:nth-child(2) .el-checkbox-button:nth-child(3) > .el-checkbox-button__inner").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".search-button > span").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".car-table-tr-div:nth-child(1) .dealStatus").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".deal-content > p:nth-child(1) > span").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".intervene-reason-tag:nth-child(10)").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".reason-list > .intervene-reason-tag:nth-child(1)").click()
    # self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .ant-btn").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".search-button").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".car-table-tr-div:nth-child(1) .spec").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".deal-content > p:nth-child(1) > span").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".intervene-reason-tag:nth-child(8)").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".reason-list > .intervene-reason-tag:nth-child(1)").click()
    # self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .ant-btn > span").click()
    # element = self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-clicked")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.CSS_SELECTOR, ".search-button > span").click()

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

def main():
    #TestApp().run()
    print(os.getcwd())
    ae = AutoExe()
    ae.setup_method()
    ae.exec()
    ae.wait_for_window(10000)
    ae.teardown_method()