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

url = "https://lafuente.es/mi-cuenta/"

driver.get(url)
driver.maximize_window() #Maximiza la ventana del navegador

time.sleep(1)
correologin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
correologin.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya creada

time.sleep(1)
passlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
passlogin.send_keys("ChaoMarta235.") #Escribir contraseña de una cuenta ya creada

time.sleep(1)
botonlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'login')))
botonlogin.click()

time.sleep(10) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()
