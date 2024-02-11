from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


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
driver = webdriver.Remote(appium_server_url, capabilities)

wait = WebDriverWait(driver,'10')

Error_Session = wait.until(EC.presence_of_element_located((AppiumBy.ID,'android:id/button1'))).click()
Ingresar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.plataforma.movil:id/ingresar'))).click()

Opcion = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.luzdelsur.plataforma.movil:id/icon"])[3]'))).click()
Opcion_SAD = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.luzdelsur.plataforma.movil:id/tracks"]/android.widget.LinearLayout[1]'))).click()

Pendientes = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()

try:
	
	catastro = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabPrincipal'))).click()
	buscar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/fabBuscar'))).click()
	buscar_inspecciones = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="android:id/text1"])[2]'))).click()
	seleccionar = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="En inspección"]'))).click()
	
	buscar_inspecciones = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/edtBuscar"]')))
	buscar_inspecciones.send_keys('1605816')

	opcion_realizar = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/imOption'))).click()
	seleccionar_realizar = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.luzdelsur.bt.inspecciones.ui:id/title" and @text="Realizar Inspección"]'))).click()
	
    

except TimeoutException:

	advertencia = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.bt.inspecciones.ui:id/btnAceptar'))).click()
	Pendientes = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.luzdelsur.proydist.sad:id/cvInicioPendientes'))).click()













