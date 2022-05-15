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
driver.maximize_window()

time.sleep(1)
chilebotonlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='login-top boton-account-top']")))
chilebotonlogin.click()

time.sleep(1)
chileuserlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'username')))
chileuserlogin.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya creada

time.sleep(1)
chilepasslogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
chilepasslogin.send_keys("SoyUnaMarta2") #Escribir contraseña de una cuenta ya creada

time.sleep(1)
chileaccederlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='woocommerce-button button woocommerce-form-login__submit']")))
chileaccederlogin.click()

time.sleep(3)
chilecuentamodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='login-top boton-account-top']")))
chilecuentamodificar.click()

time.sleep(1)
chilelistamodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[id='menu-item-23663']")))
chilelistamodificar.click()

time.sleep(1)
chilepassactualmodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password_current')))
chilepassactualmodificar.send_keys("SoyUnaMarta2") #Escribir contraseña actual de la cuenta

time.sleep(1)
chilepasscambiomodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password_1')))
chilepasscambiomodificar.send_keys("SoyUnaMarta34") #Escribir contraseña nueva

time.sleep(1)
chileconfirmapassmodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password_2')))
chileconfirmapassmodificar.send_keys("SoyUnaMarta34") #Escribir contraseña nueva

time.sleep(1)
chileguardanuevapass = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'save_account_details')))
chileguardanuevapass.click()

time.sleep(15) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()
