from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Cambiar valores de las variables.
#python resetpassfuente.py

correo = "gg.2109.lp@gmail.com"

driver = webdriver.Chrome()

url = "https://lafuente.es/mi-cuenta/"

driver.get(url)

time.sleep(10)

driver.find_element_by_link_text('¿Olvidaste la contraseña?').click()

time.sleep(10)

driver.find_element(by=By.ID, value="user_login").send_keys(correo)

time.sleep(2)

driver.find_element_by_css_selector("button[class='woocommerce-Button button']").click()

time.sleep(45)

driver.close()

time.sleep(3)
