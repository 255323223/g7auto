
import time
import json
import os
import sys
import random
import urllib.request 
import urllib.error
from threading import Thread
import logging

#logging.basicConfig(filename= 'G7Auto.log', filemode='w', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d [%(pathname)s %(filename)s:%(lineno)d] %(message)s', datefmt='## %Y-%m-%d %H:%M:%S')
logging.basicConfig(filename= 'G7Auto.log', filemode='w', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(message)s', datefmt='## %Y-%m-%d %H:%M:%S')
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("kivy").setLevel(logging.ERROR)
logger = logging.getLogger()
#logger.addHandler(logging.FileHandler('G7Auto.log', 'w'))
printF = logger.debug


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException,WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)

import pyautogui

os.environ['KIVY_IMAGE'] = 'pil,sdl2'
# config
from kivy.config import Config
Config.set('graphics', 'shaped', 1)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
# Config.set('kivy', 'keyboard_mode', 'systemandmulti')
# Config.set('graphics','resizable',False) 
#Config.set('graphics', 'fullscreen', 'fake')
# Config.set('graphics', 'position', 'custom') 
# Config.set('graphics', 'top', '100') 
# Config.set('graphics', 'left', '100') 
Config.set('graphics', 'width', '60') 
Config.set('graphics', 'height', '60') 


from kivy.logger import Logger, LOG_LEVELS
Logger.setLevel(LOG_LEVELS["error"])
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    StringProperty,
    ListProperty,
)
from KivyOnTop import register_topmost, unregister_topmost

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

from kivy.resources import resource_find,resource_add_path
cwd = os.getcwd().replace("\\", "/")
# printF(cwd)
resource_add_path(f'{cwd}/data/')
default_shape = Config.get('kivy', 'window_shape')
alpha_shape = resource_find(
    'bg.png'
)
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
# printF(default_shape)
# printF(alpha_shape)

