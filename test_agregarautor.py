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

class TestAgregarautor():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregarautor(self):
    self.driver.get("http://localhost:53922/")
    self.driver.set_window_size(1042, 808)
    self.driver.find_element(By.NAME, "correo").click()
    self.driver.find_element(By.NAME, "correo").send_keys("Konoe@gmail.com")
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Autores").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtdescripcion").click()
    self.driver.find_element(By.ID, "txtdescripcion").send_keys("Grabiel Garcia")
    self.driver.find_element(By.ID, "FormModal").click()
    self.driver.find_element(By.ID, "txtdescripcion").send_keys("Gabriel García Márquez")
    self.driver.find_element(By.ID, "cboEstado").click()
    self.driver.find_element(By.ID, "cboEstado").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
  
