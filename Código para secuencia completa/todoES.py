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

######### Registro de usuario #########

time.sleep(1) #Tiempo de espera de 1 segundo para evitar conflictos con la página en la automatización
correoregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
correoregistro.send_keys("andreillaforever@gmail.com") #Escribir correo a registrar

time.sleep(1)
passregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'reg_password')))
passregistro.send_keys("marta12chaoRR") #Escribir contraseña para la cuenta

time.sleep(1)
botonregistro = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'register')))
botonregistro.click()

time.sleep(3) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close() #Cierra la página del navegador


######### Log in de usuario #########

time.sleep(1)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(1)
correologin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
correologin.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya creada

time.sleep(1)
passlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
passlogin.send_keys("ChaoMarta235.") #Escribir contraseña de una cuenta ya creada

time.sleep(1)
botonlogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'login')))
botonlogin.click()

time.sleep(3)


######### Modificar contraseña #########

textomodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'CONTRASEÑA')))
textomodificar.click()

time.sleep(1)
galletamodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'cn-accept-cookie')))
galletamodificar.click()

### Usar nombremodificar y apellidomodificar solo la primera vez que se cambia la contraseña

#time.sleep(1)
#nombremodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'account_first_name')))
#nombremodificar.send_keys('Marta') #Escribir nombre del usuario

#time.sleep(1)
#apellidomodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'account_last_name')))
#apellidomodificar.send_keys('Morales') #Escribir apelido del usuario

time.sleep(1)
passahoramodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password_current')))
passahoramodificar.send_keys("ChaoMarta235.") #Escribir contraseña actual de la cuenta

time.sleep(1)
passnuevamodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password_1')))
passnuevamodificar.send_keys("chaoMarta538.") #Escribir contraseña nueva

time.sleep(1)
mismapassnuevamodi = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'password_2')))
mismapassnuevamodi.send_keys("chaoMarta538.") #Escribir contraseña nueva

time.sleep(1)
guardamodificar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'save_account_details')))
guardamodificar.click()

time.sleep(3) #Minimizar este número si se quiere que el browser se cierre más rápido
driver.close()


######### Restablecer contraseña #########

time.sleep(2)

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

time.sleep(1)
olvidasterestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, '¿Olvidaste la contraseña?')))
olvidasterestablecer.click() #Hace click en el texto que dice '¿Olvidaste la contraseña?' en la página de iniciar sesión

time.sleep(1)
correorestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'user_login')))
correorestablecer.send_keys("marta33.morales99@gmail.com") #Escribir correo de una cuenta ya existente

time.sleep(1)
botonrestablecer = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='woocommerce-Button button']")))
botonrestablecer.click()

time.sleep(10) #Minimizar este número si se quiere que el browser se cierre más rápido

driver.close()