from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from GoogleEyes import service,upload_image_complet

class App:
    def __init__(self):
        pass
        # self.capabilities = dict(
        #     platformName='Android',
        #     platformVersion='13',
        #     automationName='uiautomator2',
        #     deviceName='cancun',
        #     appPackage='com.luzdelsur.plataforma.movil',
        #     appActivity='com.luzdelsur.plataforma.movil.ui.activity.ProgramasActivity',
        #     noReset='true',
        #     forceAppLaunch = 'true'
        # )
        # self.appium_server_url = 'http://localhost:4723'        
        # self.driver = webdriver.Remote(self.appium_server_url, self.capabilities)
        # self.wait = WebDriverWait(self.driver,'10')
        # self.loaded = WebDriverWait(self.driver,'20')
        # self.short = WebDriverWait(self.driver,'5')
        
    def Opcions_De_Catastro(self):
        pass
        # Pendientes = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
        # buscar_inspecciones = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
        # seleccionar = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="En inspección"]'))).click()
        # opcion_realizar = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/imOption'))).click()
        # seleccionar_realizar = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/title" and @text="Realizar Inspección"]'))).click()

    def Estado_Laboral(self):

        try:
            btn_text_inicio = self.short.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada"]')))
            extract_text_inicio = btn_text_inicio.text

            if extract_text_inicio == 'Iniciar Jornada':
                btn = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada'))).click()
                print('[+] INICIANDO JORNADA')
                self.Estado_Laboral()

        except TimeoutException:
            btn_text_fin = self.short.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/textView4"]')))
            extract_text_fin = btn_text_fin.text

            if extract_text_fin == 'Finalizar Jornada':
                print('[+] SECCION YA INICIADA REVISAR PENDIENTES')
                Pendientes = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
                catastro = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
                buscar = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()    
                # self.Opcions()
  
    def Session(self):

        # errores de la app solucion noRset y forceAppLauncher
        Error_Session = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'android:id/button1'))).click()
        print('[+] Forsar APP')

        # Iniciar la secion de usuario y contrasena que ya estan previamente guardadas manualmente en la app
        Ingresar = self.wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()
        print('[+] Session iniciada')

        # revisar la opciones para abrir sad
        Opcion = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[3]'))).click()
        print('[+] Opciones SAD')

        # iniciar la opcion de SAD
        Opcion_SAD = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()
        print('[+] Iniciando SAD ')

        try:
            self.Estado_Laboral()
        except Exception as e:
            print('[-] Sucedio un error')

    def foto_suministros(self):        
        service()
        profile_path = r'C:\Users\nimun\AppData\Local\Mozilla\Firefox\Profiles\tped0zt5.automata'
        options=Options()
        options.add_argument("--headless")
        options.add_argument("-profile")
        options.add_argument(profile_path)
        driver = webdriver.Firefox(options=options)
        suministros = upload_image_complet(driver,'suministros.jpeg')
        print('[+] Suministros extraidos exitosamente')


app = App()
app.Session()

# usa el proyecto de resolver 
# capcha numerico

# tomar un foto 
# error login
# inicio de session
# desplegar opciones
# abrir opcion de capataz
# ver pendientes
# desplegar opciones 
# abrir opcion de buscar
# buscar inpecciones
# 