import os
import re
import requests
import platform
import subprocess
import time as tmp
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
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException

class Op:
    def __init__(self):    
        self.so = platform.system()
        self.python = 'python3' if self.so == 'Linux' else 'python'
        self.directory = os.getcwd()
        self.complet = self.directory + '/capcha' if self.so == 'Linux' else self.directory + '\\capcha'
        self.fracments = self.directory + '/fracmentos' if self.so == 'Linux' else self.directory + '\\fracmentos'

def start_http_server(*args):
    """
    Inicia un servidor HTTP simple.

    Args:
        args[0] (str): Directorio base que indica en que directorio se encuentra con os.getcwd()
        args[1] (str): Indica en que plataforma esta si en linux u otos
        args[2] (str): Nombre del ejecutable de python en linux u otros
    """

    print('[+] Servidor Python Iniciado')
    directory = args[0] + '/fracmentos' if args[1] == 'frac' else args[0]
    os.chdir(directory)
    subprocess.Popen([f"{args[2]}", "-m", "http.server", "9090"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def start_ngrok(*args):
    """
    Inicia un Tunnel HTTPS.

    Args:
        args[0] (str): Directorio base que indica en que directorio se encuentra con os.getcwd()
        args[1] (str): Indica en que plataforma esta si en linux u otos
    """
    print('[+] Servidor Ngrok Iniciado')
    directory = args[0] + '/fracmentos' if args[1] == 'frac' else args[0]
    os.chdir(directory)
    subprocess.Popen(["ngrok", "http", "9090"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def check_ngrok():
    """
    Verifica si el ejecutable de ngrok esta emn el sistema .
    """
    try:
        result = subprocess.run(['ngrok', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if 'ngrok version' in result.stdout:
            return True, result.stdout.strip()
        else:
            return False, Fore.RED + "[-] Ngrok No Instalada Instalatar Manualmente Desde En https://ngrok.com/"
    except FileNotFoundError:
        return False, Fore.RED + "[-] Ngrok No Instalada Instalatar Manualmente Desde En https://ngrok.com/"

def base(*args):
    """
    Base.

    la funcion verifica los directorios y si no existen
    crear los directoriso correctos
    
    Args:
        args[0] (str): Directorio base que indica en que directorio se encuentra con os.getcwd()
        args[1] (str): Indica en que plataforma esta si en linux u otos

    """
    
    complet = args[0] + '/capcha' if args[1] == 'Linux' else args[0] + '\\capcha'
    fracments = args[0] + '/fracmentos' if args[1] == 'Linux' else args[0] + '\\fracmentos'

    if not os.path.exists(complet):
        msg1 = '[+] Creando Directorio Capcha'
        os.mkdir(complet)
        print(msg1)

    if not os.path.exists(fracments):
        msg2 = '[+] Creando Directorio Fracments'
        os.mkdir(fracments)
        print(msg2)

def reset():
    directory = os.getcwd()
    capcha_dir = Path(directory) / "capcha"
    fracmentos_dir = Path(directory) / "fracmentos"

    if capcha_dir.exists():
        for file in capcha_dir.glob("*"):
            try:
                os.remove(file)
            except OSError as e:
                print("Error borrando archivo:", e)

    if fracmentos_dir.exists():
        for file in fracmentos_dir.glob("*"):
            try:
                os.remove(file)
            except OSError as e:
                print("Error borrando archivo:", e)

def service(*args):
    """
    Inicia los srevicion de python y ngrok.

    Args:
        args[0] (str): Directorio base que indica en que directorio se encuentra con os.getcwd()
        args[1] (str): Indica directorio se va a usar si capcha o fracmentos
        args[2] (str): Nombre del ejecutable de python en linux u otros
    """

    complet_P = args[0],args[1],args[2]
    complet_N = args[0],args[1]

    pool = ThreadPool(2)
    pool.apply_async(start_http_server, (complet_P,))
    pool.apply_async(start_ngrok, (complet_N,))

def search_url_ngrok(driver, d1, d2, time_short, time):
    print(Fore.YELLOW+'[+] Llamando a servicios')
    service(d1, d2)

    url = 'http://127.0.0.1:4040/inspect/http'
    driver.execute_script("window.open('about:blank', 'secondtab');")
    driver.switch_to.window("secondtab")
    driver.get(url)

    # try:
    #     local = time_short.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/ul/li/a')))
    #     url_ngrok = local.get_attribute('href')
    #     driver.close()
    #     driver.switch_to.window(driver.window_handles[1])
    #     return url_ngrok
    
    # except TimeoutException:
    #     clear_requests = time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[1]/div/h4/button')))
    #     clear_requests.click()
    #     local = time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/ul/li/a')))
    #     url_ngrok = local.get_attribute('href')
    #     driver.close()
    #     driver.switch_to.window(driver.window_handles[1])
    #     return url_ngrok
    
    # except IndexError:
    #     driver.switch_to.window(driver.window_handles[0])
    #     return url_ngrok
    
    # except NoSuchWindowException:
    #     driver.get(url)

def Download(driver, time):
    url = 'http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx'
    driver.get(url)
    selecccionar = time.until(EC.presence_of_element_located((By.ID, 'cboTipoBusqueda')))
    select = Select(selecccionar)
    select.select_by_value('1')
    xpath_capcha = time.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[3]/td/table[3]/tbody/tr[1]/td/div/span[1]/img')))
    url_img = xpath_capcha.get_attribute('src')
    Download = requests.get(url_img)
    if Download.status_code == 200:
        imagen = Download.content
        nombre_file = 'capcha.jpg'
        try:
            pwd = os.getcwd() + '/capcha/' + nombre_file
            with open(pwd, 'wb') as archivo:
                archivo.write(imagen)
                archivo.close()
        except FileNotFoundError:
            print(Fore.RED + "[-] Archivo No encontrado")
            print(Fore.GREEN + "[+] Creando Directorios")

def evaluation(texto, driver, count, time):
    solo_numeros = re.sub(r'[^\W\d#,.\n]+', '', texto).strip()
    logitud = len(solo_numeros)
    if int(logitud) == 5:
        print(Fore.GREEN + f'[+] Capcha Resuelto: {texto}')
        driver.close()
    else:
        print(f'[+] Capcha No Resuelto: {texto}')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        Download(driver, time)

def check_driver(driver):
    if driver is None:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.get('https://www.google.com/search?client=firefox-b-d&q=ll')
        return False, driver
    return True, driver

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
    time_short = WebDriverWait(driver, 5)
    time_half = WebDriverWait(driver, 5)

    define = 'comp'
    url = 'https://www.google.com/search?client=firefox-b-d&q=ll'

    try:
        file = os.listdir(os.getcwd() + '/capcha')[fichero]

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

        ngrok = search_url_ngrok(driver,define,define , Args[0], Args[1])

        print(Fore.GREEN + "[+] Iniciando Los servicios ")

        enlace = time.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cB9M7[jsname="W7hAGe"]')))
        enlace.send_keys(ngrok + r'/capcha/' + file)
        enlace.send_keys(Keys.RETURN)

        tmp.sleep(4)

        traducir = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[1]/div/div[3]/div/div/span[3]/span')
        traducir.click()
        tmp.sleep(4)

        cuadro_de_texto = time.until(EC.presence_of_element_located((By.CLASS_NAME, 'QeOavc')))
        texto = cuadro_de_texto.text

        evaluation(texto, driver, Args[3], Args[1])


    except FileNotFoundError:
        print(Fore.RED + "[-] Fichero No Encontrado ")

    except TimeoutException:
        driver.close()
        count += 1
        print(Fore.RED + f"[-] Intento Fallido {count}")
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        reset()
        Download(driver, Args[2])

    except IndexError :
        print(Fore.RED + "[-] La Ventana No Existe ")
        driver.close()
        
    except NoSuchWindowException:
        driver.switch_to.window(driver.window_handles[0])

    except NoSuchElementException:
        print('[-] No Se Encontro El Elemnto')
        pass

def formulario_nombres_apellidos(driver, capcha, time):
    Apellido_Paterno = time.until(EC.presence_of_element_located((By.ID, 'txtPriNombre')))
    Apellido_Paterno.send_keys('tony')

    Apellido_Paterno = time.until(EC.presence_of_element_located((By.ID, 'txtSegNombre')))
    Apellido_Paterno.send_keys('ruben')

    Apellido_Paterno = time.until(EC.presence_of_element_located((By.ID, 'txtApePaterno')))
    Apellido_Paterno.send_keys('guizado')

    Apellido_Paterno = time.until(EC.presence_of_element_located((By.ID, 'txtApeMaterno')))
    Apellido_Paterno.send_keys('vasquez')

    box_capcha = time.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/div[1]/table/tbody/tr[3]/td/table[3]/tbody/tr[1]/td/div/span[2]/input')))
    box_capcha.send_keys(capcha)

    Consultar = time.until(EC.presence_of_element_located((By.ID, 'btnConsultar')))
    Consultar.click()

    # evaluation_response_site_capcha(driver, time, 0)

def run():
    instalado, erro = check_ngrok()
    if instalado:
        pass
        # print(Fore.GREEN+f"[+] Ngrok Instalada")
    else:
        print(erro)

    reset()
    print(Fore.GREEN + "[+] Fomateo De Directorios")

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    time = WebDriverWait(driver, 60)
    time_short = WebDriverWait(driver, 5)
    time_half = WebDriverWait(driver, 5)

    Download(driver, time)
    print(Fore.GREEN + "[+] Captcha Descargado")
    print(Fore.GREEN + '[+] Corriendo Servicios')

    while True:
        try:
            complet, capcha_valor = upload_image_complet(driver, 0, time, time_half, 0)
            if complet == 5:
                driver.switch_to.window(driver.window_handles[0])
                formulario_nombres_apellidos(driver, capcha_valor, time)
                tmp.sleep(5)
                driver.quit()
                break
            else:
                count += 1
                print(Fore.RED + f"[-] Intento Fallido {count}")
        except TypeError:
            pass
        except KeyboardInterrupt:
            print(Fore.RED + "[-] Interrupcion del programa ")
            break
