import os                                               # Libreria de pytyon parar ejecutar comandos del sistema operativo
import django                                           # Importo el paquete de django
from dotenv import load_dotenv, find_dotenv             # Importo las variables de entorno

load_dotenv(find_dotenv())                              # Ejecuto las variables de entorno            
os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings"   # Indico donde se ejecuta settings.py
django.setup()                                          # Inicialice django

# Importamos las semillas:
from seeds.seeddata import TipotelefonoIngestion,GeneroIngestion,EtniasIngestion,TipoDocumentoIngestion,EstadoCivilIngestion,VulnerabilidadsIngestion, DespachoIngestion
from seeds.datadepto import DepartamentoSeed

def execute_seed():
    semilla_tipoTele = TipotelefonoIngestion() 
    semilla_genero = GeneroIngestion()
    semilla_etnias = EtniasIngestion()
    semilla_tipoDocu = TipoDocumentoIngestion()
    semila_estadoCivil = EstadoCivilIngestion()
    semilla_vulnerabilidad = VulnerabilidadsIngestion()
    semilla_despacho = DespachoIngestion()
    departamento_seed = DepartamentoSeed()

    if semilla_tipoTele.should_run():
        semilla_tipoTele.run()

    if semilla_genero.should_run():
        semilla_genero.run()
    
    if semilla_etnias.should_run():
        semilla_etnias.run()

    if semilla_tipoDocu.should_run():
        semilla_tipoDocu.run()

    if semila_estadoCivil.should_run():
        semila_estadoCivil.run()

    if semilla_vulnerabilidad.should_run():
        semilla_vulnerabilidad.run()

    if semilla_despacho.should_run():
        semilla_despacho.run()
    
    if departamento_seed.should_run():
        departamento_seed.run()

execute_seed()