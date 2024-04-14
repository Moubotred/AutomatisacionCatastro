
# from RedNeuronalSimple import ModeloNeuronal

class OpcionesAntes:
    
    # Se puede realizar?
    # si son 6 fotos si | condicion

    def EsPosibleRealizarCatastro(self,**kwargs):
        if kwargs.get('numero') < '6' or kwargs.get('numero') == '6':
            return 'Si'
        
        if kwargs.get('numero') >= '4':
            return 'Inspección parcial'

    # Bateria / Individual 
    # solo si hay foto en el primer los suministro
    # se considera bateria de lo contrario 
    # es individual  | red neuronal
        
    def TipoDeSuministro(self):
        pass
        # Respuesta = ModeloNeuronal('IdentificacionSuministro','ConjuntosSuministro','imagen001.jpg')
        # return Respuesta
        



# Tipo de medidor
# electronico/electromecanico | red neuronal

# Tipo de conexion
# si es aerea tomar foto al poste de lo 
# contrario se asumira que es subterranea
# |condicion

# Tipo de superficie
# tierra color marron diferentes tonos superficies
# plantas verdes ,concretos irregularidades 
# nose puede indentidicar todavia 

# Ubicacion de conexion
# tomar foto alas rejas si es interno 
# de lo contrario de asumira que es externo 
# | solo primer suministro
# | condicion

# Rotulado 
# se usar el script de GoogleEyes.py para reconoser 
# si existe el numero de suminstro y habra una condicion 
# si existe digitos superiores a 4 digitos < de lo contrario
# se seleccionar opcion de sin rotular o deteriorado  
# | condcion | script

# Electrizamiento
# poner manualmente electrizamiento

# Tapa de caja de medicion
# entrenar una red que reconosca cpv 
# sino recococe la tapa como cpv, 
# seleccionar corresponde al tipo de tapa 
# | condicion | red neuronal

# Estado de Tapa de c. Medidcion
# podria entrenar una red neuronal
# para que indetifique las partes rotas
# de una tapa 

# tapa caja de medicion
# nose puede entrenar la red porque las dimesiones nunca 
# sernan iguales y no tengo forma de entrenarla todavia

# tapa caja de medicion
# nose puede entrenar la red porque las dimesiones nunca 
# seran iguales y no tengo forma de entrenarla todavia

# Estado caja de medicion
# *pendiente

# Altura de caja
# generar de manera eleatoria

# Ancho de la caja
# depende de la tapa

# Profundidad de la caja
# depende de la tapa

# Chaqueta Plomo
# *pendiente

# ubicacion de caja
# por defecto fachada

# Medidor
# *Pendiente

# N Fases
# red neuronal se puede identificar con los 
# tipos de medidores y las fases

# Conexion Acometida con medidor
# por defecto al sistema proteccion

# Estado Tubo corrugado
# *Pendiente

# Tipo de proteccion C.medicion
# uso de red neuronal para poder identiifcar
# el tipo de sistema de proteccion

# Estado de sistema de proteccion
# por defecto bueno

# Capacidad de ITM C.medicion
# depende de la potencia
# y una tabla de potencia

# Tipo de acometida
# * Pendiente

# Estado de Acometida
# *Pendiente

# Electrizamiento
# *Pendiente

# Densidad del publico
# por defecto baja

# El predio corresponde
# por defecto vivienda

# Tareas ejecutaadas
# *basico