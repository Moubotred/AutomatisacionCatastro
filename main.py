# para iniciar se tomara al foto en 3 partes

# suminstros
# para transquibir los numeros de los suminstros 
# se usara el resolvedor de capcha numerico 
# guardar con el nombre de suministros.png

# observaciones
# para transquibir las observaciones
# se usara el resolvedor de capcha numerico 
# guardar con el nombre de observaciones.png

# trabajo hechos
# para transquibir trabajo hechos
# se usara el resolvedor de capcha numerico 
# guardar con el nombre de trabajos_hechos.png

# una vez tomada las 3 fotos se procedara a traspasar esos datos a una tabla de datos con pandas

from capcha import capcha
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchWindowException

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
time = WebDriverWait(driver, 6)

Capcha = capcha()
service = Capcha.service('comp','comp')
suministros = Capcha.upload_image_complet(driver,1,'ll')
