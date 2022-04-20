from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python loginfuente.py

correo = "gg.2109.lp@gmail.com"
password = "holA1hola3Hola"

driver = webdriver.Chrome()

url = "https://lafuente.es/mi-cuenta/"

driver.get(url)

time.sleep(10)

driver.find_element(by=By.NAME, value="username").send_keys(correo)

time.sleep(1)

driver.find_element(by=By.ID, value="password").send_keys(password)

time.sleep(1)

driver.find_element(by=By.NAME, value="login").click()

time.sleep(60)

driver.close()

time.sleep(3)
