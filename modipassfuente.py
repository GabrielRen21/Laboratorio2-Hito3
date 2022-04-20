from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python modipassfuente.py

name = "Juan"
apellido = "Castro"
correo = "gg.2109.lp@gmail.com"
password = "holA1hola3Hola"
password2 = "holA11ola33olaa"

driver = webdriver.Chrome()

url = "https://lafuente.es/mi-cuenta/"

driver.get(url)

time.sleep(10)

driver.find_element(by=By.NAME, value="username").send_keys(correo)

time.sleep(2)

driver.find_element(by=By.ID, value="password").send_keys(password)

time.sleep(2)

driver.find_element(by=By.NAME, value="login").click()

time.sleep(10)

driver.find_element_by_link_text('CONTRASEÑA').click()

time.sleep(1)

driver.find_element(by=By.ID, value="cn-accept-cookie").click()

time.sleep(1)

driver.find_element(by=By.ID, value="account_first_name").send_keys(name)

time.sleep(2)

driver.find_element(by=By.ID, value="account_last_name").send_keys(apellido)

time.sleep(2)

driver.find_element(by=By.ID, value="password_current").send_keys(password)

time.sleep(2)

driver.find_element(by=By.ID, value="password_1").send_keys(password2)

time.sleep(2)

driver.find_element(by=By.ID, value="password_2").send_keys(password2)

time.sleep(2)

driver.find_element(by=By.NAME, value="save_account_details").click()

time.sleep(45)

driver.close()

time.sleep(3)
