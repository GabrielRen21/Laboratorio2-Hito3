from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python logincl3.py

correo = "gg.2109.lp@gmail.com"
password = "SamLGteleSmart"


driver = webdriver.Chrome()

url = "https://chilesuplementos.cl/"

driver.get(url)

time.sleep(15)

inilogibt = driver.find_element_by_css_selector("span[class='login-top boton-account-top']")
inilogibt.click()

time.sleep(8)

driver.find_element(by=By.ID, value="username").send_keys(correo)

time.sleep(2)

driver.find_element(by=By.ID, value="password").send_keys(password)

time.sleep(2)

driver.find_element_by_css_selector("button[class='woocommerce-button button woocommerce-form-login__submit']").click()

time.sleep(45)

driver.close()

time.sleep(3)

