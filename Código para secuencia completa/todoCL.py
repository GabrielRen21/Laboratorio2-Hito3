from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

###Credenciales de un correo de google que se puede usar
# marta33.morales99@gmail.com
# marta1Morales2

######### Registro de usuario ######### 

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

time.sleep(2) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()


######### Log in de usuario #########

driver = webdriver.Chrome()
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


######### Modificar contraseña #########

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

time.sleep(3) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()


######### Restablecer contraseña #########

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

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

time.sleep(10) #Minimizar este número si se quiere que el browser se cierre más rápido

driver.close()
