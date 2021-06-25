
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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
    self.driver.implicitly_wait(10) # seconds
    self.driver.get("http://deppon-g7s.co.huoyunren.com/#home.html")
    self.driver.maximize_window()
    try:
      element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='left-panel']/nav/ul/li[1]/a")))
    except TimeoutException:
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "passwd").click()
      self.driver.find_element(By.ID, "passwd").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "form_button").click()
    # 去除指引
    try:
      self.driver.find_element(By.XPATH, "/html/body/div[11]/div[9]").click()
    except:
        pass    
    # 实时风险监控台new
    try:
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/a/span").click()
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/a").click()
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/ul/li[1]/a").click()
    except:
      pass
    finally:
      self.driver.switch_to.window(self.driver.window_handles[1]) 
    # 选择中高风险
    try:
      self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/label[3]/span").click()
    except:
        pass   
    # 进行查询
    try:
      self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/button/span").click()
    except:
        pass
    # 点击第一项 
    try:
      self.driver.find_element(By.XPATH, "//*[@id='listBody']/div[3]/div[1]").click()
    except:
        pass   
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