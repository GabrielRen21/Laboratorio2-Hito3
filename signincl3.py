from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python signincl3.py

nombre = "Sam"
apellido = "Perry Sony"
correo = "gg.2109.lp@gmail.com"

driver = webdriver.Chrome()

url = "https://chilesuplementos.cl/"

driver.get(url)

time.sleep(15)

inibt = driver.find_element_by_css_selector("span[class='login-top boton-account-top']")
inibt.click()

time.sleep(5)

regisbt = driver.find_element_by_css_selector("button[class='button secondary toggle-login']")
regisbt.click()

time.sleep(3)

driver.find_element(by=By.NAME, value="email").send_keys(correo)

time.sleep(3)

driver.find_element(by=By.NAME, value="billing_first_name").send_keys(nombre)

time.sleep(3)

driver.find_element(by=By.NAME, value="billing_last_name").send_keys(apellido)

time.sleep(3)

driver.find_element(by=By.NAME, value="register").click()

time.sleep(45)

driver.close()

time.sleep(3)

