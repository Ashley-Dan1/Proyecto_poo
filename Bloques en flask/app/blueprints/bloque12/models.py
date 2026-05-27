# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 15: FUNCIONES DE ORDEN SUPERIOR
# =====================================================================
from functools import reduce

# ---------------------------------------------------------------------
# EJERCICIO 1: map() para incrementar en 1 cada elemento.
# ---------------------------------------------------------------------
class TransformadorMap:
    def __init__(self, numeros: list):
        self.numeros = numeros

    def incrementar(self):
        print("🗺️  FUNCIONES DE ORDEN SUPERIOR — map()")
        print("--------------------------------------------------")
        print(f"  Lista original  : {self.numeros}")
        resultado = list(map(lambda x: x + 1, self.numeros))
        print(f"  lambda x: x + 1")
        print(f"\n  Resultado       : {resultado}")
        print("\n💡 map() aplica la función a CADA elemento y devuelve un iterador.")


class GestorMap:
    @staticmethod
    def ejecutar_demostracion(lista: list):
        TransformadorMap(lista).incrementar()


# ---------------------------------------------------------------------
# EJERCICIO 2: filter() para obtener elementos mayores a umbral.
# ---------------------------------------------------------------------
class FiltradorFilter:
    def __init__(self, numeros: list):
        self.numeros = numeros

    def filtrar_mayores(self, umbral: float):
        print(f"🔍 FUNCIONES DE ORDEN SUPERIOR — filter() (umbral: {umbral})")
        print("--------------------------------------------------")
        print(f"  Lista original  : {self.numeros}")
        resultado = list(filter(lambda x: x > umbral, self.numeros))
        print(f"  lambda x: x > {umbral}")
        print(f"\n  Resultado       : {resultado}")
        print("\n💡 filter() conserva solo los elementos donde la función retorna True.")


class GestorFilter:
    @staticmethod
    def ejecutar_demostracion(lista: list, umbral: float):
        FiltradorFilter(lista).filtrar_mayores(umbral)


# ---------------------------------------------------------------------
# EJERCICIO 3: reduce() para multiplicar todos los elementos.
# ---------------------------------------------------------------------
class ReductorReduce:
    def __init__(self, numeros: list):
        self.numeros = numeros

    def multiplicar(self):
        print("➡️  FUNCIONES DE ORDEN SUPERIOR — reduce()")
        print("--------------------------------------------------")
        print(f"  Lista original  : {self.numeros}")
        if not self.numeros:
            print("  ⚠️  Lista vacía, no se puede reducir.")
            return
        resultado = reduce(lambda x, y: x * y, self.numeros)
        # Traza visual del proceso acumulativo
        pasos = " × ".join(str(int(n) if n == int(n) else n) for n in self.numeros)
        print(f"  lambda x, y: x * y")
        print(f"  Proceso         : {pasos} = {resultado}")
        print(f"\n  Resultado       : {resultado}")
        print("\n💡 reduce() aplica la función de forma acumulada de izquierda a derecha.")


class GestorReduce:
    @staticmethod
    def ejecutar_demostracion(lista: list):
        ReductorReduce(lista).multiplicar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(lista):
    GestorMap.ejecutar_demostracion(lista)

def ejecutar_ejercicio2(lista, umbral):
    GestorFilter.ejecutar_demostracion(lista, umbral)

def ejecutar_ejercicio3(lista):
    GestorReduce.ejecutar_demostracion(lista)
