import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAuto():
  def setup_method(self, method):
    self.driver = webdriver.Chrome("F:\webdriver\chromedriver.exe")
    self.vars = {}

  def test_auto(self):
      self.driver.get("http://39.98.251.12/www/login")
      self.driver.maximize_window()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-input-type-text > .ivu-input").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-input-type-text > .ivu-input").send_keys("test")
      self.driver.find_element(By.CSS_SELECTOR,".ivu-input-type-password > .ivu-input").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-input-type-password > .ivu-input").send_keys("123456")
      self.driver.find_element(By.CSS_SELECTOR, ".ivu-checkbox-input").click()
      self.driver.find_element(By.CSS_SELECTOR, ".loginBtn > span").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR,".ivu-menu-submenu:nth-child(7) > .ivu-menu-submenu-title").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-menu-opened .ivu-menu-item:nth-child(1)").click()
      self.driver.find_element(By.CSS_SELECTOR,".f-floatRight > span").click()  # 点击添加患者
      self.driver.find_element(By.CSS_SELECTOR,".ivu-form-item-required .ivu-input:nth-child(2)").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-form-item-required .ivu-input:nth-child(2)").send_keys("zd00006")
      self.driver.find_element(By.CSS_SELECTOR,".ivu-form-item-content > .ivu-input-type-text > .ivu-input:nth-child(3)").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-form-item-content > .ivu-input-type-text > .ivu-input:nth-child(3)").send_keys("自动6号")
      self.driver.find_element(By.CSS_SELECTOR,".ivu-radio-group-item:nth-child(2)").click()

      # 选择日期
      self.driver.find_element(By.CSS_SELECTOR,".ivu-form-item-content > .ivu-date-picker").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-picker-panel-body > .ivu-date-picker-header > span:nth-child(3) > span:nth-child(1)").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-picker-panel-body > .ivu-date-picker-header > span:nth-child(3) > .ivu-icon-ios-arrow-forward").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-picker-panel-body > .ivu-date-picker-header > span:nth-child(3) > .ivu-icon-ios-arrow-forward").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-picker-panel-body > .ivu-date-picker-header > span:nth-child(3) > .ivu-icon-ios-arrow-forward").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-date-picker-cells-year > span:nth-child(6)").click()
      self.driver.find_element(By.CSS_SELECTOR,".ivu-date-picker-cells-month > span:nth-child(4)").click()

      self.driver.find_element(By.CSS_SELECTOR,".ivu-date-picker-cells:nth-child(1) >.ivu-date-picker-cells-cell:nth-child(37) > em").click()












