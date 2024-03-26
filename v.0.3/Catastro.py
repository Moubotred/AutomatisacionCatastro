from  PIL import Image
import io
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.keys import Keys
import time as tmp
# from _Individual import OpcionesAntes as OA

# OpcionesAntes = OA()

def CatastroPreguntas_widget_1(wait):
    scrollview = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/contentFrame"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView[1]')))
    
    # opcion1 = OpcionesAntes.EsPosibleRealizarCatastro(numero=f'{numerodefotos}')
    opcion1 = 'Si'
    P1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
    R1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{opcion1}"]'))).click()
    
    start_points = [588, 590, 600, 625, 690, 720, 730,805]
    end_point = 147

    do_scroll(scrollview, start_points[0], end_point)

    # brain = 
    P2 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[5]'))).click()
    R2 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Individual"]'))).click()

    P3 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'))).click()
    R3 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'))).click()

    do_scroll(scrollview, start_points[1], end_point)

    P4 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[5]'))).click()
    R4 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Subterránea"]'))).click()

    P5 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'))).click()
    R5 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'))).click()

    do_scroll(scrollview, start_points[2], end_point)

    P6 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    R6 = wait.until(EC.presence_of_element_located( (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Externo"]'))).click()

    do_scroll(scrollview, start_points[3], end_point)

    P7 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    R7 = wait.until(EC.presence_of_element_located( (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Si coincide"]'))).click()

    do_scroll(scrollview, start_points[6], 0)

    P8 =  wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtElectrIniCMedicion'))).send_keys('0.012')

    P9 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'))).click()
    R9 = wait.until(EC.presence_of_element_located( (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Corresponde al tipo de caja"]'))).click()

    P10 = wait.until(EC.presence_of_element_located(  (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    P10_1 = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/contentPanel')))

    # dimensions = P10_1.rect #|el .rect devuelve un diccionario con los valores de ancho alto y otros vaslores de un widget

    do_scroll(P10_1, start_points[7], 0)
    #//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]
    P10 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'))).click()
    
    do_scroll(scrollview, 690, -10)

    P11 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[1]'))).click()
    R11 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="L"]'))).click()


    P12 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
    R12 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'))).click()

    do_scroll(scrollview, 600,0)

    P13 = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAlturaCajaMedicion'))).send_keys('50')
    P14 = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAnchoCajaMedicion'))).send_keys('19')
    P15 = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtProfundidadCajaMedicion'))).send_keys('18')

    P16 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
    R16 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]'))).click()

    print('Tarea 4 Widget 1 Resuelto')

def CatastroPreguntas_widget_2(wait):
    scrollview = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/contentFrame"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView[2]')))

    P1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'))).click()
    R1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Fachada de cliente(nicho)"]'))).click()

    P2 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    R2 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]'))).click()

    P3 =  wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spFasesMedidor'))).click()
    R3 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'))).click()

    P4 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[7]'))).click()
    R4 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[3]'))).click()

    do_scroll(scrollview, 600, -140)

    P5 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'))).click()
    R5 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.CheckedTextView[@resource-id="android:id/text1"])[2]'))).click()

    P6 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    R6 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="ITM (TERMICO)"]'))).click()

    P7 =  wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spEstadoProtecCajaMedicion'))).click()
    R7 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Bueno"]'))).click()

    P8 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.Spinner[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/spCapItmCajaMedicion"]'))).click()
    R8 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="50"]'))).click()

    do_scroll(scrollview, 600, -140)

    P9 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[7]'))).click()
    R9 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="NYY"]'))).click()

    do_scroll(scrollview, 600, -140)

    P10 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'))).click()
    R10 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'))).click()

    do_scroll(scrollview, 700, -140)    

    P11 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtElectrFinCMedicion"]'))).send_keys('0.012')

    P12 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[6]'))).click()
    R12 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Baja"]'))).click()

    do_scroll(scrollview, 600, -140)    

    P13 =  wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[4]'))).click()
    R13 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Vivienda"]'))).click()

    TEJ = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.Button[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnAgregarTareasEjecutadas"]'))).click()
    OPC = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/rvTareasEjecutadas"]')))
    CHEK_1 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Limpieza y ajuste"]'))).click()
    CHEK_2 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Cambio de visor"]'))).click()
    CHEK_3 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Pintado y rotulado de tapa"]'))).click()
    # print(OPC.rect)
    do_scroll(OPC, 200, -700*2)    
    CHEK_4 = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckBox[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/cbTareaEjecutada" and @text="Otros"]'))).click()
    BTN = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.Button[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnAceptar"]'))).click()
    OTROS = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtDescTareasEjecutadas"]'))).send_keys('biselado')

    # print(scrollview.rect)

    print('Tarea 5 Widget 2 Resuelto')

def screenshot(ObtImg,name):
    screenshot = driver.get_screenshot_as_png()

    size = ObtImg.size
    image = Image.open(io.BytesIO(screenshot))

    Desplaza_left = 0 # desplaza_left
    Desplazar_top = int(size['width'] / 2.7) # 1080 / 2.7 = 400 Desplazar_top
    Ancho = size['width'] # 1080 Ancho
    Altura = int(size['height'] - Desplazar_top) #2400 - 400 = 2000 Altura
    
    im1 = image.crop((Desplaza_left, Desplazar_top, Ancho, Altura))

    im1.save(f'{name}.png')

def FotosSad(wait,driver):
    SadFotos = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.ImageButton[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnVerFotoSAD"]'))).click() 
    Imagenes = wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,'//android.widget.ListView[@resource-id="com.luzdelsur.proydist.sad:id/lstFoto"]/android.widget.LinearLayout')))

    for Imagen in range(1,len(Imagenes)+1):
        AbrirFoto = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f'(//android.widget.ImageView[@resource-id="com.luzdelsur.proydist.sad:id/imgFoto"])[{Imagen}]'))).click()
        ObtenerImg = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.google.android.apps.photos:id/photos_photofragment_components_background_photo_view')))
        screenshot(ObtenerImg,f'C:\\Users\\nimun\\Documents\\scripts\\examples\\opencv\\__fotos_sad__\\Imagen_00{Imagen}')
        tmp.sleep(5)        
        driver.back()
    driver.back()
    return Imagen # retorna el numero de las fotos que se tomaron

def do_scroll(scrollview, start_y, end_y):
        actions = TouchAction(driver)
        actions.press(scrollview, x=0, y=start_y).move_to(scrollview, x=0, y=end_y).release().perform()    

def opciones(wait,driver,suministro):
    sum = suministro
    BuscarSuministro = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtBuscar"]')))
    BuscarSuministro.send_keys(sum)
    if BuscarSuministro.text == sum:
        # print('Tarea 2 completa')
        Opciones = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/imOption'))).click()
        RealizarInspeccion = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.LinearLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/content"])[1]'))).click()

        BtnTipoMedicion = wait.until(EC.presence_of_element_located((AppiumBy.ID,'android:id/text1'))).click()

        MedicionDirecta = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Medición directa"]'))).click()
        BtnAceptar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/btnAceptar'))).click()
        
        print('Tarea 3 Completa')


        try:
            # Preaccion = FotosSad(wait,driver)
            # Preaccion = '6'
            # CatastroPreguntas_widget_1(wait,Preaccion)
            CatastroPreguntas_widget_1(wait)
            CatastroPreguntas_widget_2(wait)

            driver.back()
            BTN = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.Button[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnAceptar"]'))).click()

        except Exception as e:
            print('Error: ',e)
            
def FinalizarJornada(driver,wait):
    btn_text_fin = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/textView4"]')))
    extract_text_fin = btn_text_fin.text

    if extract_text_fin == 'Finalizar Jornada':
        # print('[+] SECCION YA INICIADA REVISAR PENDIENTES')

        Btn_Pendientes = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
        Btn_Catastro = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
        Btn_Buscar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()    

        print('Tarea 2 completa')
        
        suministros = ['32634','43054','1231373']

        for suministro in suministros:
            opciones(wait,driver,suministro)

def IniciarJornada(driver,wait):
    btn_text_inicio = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada"]')))
    extract_text_inicio = btn_text_inicio.text
    if extract_text_inicio == 'Iniciar Jornada':
        btn = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada'))).click()
        # print('[+] INICIANDO JORNADA')
        print('Tarea 2 Completa')

def EjecuarApp(wait):
    # errores de la app solucion noRset y forceAppLauncher
    Error_Session = wait.until(EC.presence_of_element_located((AppiumBy.ID,'android:id/button1'))).click()

    # Iniciar la secion de usuario y contrasena que ya estan previamente guardadas manualmente en la app
    Ingresar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()

    # revisar la opciones para abrir sad
    Opcion = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[4]'))).click()

    # iniciar la opcion de SAD
    Opcion_SAD = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()
    
    print('Tarea 1 Completa')

capabilities = dict(
    platformName='Android',
    platformVersion='13',
    automationName='Uiautomator2',
    deviceName='cancun',
    appPackage='com.luzdelsur.plataforma.movil',
    appActivity='com.luzdelsur.plataforma.movil.ui.activity.ProgramasActivity',
    noReset='true',
    forceAppLaunch = 'true'
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, capabilities)
wait = WebDriverWait(driver,'25')

EjecuarApp(wait)

try:
    FinalizarJornada(driver,wait)
except TimeoutException:
    IniciarJornada(driver,wait)
