from RedNeuronalSimple import ModeloNeuronal
import os

# C:\Users\nimun\Documents\scripts\examples\opencv\__fotos_sad__

valor = len(os.listdir(os.path.join(os.getcwd(),'__fotos_sad__')))

Preguntas = [
            ('M','com.luzdelsur.bt.inspecciones.ui:id/spRealizarCatastro'), 

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTipoSuministro'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTecnologiaMedidor'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTipoConexion'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTipoSuperficie'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spUbicacionConexion'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spRotulado'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/edtElectrIniCMedicion','222222'),
            
            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTapaCajaMedicion'),
            
            ('M','com.luzdelsur.bt.inspecciones.ui:id/spEstadoTapaCajaMedicion'),
            ('M','com.luzdelsur.bt.inspecciones.ui:id/contentPanel'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spTipoCajaMedicion'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spEstadoCajaMedicion'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/edtAlturaCajaMedicion','222222') ,
            ('M','com.luzdelsur.bt.inspecciones.ui:id/edtAnchoCajaMedicion','222222'),
            ('M','com.luzdelsur.bt.inspecciones.ui:id/edtProfundidadCajaMedicion','222222'),

            ('M','com.luzdelsur.bt.inspecciones.ui:id/spChaquetaPlomo'),
            ]

Respuesta = [
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="$"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Individual"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Electrónico"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Subterránea"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Tierra"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Externo"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Si coincide"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Corresponde al tipo de caja"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="L"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Buen estado"]'),
            ('M','//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="No"]')
            ]

# Preguntas[0][1]
Modelo = 'Si' if valor >= 5  else 'No'
print(Respuesta[0][1].replace('$',Modelo))

# # crea un modelo de que indetifique si es una bateria o individual
Preguntas[2][1]
Modelo = ModeloNeuronal('spTipoSuministro','TipoSuministro','Suministro','Imagen_007.jpg')
print(Respuesta[2][1].replace(Modelo))

# # crea un modelo de que indetifique si es una electronico o electromecanico
Preguntas[2][1]
Modelo = ModeloNeuronal('spTecnologiaMedidor','TecnologiaMedidor','Suministro','Imagen_007.jpg')
print(Respuesta[2][1].replace(Modelo))

# # crea un modelo de que indetifique si es subterraneo o aereo
# Preguntas[3][1]
# Modelo = ModeloNeuronal('IdentificacionSuministro','ConjuntosSuministro','Suministro','Imagen_007.jpg')
# print(Respuesta[3][1].replace(Modelo))

# # valor por defecto Concreto
# Preguntas[4][1]
# Modelo = 'Concreto'
# print(Respuesta[4][1].replace(Modelo))

# # valor por defecto Externo
# Preguntas[5][1]
# Modelo = 'Externo'
# print(Respuesta[5][1].replace(Modelo))

# # valor por defecto Externo
# Preguntas[6][1]
# Modelo = 'si coincide'
# print(Respuesta[6][1].replace(Modelo))

# # valor por defecto Corresponde al tipo de caja
# Preguntas[7][1]
# Modelo = 'Corresponde al tipo de caja'
# print(Respuesta[7][1].replace(Modelo))

# # valor por defecto Buen estado
# Preguntas[8][1]
# Modelo = 'Buen estado'
# print(Respuesta[8][1].replace(Modelo))

# # valor por defecto L
# Preguntas[9][1]
# Modelo = 'L'
# print(Respuesta[9][1].replace(Modelo))

# # valor por defecto No
# Preguntas[10][1]

# Modelo = 'No'
# print(Respuesta[10][1].replace(Modelo))