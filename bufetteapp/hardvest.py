import os                                               # Libreria de pytyon parar ejecutar comandos del sistema operativo
import django                                           # Importo el paquete de django
from dotenv import load_dotenv, find_dotenv             # Importo las variables de entorno

load_dotenv(find_dotenv())                              # Ejecuto las variables de entorno            
os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings"   # Indico donde se ejecuta settings.py
django.setup()                                          # Inicialice django

# Importamos las semillas:
from seeds.seeddata import TipotelefonoIngestion

def execute_seed():
    semilla = TipotelefonoIngestion() 

    if semilla.should_run():
        semilla.run()

execute_seed()