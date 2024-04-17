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

class TestVerlacondicionesdeloslibrosprestado():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_verlacondicionesdeloslibrosprestado(self):
    self.driver.get("http://localhost:53922/")
    self.driver.set_window_size(1046, 804)
    self.driver.find_element(By.NAME, "correo").click()
    self.driver.find_element(By.NAME, "correo").send_keys("Konoe@gmail.com")
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Prestamos").click()
    self.driver.find_element(By.LINK_TEXT, "Consultar").click()
    self.driver.find_element(By.ID, "cboestadoprestamo").click()
    self.driver.find_element(By.ID, "btnbuscar").click()
    element = self.driver.find_element(By.ID, "btnbuscar")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".odd .btn").click()
  
