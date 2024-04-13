import json
from  registration.models import TipoTelefono

# Clases para la ingesta de datos:
class TipotelefonoIngestion:
    """Clase para ingesta de datos de tipo de telefono"""
    
    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/tipotele.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return TipoTelefono.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            tipotele_model = TipoTelefono(nombre_tipo = item['nombre_tipo'])
            tipotele_model.save()

    
