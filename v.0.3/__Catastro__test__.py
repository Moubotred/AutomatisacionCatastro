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

# wait = ''

# scrollview = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/contentFrame"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView[1]')))

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
                  (MobileBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/edtAlturaCajaMedicion'),
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

def CatastroAntes():
    print(PreguntasDespues)
    pass
#     Pregunta = wait.until(EC.presence_of_element_located(())).click()

CatastroAntes()

