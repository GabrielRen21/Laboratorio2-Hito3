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

time.sleep(1) #Tiempo de espera de 1 segundo para evitar conflictos con la página en la automatización
chilebotoninicioregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='login-top boton-account-top']")))
chilebotoninicioregistro.click()

time.sleep(1)
chilebotonregistroregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='button secondary toggle-login']")))
chilebotonregistroregistro.click()

time.sleep(1)
chilecorreoregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
chilecorreoregistro.send_keys("andreillaforever@gmail.com") #Escribir correo a registrar

time.sleep(1)
chilenombreregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'billing_first_name')))
chilenombreregistro.send_keys("Martaa") #Escribir nombre del usuario

time.sleep(1)
chileapellidoregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'billing_last_name')))
chileapellidoregistro.send_keys("Moorales") #Escribir apellido del usuario

time.sleep(1)
chilebotonregistrar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'register')))
chilebotonregistrar.click()

time.sleep(15) #Minimizar este número si se quiere que el browser se cierre más rápido

driver.close()
