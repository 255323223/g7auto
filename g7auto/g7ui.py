
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
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException,WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

import os 
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

from kivy.resources import resource_find,resource_add_path
cwd = os.getcwd().replace("\\", "/")
resource_add_path(f'{cwd}/g7auto/data/')
default_shape = Config.get('kivy', 'window_shape')
alpha_shape = resource_find(
    'bg.png'
)


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
  def run(self,app):
    try:
      self.run_inter(app)
    except NoSuchWindowException:
      print("run_inter NoSuchWindowException")
    except WebDriverException:
      print("run_inter WebDriverException")
    finally:
      #print(app.root.screens)
      app.root.current = 'start'
  def run_inter(self,app):
    print(app)
    try:
      self.driver.implicitly_wait(2) # seconds
      self.driver.get("http://deppon-g7s.co.huoyunren.com/#home.html")
      self.driver.maximize_window()
      #self.driver.fullscreen_window()
    except NoSuchWindowException:
      return
    except WebDriverException:
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
      time.sleep(3)
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
      time.sleep(3)
      self.driver.switch_to.window(self.driver.window_handles[1]) 
    # 选择中高风险
    try:
      if not self.running: return
      self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/label[3]/span").click()
    except:
        print("选择中高风险")  
    while self.running: 
      while self.running: 
        try:
          webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
          print("esc")
        # 隐藏侧边栏 
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[1]/span[3]/i").click()
          #time.sleep(1)
        except:
          print("隐藏侧边栏")
        # 进行查询 
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/button/span").click()
          time.sleep(1)
        except:
          print("点击查询")
          break
        # 点击第一项 
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='listBody']/div[3]/div[1]").click()
          time.sleep(1)
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
          time.sleep(1)
        except:
          print("点击通知")
          continue
        # 选择人工电话
        try:
          #人工电话
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div/div/p[1]/span").click()
          time.sleep(1)
        except:
          print("点击人工电话")
          continue
        # 干预
        try:
          # 选择干预原因
          if not self.running: return
          nlist = [2,6,7,8,9,10,11,12,13,15]
          num = nlist[random.randint(0,9)]
          self.driver.find_element(By.XPATH, f"//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[3]/div/span[{num}]").click()
          #time.sleep(1)
        except:
          print("选择干预原因")
          continue
        # 干预
        try:
          # 已接通并干预
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[2]/div/div[4]/div/span[1]").click()
          time.sleep(1)
        except:
          print("已接通并干预")
          continue
        # 保存
        try:
          if not self.running: return
          self.driver.find_element(By.XPATH, "//*[@id='content']/div[12]/div[2]/div/div[1]/div[3]/div/button/span").click()
          time.sleep(1)
        except:
          print("保存")
          continue
        # time.sleep(1)
      # count = 1
      # while(count > 0):
      #   if not self.running: return
      #   self.wait_for_window(2)
      #   count = count - 1
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
def run_task(app):
  # Create and launch a thread
  ae = AutoExe()
  ae.setup_method()
  t = Thread(target=ae.run, args=(app,))
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
    Button:
        id: br
        text: 'R'
        bold: True
        font_size: '50sp'
        color: 1,0,0,1
        background_color: 1,0,0,1
        on_release: root.manager.current = 'stop';root.do_start(app)

<StopScreen>:
    name: 'stop'
    Button:
        id: bs
        text: "S"
        bold: True
        font_size: '50sp'
        color: 0,1,0,1
        background_color: 0,1,0,1
        on_release: root.manager.current = 'start';root.do_stop(root.manager.get_screen("start"))
''')


class ScreenManager(ScreenManager):
    pass

class StartScreen(Screen):
  # def on_pre_enter(self):
  #   Window.bind(mouse_pos=self.on_mouse_pos)
  def do_start(self,app):
    self.tui = run_task(app)
    print('start')
  # def on_mouse_pos(self, window, pos):
  #   print(window,pos)

class StopScreen(Screen):
  def do_stop(self, scn):
    if hasattr(scn, 'tui'):
      print(scn.tui)
      shutdown_task(scn.tui)
      scn.tui = {}
    print('stop')

class TestApp(App):
  #shape_image = StringProperty('', force_dispatch=True)

  def on_stop(self, *args):
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
    self.bind(on_stop=lambda *args, w=Window, t=title: unregister_topmost(w, t))
    #move window
    #Window.bind(mouse_pos=self.on_mouse_pos)
    Window.bind(on_key_down=self.on_key_action)
  def on_mouse_pos(self, window, pos):
    print(self.root.get_screen("start").ids.br.state)
    if self.root.get_screen("start").ids.br.state == "down":
      Window.left, Window.top = pos
  def on_key_action(self, t1,t2,t3,key,t4):
    print(key)
    if key == 'a':
      Window.left = Window.left - 10
    elif key == 'd':
      Window.left = Window.left + 10  
    elif key == 'w':
      Window.top = Window.top - 10   
    elif key == 's':
      Window.top = Window.top + 10   

  def build(self):
    return ScreenManager()

def main():

  app = TestApp()
  app.run()

if __name__ == "__main__":
  #cwd = os.getcwd().replace("\\", "/")
  #print(cwd)
  main()