from selenium import webdriver as web
from appium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy
from GoogleEyes import service,upload_image_complet

def Verificacion(wait,suministro): 
        # wait = WebDriverWait(driver,'10')

        suministro.append('373513')

        Pendientes = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
        catastro = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
        buscar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()    

        Estados = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
        Inspeccciones = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="En inspección"]'))).click()

        # print(suministro)

        for sum in range(len(suministro)):
            Buscar_Inspecciones = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtBuscar"]')))
            Buscar_Inspecciones.send_keys(suministro[sum])
            
            # verificacion_suministro = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/txtCodigo"]'))).text
            # if sum == verificacion_suministro:
            #     print(f'[+] suministro {sum} valido')
            # else:
            #     print(f'[+] suministro NO {sum} valido')

        # opciones = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/imOption"]'))).click()
        # Realizar_inspeccion = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/title" and @text="Realizar Inspección"]'))).click()

def Extraccion_Fotos():# wait
    service()
    profile_path = r'C:\Users\nimun\AppData\Local\Mozilla\Firefox\Profiles\tped0zt5.automata'
    options=Options()

    # options.add_argument("--headless")
    options.add_argument("-profile")

    options.add_argument(profile_path)

    driver1 = web.Firefox(options=options)
    
    suministros = upload_image_complet(driver1,'suministros.jpeg')
    # print('[+] Suministros extraidos')
    # print(suministros)

    
    driver2 = web.Firefox(options=options)
    observaciones = upload_image_complet(driver2,'observaciones.jpeg')
    # print('[+] Observaciones extraidos')
    # print(observaciones)

    
    driver3 = web.Firefox(options=options)
    trabajos_hechos = upload_image_complet(driver3,'trabajos.jpeg')
    # print('[+] Trabajos extraidos')
    # print(trabajos_hechos)

    driver4 = web.Firefox()
    wait = WebDriverWait(driver4,'15')

    Verificacion(wait,suministros)

def Inspeccciones(driver,short):

    try:
        btn_text_inicio = short.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada"]')))
        extract_text_inicio = btn_text_inicio.text

        if extract_text_inicio == 'Iniciar Jornada':
            btn = short.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada'))).click()
            print('[+] INICIANDO JORNADA')
            Inspeccciones(driver,short)

    except TimeoutException:
        btn_text_fin = short.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/textView4"]')))
        extract_text_fin = btn_text_fin.text

        if extract_text_fin == 'Finalizar Jornada':
            print('[+] SECCION YA INICIADA REVISAR PENDIENTES')
            Extraccion_Fotos()
            # Verificacion(short,'373513')


def Lanzar_App(driver):

    wait = WebDriverWait(driver,'15')

    # errores de la app solucion noRset y forceAppLauncher
    Error_Session = wait.until(EC.presence_of_element_located((AppiumBy.ID,'android:id/button1'))).click()
    print('[+] Forsar APP')

    # Iniciar la secion de usuario y contrasena que ya estan previamente guardadas manualmente en la app
    Ingresar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()
    print('[+] Session iniciada')

    # revisar la opciones para abrir sad
    Opcion = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[3]'))).click()
    print('[+] Opciones SAD')

    # iniciar la opcion de SAD
    Opcion_SAD = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()
    print('[+] Iniciando SAD ')

    try:
        Inspeccciones(driver,wait)
    except Exception as e:
        print(f'[-] Sucedio un error {e}')

capabilities = dict(
        platformName='Android',
        platformVersion='13',
        automationName='uiautomator2',
        deviceName='cancun',
        appPackage='com.luzdelsur.plataforma.movil',
        appActivity='com.luzdelsur.plataforma.movil.ui.activity.ProgramasActivity',
        noReset='true',
        forceAppLaunch = 'true'
    )
appium_server_url = 'http://localhost:4723'        
driver = webdriver.Remote(appium_server_url,capabilities)

Lanzar_App(driver)
# Extraccion_Fotos()