class AutoExe():
  def setup_method(self):
    #设置chrome浏览器无界面模式
    options = webdriver.ChromeOptions()
    #options.add_argument('log-level=3')
    options.add_argument("--start-maximized")
    ##
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--remote-debugging-port=9222')
    # service = Service('chromedriver')
    # service.creationflags = CREATE_NO_WINDOW
    # self.driver = webdriver.Chrome(options=options, service_args=service)  # version 4 

    self.driver = webdriver.Chrome(executable_path= f'{cwd}/chromedriver.exe',options=options)
    self.vars = {}
    self.running = True
    self.count = 0

  def stop(self):
    self.running = False

  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 1):
    time.sleep(timeout)
  def run(self,app):
    try:
      self.run_inter(app)
    except NoSuchWindowException:
      printF("run NoSuchWindowException")
    except WebDriverException:
      printF("run WebDriverException")
    except ConnectionResetError:
      printF("run ConnectionResetError")
    except ConnectionError:
      printF("run ConnectionError")
    finally:
      #print(app.root.screens)
      printF("停止自动化任务(被动)")
      #app.root.get_screen("stop").do_stop(app.root.get_screen("start"))
      app.root.current = 'start'
  def run_inter(self,app):
    #print(app)
    try:
      self.driver.implicitly_wait(2) # seconds
      self.driver.get("http://deppon-g7s.co.huoyunren.com/#home.html")
      time.sleep(3)
      #self.driver.maximize_window()
      #self.driver.fullscreen_window()
    except NoSuchWindowException:
      printF("run_inter NoSuchWindowException")
      return
    except WebDriverException:
      printF("run_inter WebDriverException")
      return
    try:
      if not self.running: return
      element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='left-panel']/nav/ul/li[1]/a")))
    except TimeoutException:
      self.driver.find_element(By.ID, "username").click()
      self.driver.find_element(By.ID, "username").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "passwd").click()
      self.driver.find_element(By.ID, "passwd").send_keys("DP_dlyy127")
      self.driver.find_element(By.ID, "form_button").click()
      printF("登录")
    try:
      if not self.running: return
      element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/a/span")))
    except TimeoutException:
      printF("run_inter TimeoutException 登录")
      return
    # 去除指引
    try:
      if not self.running: return
      element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div[9]")))
    except TimeoutException:
      pass
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "/html/body/div[11]/div[9]").click()
    except:
        pass    
    # 实时风险监控台new
    try:
      if not self.running: return
      cur_handles = self.driver.window_handles
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/a/span").click()
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/a").click()
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//*[@id='left-panel']/nav/ul/li[4]/ul/li[2]/ul/li[1]/a").click()
    except:
      printF("run_inter 实时风险监控台new")
      return
    finally:
      try:
        element = WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(cur_handles))
      except TimeoutException:
        printF("失败，等待新窗口")
        return
      try:
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        printF("打开实时风险看板")
      except:
        printF("失败，打开新窗口") 
    # 选择中高风险
    try:
      element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/label[3]/span")))
    except TimeoutException:
      printF("失败，等待中高风险")
      return
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/label[3]/span").click()
      time.sleep(2)
    except:
        printF("失败，选择中高风险")  
        return
    while self.running:
      # 发送ESC按键
      try:
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
      except:
        printF("发送ESC按键")
      # 隐藏侧边栏 
      try:
        if not self.running: return
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[1]/span[3]/i").click()
      except:
        pass
        #printF("隐藏侧边栏")
      # 进行查询 
      try:
        if not self.running: return
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div[1]/button/span")))
        time.sleep(1)
      except TimeoutException:
        printF("失败，无查询按钮")
        continue
      try:
        if not self.running: return
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/button/span").click()
        time.sleep(1)
      except:
        printF("失败，点击查询")
        continue
      # 点击第一项 
      try:
        if not self.running: return
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='listBody']/div[3]/div[1]")))
      except TimeoutException:
        printF("无数据")
        continue
      try:
        if not self.running: return
        self.driver.find_element(By.XPATH, "//*[@id='listBody']/div[3]/div[1]").click()
      except:
        printF("失败，点击第一项")
        continue
      # 通知，mouse hover
      try:
        if not self.running: return
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div/div[1]/span[3]/i")))
      except TimeoutException:
        printF("失败，无侧边栏")
        continue
      try:
        if not self.running: return
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]")))
      except TimeoutException:
        printF("失败，无通知")
        continue
      num = 3
      while num != 0:
        num-=1
        try:
          #if not self.running: return
          element_to_hover_over = self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]")
          hover = ActionChains(self.driver).move_to_element(element_to_hover_over).click(element_to_hover_over).click(element_to_hover_over)
          hover.perform()
          time.sleep(0.5)
        except:
          printF("失败，点击通知")
          continue
        # 选择人工电话
        try:
          if not self.running: return
          WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div/div/p[1]/span")))
        except TimeoutException:
          printF("失败，等待人工电话")
          continue
        try:
          #人工电话
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div/div/p[1]/span").click()
        except:
          printF("失败，点击人工电话")
          continue
        break #while end  
      # 干预
      try:
        if not self.running: return
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[3]/div/span[10]")))
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[4]/div/span[1]")))
      except TimeoutException:
        continue
      try:
        # 选择干预原因
        if not self.running: return
        time.sleep(0.5)
        nlist = [2,6,7,8,9,10,11,12,13,15]
        num = nlist[random.randint(0,9)]
        self.driver.find_element(By.XPATH, f"//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[3]/div/span[{num}]").click()
      except:
        printF("失败，选择干预原因")
        continue
      # 干预
      try:
        # 已接通并干预
        if not self.running: return
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[4]/div/span[1]").click()
      except:
        printF("失败，已接通并干预")
        continue
      # 保存
      try:
        if not self.running: return
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[3]/div/button/span").click()
        self.count = self.count + 1
        printF(f"已经完成任务:{self.count}")
        time.sleep(3)
      except:
        printF("失败，保存")
        continue


####################################################
###   auto task
####################################################

def run_task(app):
  # Create and launch a thread
  tui = AutoExe()
  tui.setup_method()
  thr = Thread(target=tui.run, args=(app,))
  thr.start()
  return thr, tui

def shutdown_task(tui):
  #print(tui)
  tui.stop()
  #tui["t"].join()
  tui.teardown_method()
  #tui = {}
  pass
