import re
import time
import os
import subprocess
import time as tmp
import platform
import pandas as pd
from pyngrok import ngrok
from colorama import Fore
from selenium import webdriver
from multiprocessing.pool import ThreadPool 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options

so = platform.system() 
python = 'python3'if so == 'Linux'else 'python'

def start_http_server(complet,*args):
    if complet == 'fracmentos':
        os.chdir(os.getcwd()+f'//{args[0]}')
        subprocess.Popen([f"{python}", "-m", "http.server", "9090"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        # print('[+] Corriendo Servidor')

    elif complet == 'completo':
        os.chdir(os.getcwd())
        subprocess.Popen([f"{python}", "-m", "http.server", "9090"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        # print('[+] Corriendo Servidor')

def start_ngrok():
    PUERTO = 9090
    ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
    url_publica = ngrok.connect(PUERTO)
    #base = url_publica.split()[1]
    
def service():
    pool = ThreadPool(2)
    pool.apply_async(start_http_server('completo'))
    pool.apply_async(start_ngrok())
    tunnels = ngrok.get_tunnels()

    global base_ngrok
    base_ngrok = str(tunnels).split('"')[1]

    print(Fore.GREEN + "[+] Iniciando Los servicios ")
    
def upload_image_complet(driver, fichero, *Args):# define ,time_half, time,
    """
    La funcion se encarga de crear un servidor en python y ngrok
    para poder subir la imagen descargada y que encuentre localmente,
    sube la imagen a google lents y la convierte la imagen a texto

    Args:
        args[0] (str): Directorio base que indica en que directorio se encuentra con os.getcwd()
        args[1] (str): Indica en que plataforma esta si en linux u otos
    """
    
    time = WebDriverWait(driver, 60)
    short = WebDriverWait(driver, 10)

    define = 'comp'
    url = 'https://www.google.com/search?client=firefox-b-d&q=ll'

    try:
        window_handles = driver.window_handles
        if len(window_handles) > 1:
            try:
                driver.execute_script("window.open('', 'secondtab');")
                driver.switch_to.window("secondtab")
                driver.get(url)
            except NoSuchWindowException:
                print(Fore.GREEN + "[+] No Se Encontraron Ventanas Activas ")    
        else:
            # Si no hay ventanas adicionales abiertas, abre una nueva pestaña usando get()
            driver.get(url)
            print(Fore.GREEN + "[+] Iniciando Ventanas ")

        tmp.sleep(6)
        lents = driver.find_element(By.CLASS_NAME, 'nDcEnd').click()
        tmp.sleep(4)

        print(Fore.GREEN + "[+] Click En La Lupa")

        enlace = time.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cB9M7[jsname="W7hAGe"]')))
        enlace.send_keys(base_ngrok+'/'+ fichero)
        # tmp.sleep(10)

        enlace.send_keys(Keys.RETURN)

        tmp.sleep(4)

        traducir = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[1]/div/div[3]/div/div/span[3]/span')
        traducir.click()
        tmp.sleep(4)

        lista_informacion = []

        observaciones = time.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@dir="ltr"]/div')))      

        for item in range(1,len(observaciones)+1):
            observaciones = time.until(EC.presence_of_element_located((By.XPATH,f'//div[@class="QeOavc"]/div[{item}]')))
            lista_informacion.append(observaciones.text)

        driver.quit()

        return lista_informacion

        # verificador(texto)
        # df = pd.DataFrame(texto)
        # print(df)
        # tmp.sleep(10)
        # evaluation(texto, driver, Args[3], Args[1])

    except FileNotFoundError:
        print(Fore.RED + "[-] Fichero No Encontrado ")

    except TimeoutException:
        driver.close()
        # count += 1
        # print(Fore.RED + f"[-] Intento Fallido {count}")
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        # reset()
        # Download(driver, Args[2])

    except IndexError :
        print(Fore.RED + "[-] La Ventana No Existe ")
        driver.close()
        
    except NoSuchWindowException:
        driver.switch_to.window(driver.window_handles[0])

    except NoSuchElementException:
        print('[-] No Se Encontro El Elemnto')
        pass
    
# def verificador(driver,time,valor):
    code = driver.page_source
    # suministro = time.until(EC.presence_of_element_located((By.XPATH,f'/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div[3]/div/div/div[{item}]')))
    # bs = suministro.text

    # tmp.sleep(10)

    pass

# service()
# # profile_path = r'C:\Users\nimun\AppData\Local\Mozilla\Firefox\Profiles\tped0zt5.automata'
# options=Options()
# options.add_argument("--headless")
# # options.add_argument("-profile")
# # options.add_argument(profile_path)
# driver = webdriver.Firefox(options=options)
# # upload_image_complet(driver,'ops.jpeg')
# # upload_image_complet(driver,os.path.join(os.getcwd(),'tmp','imagen_recortada.jpg'))
# base = upload_image_complet(driver,'tmp/imagen_recortada.jpg')
# numeros = [item for item in base if re.sub(r'\D', '', item)]
# print(numeros)





# # start_time = time.time()
# end_time = time.time()
# elapsed_time = end_time - start_time
# elapsed_time_seconds = round(elapsed_time)
# print(f"Tiempo de ejecución: {elapsed_time_seconds} segundos")


# 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


# https://stackoverflow.com/questions/77469966/openai-api-error-you-tried-to-access-openai-completion-but-this-is-no-longer

# import os
# from openai import OpenAI
# client = OpenAI(api_key="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")

# # OpenAI.api_key = "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"

# completion = client.completions.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="Say this is a test",
#   max_tokens=7,
#   temperature=0
# )

# print(completion.choices[0].text)