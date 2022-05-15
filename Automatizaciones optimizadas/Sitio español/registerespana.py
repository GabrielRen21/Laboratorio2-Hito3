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

time.sleep(1) #Tiempo de espera de 1 segundo para evitar conflictos con la página en la automatización
correoregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
correoregistro.send_keys("andreillaforever@gmail.com") #Escribir correo a registrar

time.sleep(1)
passregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'reg_password')))
passregistro.send_keys("marta12chaoRR") #Escribir contraseña para la cuenta

time.sleep(1)
botonregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'register')))
botonregistro.click()

time.sleep(15) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close() #Cierra la página del navegador
