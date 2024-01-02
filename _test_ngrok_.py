from multiprocessing.pool import ThreadPool
from pyngrok import ngrok
import subprocess
import os
import time

PUERTO = 9090

def servidor():
	subprocess.Popen(["python3", "-m", "http.server", f"{PUERTO}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
	print(f"Servidor HTTP escuchando en el puerto {PUERTO}")
    
def tunel():
    ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
    url_publica = ngrok.connect(PUERTO)
    print(f"URL pública: {url_publica}")


pool = ThreadPool(2)
pool.apply_async(servidor)
pool.apply_async(tunel)
time.sleep(20)

























