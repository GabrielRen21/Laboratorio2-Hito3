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
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(1) #Tiempo de espera de 1 segundo para evitar conflictos con la página en la automatización
olvidasterestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, '¿Olvidaste la contraseña?')))
olvidasterestablecer.click() #Hace click en el texto que dice '¿Olvidaste la contraseña?' en la página de iniciar sesión

time.sleep(1)
correorestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'user_login')))
correorestablecer.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya existente

time.sleep(1)
botonrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='woocommerce-Button button']")))
botonrestablecer.click()

time.sleep(15) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()
