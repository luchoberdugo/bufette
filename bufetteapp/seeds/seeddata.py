import json
from registration.models import TipoTelefono, Genero, TipoDocumento, Etnias, EstadoCivil, Vulnerabilidades
from despachos.models import TipoDespacho, Despacho

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

    
class GeneroIngestion:

    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/generos.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return Genero.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            genero_model = Genero(nombre_genero = item['nombre_genero'])
            genero_model.save()

class EtniasIngestion:

    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/etnias.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return Etnias.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            etnias_model = Etnias(nombre_etnia = item['nombre_etnia'])
            etnias_model.save()

class TipoDocumentoIngestion:

    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/tipodocu.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return TipoDocumento.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            tipodocu_model = TipoDocumento(nombre_documento = item['nombre_documento'])
            tipodocu_model.save()

class EstadoCivilIngestion:

    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/estacivil.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return EstadoCivil.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            estadocivil_model = EstadoCivil(estado_civil = item['estado_civil'])
            estadocivil_model.save()

class VulnerabilidadsIngestion:

    def __init__(self) ->None:
        """Constructor, se encarga de leer un archivos y procesarlo en una variable y
           luego Operamos sobre una instancia de la misma clase."""
        with open('seeds/fixtures/vulnerabilidades.json', encoding = 'utf8') as data:
            self.datos = json.load(data)

    def should_run(self):
        """Este métod espera que hayan 0 registros en la bd"""
        return Vulnerabilidades.objects.count() == 0
    
    def run(self):
        """Método para recorrer el json y guardar cada uno de los items en la bd"""
        for item in self.datos:
            vulnerabilidad_model = Vulnerabilidades(nombre_vulnerabilidad = item['nombre_vulnerabilidad'])
            vulnerabilidad_model.save()

# Clases para las adiciones de semillas de Jhonathan:

class DespachoIngestion:
    def __init__(self) -> None:
        with open('seeds/fixtures/despacho.json', encoding = 'utf8') as despacho_data:
            self.despachos = json.load(despacho_data)

    def should_run(self):
        return Despacho.objects.count() == 0
    
    def run(self):
        for despacho in self.despachos:
            tipo_despacho_model = TipoDespacho(nombre_tipo_despacho = despacho['tipo_despacho'])
            tipo_despacho_model.save()

            for item in despacho["nombre_despacho"]:
                despacho_model = Despacho(tipo_despacho = tipo_despacho_model, nombre_despacho = item)
                despacho_model.save()
            
