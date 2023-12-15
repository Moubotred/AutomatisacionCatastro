import os
import re
import requests
import platform
import subprocess
import time as tmp
#from PIL import Image
from colorama import Fore
from pathlib import Path
from selenium import webdriver
from multiprocessing.pool import ThreadPool 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchWindowException


def upload_image_complet(self,fichero):
        define = 'comp'
        url = 'https://www.google.com/search?client=firefox-b-d&q=ll'

        try:
            file = os.listdir(self.complet)[int(fichero)] 
        except FileNotFoundError:
            print(Fore.RED+"[-] Directorio No Encontrado ")

        try:
            self.driver.execute_script("window.open('', 'secondtab');")
            self.driver.switch_to.window("secondtab")

            # *------------------- USO DE GOOGLE LENTS  ------------------------------------------------*
            self.driver.get(url)
            tmp.sleep(6)
            lents = self.driver.find_element(By.CLASS_NAME,'nDcEnd').click()
            tmp.sleep(4)
            # *==========================================================================================*


            # *------------------- TUNEL CREADO CON LA IMAGEN  ------------------------------------------*
            ngrok = self.search_url_ngrok(define,define)
            enlace = self.time.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.cB9M7[jsname="W7hAGe"]')))
            enlace.send_keys(ngrok+r'/capcha/'+file)
            enlace.send_keys(Keys.RETURN)
            # *===========================================================================================*

            # *------------------- CONVERSION DE IMAGEN A TEXTO ------------------------------------------*
            tmp.sleep(4)        
            traducir = self.driver.find_element(By.XPATH,'/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[1]/div/div[3]/div/div/span[3]/span')
            traducir.click()
            tmp.sleep(4)
            cuadro_de_texto = self.time_half.until(EC.presence_of_element_located((By.CLASS_NAME,'QeOavc')))
            texto = cuadro_de_texto.text
            # *============================================================================================*


            # *------------- EVALUACION SI EL TEXTO CUMPLE LA REGLA DE 5 NUMEROS --------------------------*
            solo_numeros = re.sub(r'[^\W\d#,.\n]+', '', texto).strip()
            logitud = len(solo_numeros)
            if int(logitud) == 5:
                print(Fore.GREEN+f'[+] Capcha Resuelto: {texto}')
                self.driver.close()
            else:
                # self.count += 1
                print(f'[+] Capcha No Resuelto: {texto}')
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.refresh()    
                self.Download()

            return logitud,solo_numeros
            # *============================================================================================*

        except TimeoutException:
            self.driver.close()
            self.count += 1
            print(Fore.RED+f"[-] Intento Fallido {self.count}")                
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.refresh()
            self.reset()
            self.Download()

        except NoSuchWindowException:
            self.driver.switch_to.window(self.driver.window_handles[0])
        #     self.driver.refresh()
            # self.reset()
            # self.Download()

        except NoSuchElementException:
            print('[-] No Se Encontro El Elemnto')
            # self.driver.quit()