import re
import os
import random
from PIL import Image
import GoogleEyes as Gs
from selenium import webdriver
from RedNeuronalSimple import ModeloNeuronal
from selenium.webdriver.firefox.options import Options

# EmulacionDirectorio = len(os.listdir(os.path.join(os.getcwd(),'__fotos_sad__')))

def spRealizarCatastro(EmulacionDirectorio = None):    
    
    try:
        if EmulacionDirectorio >= 5 :
            return 'Si'
        
        if EmulacionDirectorio == 4:
            return 'Parcial'

        if EmulacionDirectorio <= 2:
            return 'No'

    except Exception as E:
        pass

def spTipoSuministro(FotoCatastro = None):
    respuesta = ModeloNeuronal(os.path.join(os.getcwd(),'__modelos__','spTipoSuministro'),'mdSuministro','etsuministro',FotoCatastro)
    return respuesta

def spTecnologiaMedidor(FotoMedidor = None):
    respuesta = ModeloNeuronal(os.path.join(os.getcwd(),'__modelos__','spTecnologiaMedidor'),'mdSuministro','etsuministro',FotoMedidor)
    return respuesta

def spTipoConexion(FotoConexion = None):
    Conexion = ['Subterránea','Aérea']
    Generar = random.randint(0,1)
    return Conexion[Generar]

def spTipoSuperficie(FotoSuperficie = None):
    Conexion = ['Concreto','Tierra','Jardin']
    Generar = random.randint(0,2)
    return Conexion[Generar]

def spTipoRedAerea(FotoRed = None):
    Conexion = ['Red CPI','Red autoportante','Fin de línea']
    Generar = random.randint(0,1)
    return Conexion[Generar]

def spUbicacionConexion(FotoUbicacion = None):
    Conexion = ['Interno accesible','Externo']
    Generar = random.randint(0,1)
    return Conexion[Generar]

def spTipoMastil(FotoMastil):
    pass

def spRotulado(FotoRotulado = None, suministro = None):
    os.makedirs('tmp', exist_ok=True)
    ImagenProcesar = Image.open(FotoRotulado)
    width,height = ImagenProcesar.size

    # Definir las coordenadas de recorte (izquierda, superior, derecha, inferior)
    left = 50
    top = 50
    right = 900
    bottom = width/2 + 100

    # Recortar la imagen
    cropped_image = ImagenProcesar.crop((left, top, right, bottom))

    # Guardar la imagen recortada
    cropped_image.save(os.path.join(os.getcwd(),'tmp',"imagen_recortada.jpg"))

    Gs.service()
    options=Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    base = Gs.upload_image_complet(driver,'tmp/imagen_recortada.jpg')
    numeros = [item for item in base if re.sub(r'\D', '', item)]
    CoincidenciasListaNumeros = [item[:4] for item in numeros]
    CoincidenciasListaSuministro = [item[:4] for item in suministro]
    
    # any Compruebe si alguno de los elementos de una lista es Verdadero: 

    if any(num1 == num2 for num1 in suministro for num2 in numeros):
        return 'Si coincide'

    elif any(num1 == num2 for num1 in CoincidenciasListaNumeros for num2 in CoincidenciasListaSuministro):
        return 'Sin rotulado o deteriorado'
    else:
        return 'No coincide'

def edtElectrIniCMedicion(FotoElectrizamiento = None):
    Generar = random.randint(0,10)
    return Generar

