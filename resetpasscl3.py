from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python resetpasscl3.py

correo = "gg.2109.lp@gmail.com"
password = "SamLGteleSmart"


driver = webdriver.Chrome()

url = "https://chilesuplementos.cl/"

driver.get(url)

time.sleep(10)

iniresetbt = driver.find_element_by_css_selector("span[class='login-top boton-account-top']")
iniresetbt.click()

time.sleep(7)

driver.find_element_by_css_selector("p[class='lost_password']").click()

time.sleep(5)

driver.find_element(by=By.NAME, value="user_login").send_keys(correo)

time.sleep(2)

driver.find_element_by_css_selector("button[class='woocommerce-Button button']").click()

time.sleep(60)

driver.close()

time.sleep(3)
