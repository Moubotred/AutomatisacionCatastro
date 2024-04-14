import io
from  PIL import Image
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

wait = ''
driver = ''

PreguntasAntes = [(MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'), 
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text=" Si"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[5]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Individual"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'),
                  (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[5]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Subterránea"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'),
                  (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Externo"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Si coincide"]'),
                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtElectrIniCMedicion'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Corresponde al tipo de caja"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/contentPanel'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[1]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="L"]'),
                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'),
                  (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),

                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAlturaCajaMedicion') ,
                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAnchoCajaMedicion'),
                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtProfundidadCajaMedicion'),

                  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'),
                  (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]')
                  ]

PreguntasDespues = [(MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Fachada de cliente(nicho)"]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                    (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]'),
                    (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spFasesMedidor'),
                    (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[7]'),
                    (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'),
                    (MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="ITM (TERMICO)"]'),
                    (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spEstadoProtecCajaMedicion'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Bueno"]'),
                    (MobileBy.XPATH,'//android.widget.Spinner[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/spCapItmCajaMedicion"]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="50"]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[7]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="NYY"]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),
                    (MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtElectrFinCMedicion"]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Baja"]'),
                    (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'),
                    (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Vivienda"]'),
                    (MobileBy.XPATH,'//android.widget.Button[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnAgregarTareasEjecutadas"]'),
                    (MobileBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/rvTareasEjecutadas"]'),
                    (MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Limpieza y ajuste"]'),
                    (MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Cambio de visor"]'),
                    (MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Pintado y rotulado de tapa"]'),
                    (MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Otros"]'),
                    (MobileBy.XPATH,'//android.widget.Button[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnAceptar"]'),
                    (MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtDescTareasEjecutadas"]')
                    ]

start_points = [588, 590, 600, 625, 690, 730, 805]
end_point = -140

def do_scroll(scrollview, start_y, end_y):
        actions = TouchAction(driver)
        actions.press(scrollview, x=0, y=start_y).move_to(scrollview, x=0, y=end_y).release().perform()    

def CatastroAntes():
    scrollview = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/contentFrame"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView[1]')))
    for item in range(len(PreguntasAntes)):
        try:
            Pregunta = wait.until(EC.presence_of_element_located((PreguntasAntes[item][0],PreguntasAntes[item][1]))).click()
            do_scroll(scrollview, start_points[0], 0)
        except TimeoutException:
            Pregunta = wait.until(EC.presence_of_element_located((PreguntasAntes[item][0],PreguntasAntes[item][1]))).send_keys('')
        except IndexError:
            pass

def FinalizarJornada(driver,wait):
    btn_text_fin = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/textView4"]')))
    extract_text_fin = btn_text_fin.text

    if extract_text_fin == 'Finalizar Jornada':
        # print('[+] SECCION YA INICIADA REVISAR PENDIENTES')

        Btn_Pendientes = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
        Btn_Catastro = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
        Btn_Buscar = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()    

        print('Tarea 2 completa')
        
        suministros = ['32634','43054','1231373']

        # for suministro in suministros:
        #     opciones(wait,driver,suministro)

def IniciarJornada(driver,wait):
    Etiqueta_texto_inicio = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada"]')))
    Extractcion_texto_inicio = Etiqueta_texto_inicio.text
    if Extractcion_texto_inicio == 'Iniciar Jornada':
        Btn_iniciar_Jornada = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada'))).click()
        print('Tarea Completa : IniciarJornada [✔]')

def EjecuarPlataforma(wait):
    # errores de la app solucion noRset y forceAppLauncher
    Error_Session = wait.until(EC.presence_of_element_located((MobileBy.ID,'android:id/button1'))).click()

    # Iniciar la secion de usuario y contrasena que ya estan previamente guardadas manualmente en la app
    Ingresar = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()

    # revisar la opciones para abrir sad
    Opcion = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[4]'))).click()

    # iniciar la opcion de SAD
    Opcion_SAD = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()

    print('Tarea Completa : EjecuarPlataforma [✔]')    

# capabilities = dict(
#     platformName='Android',
#     platformVersion='13',
#     automationName='Uiautomator2',
#     deviceName='cancun',
#     appPackage='com.luzdelsur.plataforma.movil',
#     appActivity='com.luzdelsur.plataforma.movil.ui.activity.ProgramasActivity',
#     noReset='true',
#     forceAppLaunch = 'true'
# )

# appium_server_url = 'http://localhost:4723'
# driver = webdriver.Remote(appium_server_url, capabilities)
# wait = WebDriverWait(driver,'25')
obj = False
Conjunto_Preguntas = PreguntasAntes if obj else PreguntasDespues
print(Conjunto_Preguntas)
print(PreguntasAntes)


