from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.educarchile.cl/user/login"

username = ["mirnita_aguila@hotmail.com", "intialsol@hotmail.com", "mnc.silva2@gmail.com", "ximena-cid@hotmail.com", "rmmarina@hotmail.com", 
"mgbeasq@gmail.com", "lauraslcmccms@hotmail.com", "carla_nicolas1988@hotmail.com", "lavs_smitt@hotmail.com", "vihooper@hotmail.com", 
"Mabel.oliveros@hotmail.com", "gonzalezfrutos@gmail.com", "rosaguerreroq@hotmail.com", "juanapino2@gmail.com", "xmarinao@gmail.com", 
"navarrete_ruth@hotmail.com", "sandraaguayo@gmail.com", "vasquezbasany@gmail.com", "mluisa20036@yahoo.es", "agustin_profematematicas@yahoo.es", "ana.jerez562@gmail.com"]

password = ["tatytiti", "bambino", "monito", "negrito", "mmramirez2011", 
"20marzo2002", "Laura123", "martina31", "almendra", "tomasito", 
"flaca1958", "Laia2533", "maticito10", "juanqui2528", "xmv20940", 
"ruty2006", "eterna12", "nagamby1819", "caulin58", "abcd1234", "ana562"]


users = 0
while users < 21:

    time.sleep(2)
    driver = webdriver.Chrome()
    driver.maximize_window() #Maximiza la ventana del navegador

    url = "https://www.educarchile.cl/user/login"

    driver.get(url)

    time.sleep(1)
    correo = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'name')))
    correo.send_keys(username[users])

    time.sleep(1)
    contrasena = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'pass')))
    contrasena.send_keys(password[users])

    time.sleep(1)
    driver.find_element_by_name("op").click()

    time.sleep(4)
    driver.close()

    users = users + 1


