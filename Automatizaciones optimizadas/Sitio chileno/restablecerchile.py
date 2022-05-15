from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

###Credenciales de un correo de google que se puede usar
# marta33.morales99@gmail.com
# marta1Morales2

driver = webdriver.Chrome()

url = "https://chilesuplementos.cl/"

driver.get(url)
driver.maximize_window() #Maximiza la ventana del navegador

time.sleep(1)
chilebotonrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='login-top boton-account-top']")))
chilebotonrestablecer.click()

time.sleep(1)
chilelinkrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[class='lost_password']")))
chilelinkrestablecer.click() 

time.sleep(1)
chileuserrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'user_login')))
chileuserrestablecer.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya existente

time.sleep(1)
chileenviarrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='woocommerce-Button button']")))
chileenviarrestablecer.click()

time.sleep(15) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()
