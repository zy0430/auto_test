import sys
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


class TestOther():

  def setup_method(self, method):
    # self.driver = webdriver.Chrome("F:\webdriver\chromedriver.exe")
    self.driver = webdriver.Chrome("D:\chrome\chromedriver.exe")
    self.vars = {}

  def test_other(self):
    self.driver.get("http://www.baidu.com")
    # self.driver.maximize_window()
    # self.driver.find_element(By.CSS_SELECTOR,"[name='wd']").send_keys("三生三世")
    self.driver.find_element(By.CSS_SELECTOR,"input[id='kw'][name='wd']").send_keys("三生三世aaaa")
