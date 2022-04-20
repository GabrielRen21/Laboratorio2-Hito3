from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python registerfuente.py

correo = "gg.2109.lp@gmail.com"
password = "holA1hola3Hola"

driver = webdriver.Chrome()

url = "https://lafuente.es/mi-cuenta/"

driver.get(url)

time.sleep(10)

driver.find_element(by=By.NAME, value="email").send_keys(correo)

time.sleep(6)

driver.find_element(by=By.ID, value="reg_password").send_keys(password)

time.sleep(3)

driver.find_element(by=By.NAME, value="register").click()

time.sleep(45)

driver.close()

time.sleep(3)
