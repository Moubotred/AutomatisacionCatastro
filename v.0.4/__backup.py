import io
import os
from  PIL import Image
from appium import webdriver

from RedNeuronalSimple import ModeloNeuronal
import __test_preguntas as Ts

from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time

class app:
    def __init__(self):
        self.capabilities = dict(
            platformName='Android',
            platformVersion='13',
            automationName='Uiautomator2',
            deviceName='cancun',
            appPackage='com.luzdelsur.plataforma.movil',
            appActivity='com.luzdelsur.plataforma.movil.ui.activity.ProgramasActivity',
            noReset='true',
            forceAppLaunch = 'true'
        )
        self.iconos = ['✔','❌']
        self.scroll_points = [588,590,600,730,730]
        self.pixeles_negativos = -140
        self.appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(self.appium_server_url, self.capabilities)
        self.wait = WebDriverWait(self.driver,15)
        self.PreguntasAntes = [
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spRealizarCatastro'), 
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="$"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTipoSuministro'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Individual"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTecnologiaMedidor'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Electrónico"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTipoConexion'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Subterránea"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTipoSuperficie'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Tierra"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spUbicacionConexion'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Externo"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spRotulado'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Si coincide"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtElectrIniCMedicion'),
                            
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTapaCajaMedicion'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Corresponde al tipo de caja"]'),
                            
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spEstadoTapaCajaMedicion'),
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/contentPanel'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTipoCajaMedicion'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="L"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spEstadoCajaMedicion'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAlturaCajaMedicion') ,
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAnchoCajaMedicion'),
                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtProfundidadCajaMedicion'),

                            (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spChaquetaPlomo'),
                            (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="No"]')
                            ]
        self.PreguntasDespues = [
                            (MobileBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[3]'),
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

    def Scroll(self,scrollview,start_y, end_y):
        # desplazarse
        """
        Realiza un desplazamiento en un ScrollView específico.

        Args:
            scroll_view (WebElement): El elemento ScrollView.
            start_y (int): La posición Y inicial del desplazamiento.
            end_y (int): La posición Y final del desplazamiento.
        """
        actions = TouchAction(self.driver)
        actions.press(scrollview, x=0, y=start_y).move_to(scrollview, x=0, y=end_y).release().perform()    

    def ScrollDespliegewidget(self,inicio,fin):
        # Desplazarpanel
        """
        Realiza un desplazamiento (scroll) en un widget desplegable para mostrar elementos específicos.

        Args:
            self (object): Instancia de la clase que contiene la función.
            inicio (int): Índice del elemento inicial en la lista PreguntasAntes que se usará para hacer clic.
            fin (int): Índice del elemento final en la lista PreguntasAntes que se usará para obtener el widget desplegable.

        Descripción:
            La función realiza las siguientes acciones:

            1. Hace clic en el elemento de la lista PreguntasAntes correspondiente al índice 'inicio'.
            2. Obtiene el widget desplegable (scrollview) a través del elemento correspondiente al índice 'fin'.
            3. Realiza un desplazamiento (scroll) en el widget desplegable utilizando un punto de desplazamiento predefinido (self.scroll_points[3]).

        Ejemplo de uso:
            ScrollDespliegewidget(self, 17, 18)
            ScrollDespliegewidget(self, 10, 11)
        """
        wait = self.wait
        P10 = wait.until(EC.presence_of_element_located((self.PreguntasAntes[inicio][0],self.PreguntasAntes[inicio][1]))).click()
        scrollview_P10 = wait.until(EC.presence_of_element_located((self.PreguntasAntes[fin][0],self.PreguntasAntes[fin][1])))
        self.Scroll(scrollview_P10,self.scroll_points[3],-140)
        
    def TomarCapturaInformacion(self,captura_imagen,nombre_de_imagen_guardada):
        driver = self.driver
        screenshot = driver.get_screenshot_as_png()

        size = captura_imagen.size
        image = Image.open(io.BytesIO(screenshot))

        Desplaza_left = 0 # desplaza_left
        Desplazar_top = int(size['width'] / 2.7) # 1080 / 2.7 = 400 Desplazar_top
        Ancho = size['width'] # 1080 Ancho
        Altura = int(size['height'] - Desplazar_top) #2400 - 400 = 2000 Altura
        
        im1 = image.crop((Desplaza_left, Desplazar_top, Ancho, Altura))
        im1.save(f'{nombre_de_imagen_guardada}.png')

    def ExtraccionInformacion(self,driver):

        wait = self.wait
        SadFotos = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageButton[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/btnVerFotoSAD"]'))).click() 
        Imagenes = wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH,'//android.widget.ListView[@resource-id="com.luzdelsur.proydist.sad:id/lstFoto"]/android.widget.LinearLayout')))

        for Imagen in range(1,len(Imagenes)+1):
            AbrirFoto = wait.until(EC.presence_of_element_located((MobileBy.XPATH,f'(//android.widget.ImageView[@resource-id="com.luzdelsur.proydist.sad:id/imgFoto"])[{Imagen}]'))).click()
            Captura_imagen = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.google.android.apps.photos:id/photos_photofragment_components_background_photo_view')))
            nombre_de_imagen_guardada = os.path.join(os.getcwd()[:-39],'Pictures','FotoSuministro',f'Imagen_00{Imagen}')
            self.TomarCapturaInformacion(Captura_imagen,nombre_de_imagen_guardada)
            time.sleep(5)        
            driver.back()

        driver.back()
        return Imagen # retorna el numero de las fotos que se tomaron

    def ResolverPregunta(self,inidice_pregunta):
        Contador_Indice_Preguntas = len(self.PreguntasAntes)
        
        pass

    def AccionesPreguntas(self,indice_pregunta, indice_respuesta, enviar_texto=None):
        """
        Realiza acciones en los elementos de la lista PreguntasAntes.

        Args:
            self (object): Instancia de la clase que contiene la función.
            indice_pregunta (int): Índice de la pregunta en la lista PreguntasAntes.
            indice_respuesta (int, opcional): Índice de la respuesta en la lista PreguntasAntes.
                Si es None, no se realizará acción en la respuesta.
            enviar_texto (str, opcional): Texto que se enviará al elemento de la pregunta.
                Si es None, no se enviará texto.

        Descripción:
            La función realiza las siguientes acciones en los elementos de la lista PreguntasAntes:

            1. Si indice_respuesta no es None, se hace clic en el elemento de la pregunta
            y luego en el elemento de la respuesta.

            2. Si enviar_texto no es None, se envía el texto al elemento de la pregunta.

            3. Si indice_respuesta y enviar_texto son None, solo se hace clic en el elemento
            de la pregunta.

        Ejemplo de uso:
            AccionesPreguntas(self, 0, 1, "Texto de ejemplo")
            AccionesPreguntas(self, 2, 3)
            AccionesPreguntas(self, 4, enviar_texto="Otro texto")
            AccionesPreguntas(self, 5)
        """
        wait = self.wait
        if indice_respuesta is not None:
            Pa = wait.until(EC.presence_of_element_located((self.PreguntasAntes[indice_pregunta][0], self.PreguntasAntes[indice_pregunta][1]))).click()
            Post = self.ResolverPregunta(indice_respuesta)
            # Ra = wait.until(EC.presence_of_element_located((self.PreguntasAntes[indice_respuesta][0], self.PreguntasAntes[indice_respuesta][1]))).click()
        if enviar_texto:
            wait.until(EC.presence_of_element_located((self.PreguntasAntes[indice_pregunta][0], self.PreguntasAntes[indice_pregunta][1]))).send_keys(enviar_texto)

        if indice_respuesta is None and enviar_texto is None:
            wait.until(EC.presence_of_element_located((self.PreguntasAntes[indice_pregunta][0], self.PreguntasAntes[indice_pregunta][1]))).click()

    def CatastroPreguntas_widget(self,widget):
        """
        Responde a las preguntas del catastro según el estado y las preguntas proporcionadas.

        Args:
            self (object): Instancia de la clase que contiene la función.
            widget (int): El índice del widget ScrollView.

        Descripción:
            La función realiza las siguientes acciones:

            1. Obtiene el elemento ScrollView correspondiente al índice `widget`.
            2. Intenta responder a las preguntas del catastro utilizando las funciones `AccionesPreguntas`,
            `Scroll` y `ScrollDespliegewidget`.
            3. Utiliza la lista `PreguntasAntes` para obtener los localizadores (identificadores o XPath) de
            los elementos de las preguntas y respuestas.
            4. Realiza desplazamientos (scroll) en el ScrollView utilizando los puntos definidos en `self.scroll_points`.
            5. Envía texto a los campos de entrada cuando es necesario.
            6. Si se completan todas las acciones correctamente, imprime un mensaje de éxito.
            7. Si ocurre un error de tiempo de espera (`TimeoutException`), imprime un mensaje de error.
            8. Si ocurre cualquier otro error (`Exception`), imprime un mensaje de error genérico.

        Ejemplo de uso:
            CatastroPreguntas_widget(self, 1)
            CatastroPreguntas_widget(self, 2)
        """
        wait = self.wait
        scrollview = wait.until(EC.presence_of_element_located((MobileBy.XPATH,f'//android.widget.FrameLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/contentFrame"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView[{widget}]')))

        try:    

            self.AccionesPreguntas(0,1)

            self.Scroll(scrollview,self.scroll_points[0],-140)

            self.AccionesPreguntas(2,3)
            self.AccionesPreguntas(4,5)
            self.AccionesPreguntas(6,7)

            self.Scroll(scrollview,self.scroll_points[1],-140)

            self.AccionesPreguntas(8,9)
            self.AccionesPreguntas(10,11)

            self.Scroll(scrollview,self.scroll_points[2],-140)

            self.AccionesPreguntas(12,13)
            self.AccionesPreguntas(14,None,'324')
            self.AccionesPreguntas(15,16)
            self.ScrollDespliegewidget(17,18)
            self.AccionesPreguntas(19,None,None)
            self.AccionesPreguntas(20,21)

            self.Scroll(scrollview,self.scroll_points[3],-140)

            self.AccionesPreguntas(22,23)
            self.AccionesPreguntas(24,None,'50')
            self.AccionesPreguntas(25,None,'23')
            self.AccionesPreguntas(26,None,'20')
            self.AccionesPreguntas(27,28)

            print(f'[-] Tarea Completa : CatastroPreguntas_widget [{self.iconos[0]}]')

        except TimeoutException as e:
            print('Error : ',e)

        except Exception as e:
            print('Error : ',e)

    def BuscarSuministro(self,conjunto_suministro): 
        """
        Busca un suministro específico e inicia el proceso de inspección.

        Args:
            self (objeto): Instancia de la clase que contiene la función.
            conjunto_suministro (str): El número de suministro a buscar.

        Descripción:
            La función realiza las siguientes acciones:

            1. Encuentra el campo de búsqueda y envía el número de suministro proporcionado.
            2. Si el texto en el campo de búsqueda coincide con el número de suministro:
                a. Hace clic en el botón "Opciones".
                b. Hace clic en la opción "Realizar Inspección".
                c. Selecciona la opción "Medición directa" en el cuadro de diálogo.
                d. Hace clic en el botón "Aceptar".
            3. Imprime un mensaje de éxito si se completan todas las acciones.
        """
        wait = self.wait
        suministro = conjunto_suministro
        BuscarSuministro = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtBuscar"]')))
        BuscarSuministro.send_keys(suministro)

        if BuscarSuministro.text == suministro:
            
            Opciones = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/imOption'))).click()
            RealizarInspeccion = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.LinearLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/content"])[1]'))).click()

            BtnTipoMedicion = wait.until(EC.presence_of_element_located((MobileBy.ID,'android:id/text1'))).click()

            MedicionDirecta = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Medición directa"]'))).click()
            BtnAceptar = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/btnAceptar'))).click()

            print(f'[-] Tarea Completa : BuscarSuministro [{self.iconos[0]}]')

    def Analizar_Estado_Jornada(self):  
        """
        Analiza el estado de la jornada y realiza acciones según el resultado.

        Descripción:
            La función realiza las siguientes acciones:

            1. Verifica si la jornada ha sido iniciada o finalizada.
            2. Si la jornada no ha sido iniciada, hace clic en el botón "Iniciar Jornada" y vuelve a llamar a la función `Analizar_Estado_Jornada`.
            3. Si la jornada ha sido finalizada, imprime un mensaje de éxito y realiza acciones adicionales:
                a. Hace clic en el botón "Pendientes".
                b. Hace clic en el botón "Catastro".
                c. Hace clic en el botón "Buscar".
            4. Si ocurre un error de tiempo de espera (`TimeoutException`), no realiza ninguna acción.
        """     
        wait = WebDriverWait(self.driver,'15')
        try:
            Etiqueta_texto_inicio = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada"]')))
            Extraccion_texto_inicio = Etiqueta_texto_inicio.text

            if Extraccion_texto_inicio == 'Iniciar Jornada':
                btn_inicio_jornada = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.proydist.sad:id/txtInicioIniciarJornada'))).click()
                self.Analizar_Estado_Jornada()
                print(f'[-] Tarea Incompleta : Analizar_Estado_Jornada [{self.iconos[1]}]')
                print('[-] Corrigieno Error: llamando nuevamente a la funcion Analizar_Estado_Jornada')

        except TimeoutException:
            Etiqueta_texto_final = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.proydist.sad:id/textView4"]')))
            extract_text_fin = Etiqueta_texto_final.text

            if extract_text_fin == 'Finalizar Jornada':
                print(f'[-] Tarea Completa : Analizar_Estado_Jornada [{self.iconos[0]}]')
                Btn_Pendientes = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()
                Btn_Catastro = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
                Btn_Buscar = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()    
                
    def Iniciar_Session_App(self):
        """
        Inicia la sesión en la aplicación y realiza acciones necesarias.

        Descripción:
            La función realiza las siguientes acciones:

            1. Maneja un posible error de sesión haciendo clic en el botón "OK".
            2. Inicia la sesión del usuario haciendo clic en el botón "Ingresar".
            3. Abre la opción de SAD (Sistema de Atención al Distribuidor) en la aplicación.
            4. Imprime un mensaje de éxito si se completan todas las acciones.
        """

        wait = self.wait
        # errores de la app solucion noRset y forceAppLauncher
        Error_Session = wait.until(EC.presence_of_element_located((MobileBy.ID,'android:id/button1'))).click()

        # Iniciar la secion de usuario y contrasena que ya estan previamente guardadas manualmente en la app
        Ingresar = wait.until(EC.presence_of_element_located((MobileBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()

        # revisar la opciones para abrir sad
        Opcion = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[4]'))).click()

        # iniciar la opcion de SAD
        Opcion_SAD = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()
        
        print(f'[-] Tarea Completa : Iniciar_Session_App [{self.iconos[0]}]')

    def plataforma(self):

        """
        Ejecuta el flujo principal de la aplicación.
        """

        wait = WebDriverWait(self.driver,'25')
        self.Iniciar_Session_App()

        try:
            self.Analizar_Estado_Jornada()
            self.BuscarSuministro('98585')
            self.ExtraccionInformacion()
            self.CatastroPreguntas_widget(1)

        except TimeoutException:
            pass
            # IniciarJornada(driver,wait)
    
# launcher = app()
# launcher.plataforma()

PreguntasAntes = [
                (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spRealizarCatastro'), 
                (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="$"]'),
                (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/spTipoSuministro'),
                (MobileBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="$"]')
                 ]




