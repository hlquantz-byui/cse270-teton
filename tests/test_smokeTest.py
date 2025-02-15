# Generated by Selenium IDE
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

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1Navigatetothehomepage(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1920, 1036)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_2Navigatetothehomepage(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/index.html")
    self.driver.set_window_size(1200, 800)
    elements = self.driver.find_elements(By.LINK_TEXT, "Home")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
  
  def test_3DirectoryPageBusinessVerification(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/directory.html")
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_4JoinPageInputVerificatoin(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/join.html")
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("YourFirstName")
    self.driver.find_element(By.NAME, "lname").send_keys("YourLastName")
    self.driver.find_element(By.NAME, "bizname").send_keys("YouBusinessName")
    self.driver.find_element(By.NAME, "biztitle").send_keys("YourTitleOrPosition")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
    assert len(elements) > 0
  
  def test_5AdminPageLoginErrorVerification(self):
    self.driver.get("http://127.0.0.1:5501/teton/1.6/admin.html")
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("incorrectUserName")
    self.driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
  
