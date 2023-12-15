# Definición del decorador
def mi_decorador(base):
    def nueva_funcion():
        print("Antes de ejecutar la función original")
        base()
        print("Después de ejecutar la función original")
    return nueva_funcion

# Uso del decorador
@mi_decorador
def saludo():
    print("¡Hola, mundo!")

# Llamada a la función decorada
saludo()