####################################################
###   UI
####################################################
Builder.load_string('''
<RoundedButton@Button>:
    size_hint: (None, None)
    size: (60, 60)
    background_color: 1,0,0,0  # the last zero is the critical on, make invisible
    canvas.before:
        Color:
            rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
        RoundedRectangle:
            pos: (self.center_x - 30, self.center_y - 30)
            size: self.size
            radius: [30,]
    text:''

<ScreenManager>:
    StartScreen
    StopScreen

<StartScreen>:
    name: 'start'
    RoundedButton:
        id: br
        text: 'R'
        bold: True
        font_size: '50sp'
        color: 1,0,0,1
        background_color: 1,0,0,1
        on_release: root.manager.current = 'stop';root.do_start(app,self.min_state_time)

<StopScreen>:
    name: 'stop'
    RoundedButton:
        id: bs
        text: "S"
        bold: True
        font_size: '50sp'
        color: 0,1,0,1
        background_color: 0,1,0,1
        on_release: root.manager.current = 'start'
''')


class ScreenManager(ScreenManager):
    pass

class StartScreen(Screen):
  # def on_pre_enter(self):
  #   Window.bind(mouse_pos=self.on_mouse_pos)
  def do_start(self,app,mst = 0):
    #print(mst)
    if hasattr(self, 'thr'):
      self.thr.join()
      del self.thr
    if hasattr(self, 'tui'):
      del self.tui
    self.thr, self.tui = run_task(app)
    printF('开始自动化任务')
  # def on_mouse_pos(self, window, pos):
  #   print(window,pos)

class StopScreen(Screen):
  def do_stop(self, scn, mst = 0):
    #print(mst)
    if hasattr(scn, 'tui') and scn.tui:
      #print(scn.tui)
      shutdown_task(scn.tui)
      del scn.tui
      printF('停止自动化任务')
  def on_pre_leave(self):
    self.do_stop(self.manager.get_screen("start"))
class TestApp(App):
  #shape_image = StringProperty('', force_dispatch=True)
  def on_stop(self, *args):
    printF("程序停止运行")
    self.root.get_screen("stop").do_stop(self.root.get_screen("start"))
    #print(self.root.screens)
  def on_start(self, *args):
    title = 'G7Auto'
    Window.set_title(title)
    #Window.size = (256, 256)
    Window.left = 0
    Window.top = 0
    Window.borderless = True 

    #Window.shape_mode = 'default'
    Window.shape_image = alpha_shape
    Window.shape_mode = 'colorkey'
    Window.shape_color_key = [0,0,0,1]
    # Register top-most
    register_topmost(Window, title)
    # Unregister top-most (not necessary, only an example)
    #self.bind(on_stop=lambda *args, w=Window, t=title: unregister_topmost(w, t))
    #move window
    #Window.bind(mouse_pos=self.on_mouse_pos)
    Window.bind(on_key_down=self.on_key_action)
    printF("程序开始运行")

  def on_mouse_pos(self, window, pos):
    #print(self.root.get_screen("start").ids.br.state)
    if self.root.get_screen("start").ids.br.state == "down":
      Window.left, Window.top = pyautogui.position()
      #pyautogui.moveTo(0, 0)
    else:
      pass
  def on_key_action(self, t1,t2,t3,key,t4):
    #print(t1,t2,t3,key,t4)
    if key == 'a' or t3 == 80:
      Window.left = Window.left - 10
    elif key == 'd' or t3 == 79:
      Window.left = Window.left + 10  
    elif key == 'w' or t3 == 82:
      Window.top = Window.top - 10   
    elif key == 's' or t3 == 81:
      Window.top = Window.top + 10   

  def build(self):
    return ScreenManager()

def main():
  #global app
  app = TestApp()
  app.run()

if __name__ == "__main__":
  #cwd = os.getcwd().replace("\\", "/")
  #printF(cwd)
  try:
    response = urllib.request.urlopen('https://gitee.com/coolxv/g7auto/blob/master/DP_dlyy127')
    if response.status == 200:
      main()
  except urllib.error.URLError as e:
    printF("无使用权限")
    
