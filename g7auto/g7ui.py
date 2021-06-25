
import time
import json
import os
import random
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class AutoExe():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.running = True

  def stop(self):
    self.running = False

  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 5):
    time.sleep(timeout)

  
  def run(self):
    self.driver.implicitly_wait(5) # seconds
    self.driver.get("http://deppon-g7s.co.huoyunren.com/#home.html")
    self.driver.maximize_window()
    try:
      if not self.running: return
      element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='left-panel']/nav/ul/li[1]/a")))
    except TimeoutException:
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "passwd").click()
      self.driver.find_element(By.ID, "passwd").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "form_button").click()
      time.sleep(2)
    # 去除指引
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "/html/body/div[11]/div[9]").click()
    except:
        pass    
    # 实时风险监控台new
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/a/span").click()
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/a").click()
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/ul/li[1]/a").click()
    except:
      pass
    finally:
      time.sleep(2)
      self.driver.switch_to.window(self.driver.window_handles[1]) 
    # 选择中高风险
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/label[3]/span").click()
    except:
        print("选择中高风险")  
    while self.running: 
      while self.running: 
        # 进行查询
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/button/span").click()
          time.sleep(3)
        except:
          print("点击查询")
          break
        # 点击第一项 
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='listBody']/div[3]/div[1]").click()
          time.sleep(2)
        except:
          print("点击第一项")
          break
        # 通知
        try:
          #通知
          if not self.running: return
          element_to_hover_over = self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]")
          hover = ActionChains(self.driver).move_to_element(element_to_hover_over).click(element_to_hover_over)
          hover.perform()
          time.sleep(2)
        except:
          print("点击通知")
          continue
        # 选择人工电话
        try:
          #人工电话
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div/div/p[1]/span").click()
          time.sleep(2)
        except:
          print("点击人工电话")
          continue
        # 干预
        try:
          # 选择干预原因
          if not self.running: return
          num = random.randint(1,15)
          self.driver.find_element(By.XPATH, f"//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[3]/div/span[{num}]").click()
          time.sleep(2)
        except:
          print("选择干预原因")
          continue
        # 干预
        try:
          # 已接通并干预
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[4]/div/span[1]").click()
          time.sleep(2)
        except:
          print("已接通并干预")
          continue
        # 保存
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[3]/div/button/span").click()
          time.sleep(2)
        except:
          print("保存")
          continue
        self.wait_for_window(2)
      count = 5
      while(count > 0):
        if not self.running: return
        self.wait_for_window(2)
        count = count - 1
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.CSS_SELECTOR, ".search-button > span").click()

####################################################
###   auto task
####################################################
tui = {}
def run_task():
  # Create and launch a thread
  ae = AutoExe()
  ae.setup_method()
  t = Thread(target=ae.run, args=())
  t.start()
  return {"t": t,"ae" : ae}

def shutdown_task(tui):
  print(tui)
  tui["ae"].stop()
  tui["t"].join()
  tui["ae"].teardown_method()
  tui = {}
  pass
####################################################
###   UI
####################################################
Builder.load_string('''
<ScreenManager>:
    StartScreen
    StopScreen

<StartScreen>:
    name: 'start'
    Button:
        text: 'Start'
        font_size: '50sp'
        on_release: root.manager.current = 'stop';root.do_start()

<StopScreen>:
    name: 'stop'
    Button:
        text: "Stop"
        font_size: '50sp'
        on_release: root.manager.current = 'start';root.do_stop(root.manager.get_screen("start"))
''')


class ScreenManager(ScreenManager):
    pass

class StartScreen(Screen):
  def do_start(self):
    self.tui = run_task()
    print('start')

    pass

class StopScreen(Screen):
  def do_stop(self, scn):
    print(scn.tui)
    shutdown_task(scn.tui)
    print('stop')
    scn.tui = {}
    pass

class TestApp(App):
    def build(self):
        self.title = 'g7auto'
        return ScreenManager()

def main():
  Config.set('graphics','resizable',False) 
  Window.size = (300, 150)
  TestApp().run()
