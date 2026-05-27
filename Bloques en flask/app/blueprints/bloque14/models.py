# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 14: FUNCIONES DE ORDEN SUPERIOR
# =====================================================================
from functools import reduce

# ---------------------------------------------------------------------
# EJERCICIO 1: Usa map() con una función lambda para elevar al cuadrado una lista.
# ---------------------------------------------------------------------
class TransformadorColecciones:
    def __init__(self, numeros_base: list):
        self.numeros = numeros_base

    def elevar_elementos_al_cuadrado(self):
        print("🧪 TRANSFORMACIÓN DE DATOS CON map() Y LAMBDA")
        print("--------------------------------------------------")
        print(f"Lista de entrada: {self.numeros}")
        
        # map() aplica la función anónima a cada elemento de la colección iterable
        resultado_iterador = map(lambda x: x ** 2, self.numeros)
        lista_final = list(resultado_iterador)
        
        print(f"➡️ Lista transformada al cuadrado: {lista_final}")
        return lista_final


class GestorTransformacion:
    @staticmethod
    def ejecutar_demostracion(lista_web: list):
        transformador = TransformadorColecciones(lista_web)
        transformador.elevar_elementos_al_cuadrado()


# ---------------------------------------------------------------------
# EJERCICIO 2: Usa filter() para obtener solo los números mayores a 10 de una lista.
# ---------------------------------------------------------------------
class FiltroColecciones:
    def __init__(self, numeros_base: list):
        self.numeros = numeros_base

    def filtrar_mayores_que_diez(self, umbral: float):
        print(f"🔍 FILTRADO DE ELEMENTOS CON filter() (Umbral: {umbral})")
        print("--------------------------------------------------")
        print(f"Lista de entrada: {self.numeros}")
        
        # filter() conserva únicamente los elementos donde la función lambda retorna True
        resultado_filtro = filter(lambda x: x > umbral, self.numeros)
        lista_filtrada = list(resultado_filtro)
        
        print(f"➡️ Elementos que superan el umbral: {lista_filtrada}")
        return lista_filtrada


class GestorFiltrado:
    @staticmethod
    def ejecutar_calculo(lista_base: list, valor_umbral: float):
        filtrador = FiltroColecciones(lista_base)
        filtrador.filtrar_mayores_que_diez(valor_umbral)


# ---------------------------------------------------------------------
# EJERCICIO 3: Usa reduce() para multiplicar todos los elementos de una lista.
# ---------------------------------------------------------------------
class ReductorColecciones:
    def __init__(self, numeros_base: list):
        self.numeros = numeros_base

    def calcular_producto_acumulado(self):
        print("🧮 REDUCCIÓN DE ESTRUCTURAS CON reduce()")
        print("--------------------------------------------------")
        print(f"Lista de entrada: {self.numeros}")
        
        if not self.numeros:
            print("⚠️ La lista está vacía. No se puede realizar la reducción acumulada.")
            return 0
            
        # reduce() aplica la función de dos argumentos de forma acumulativa de izquierda a derecha
        producto_total = reduce(lambda acumulador, elemento: acumulador * elemento, self.numeros)
        
        print(f"➡️ Producto acumulado final de todos los elementos: {producto_total}")
        return producto_total


class GestorReduccion:
    @staticmethod
    def ejecutar_analisis(lista_base: list):
        reductor = ReductorColecciones(lista_base)
        reductor.calcular_producto_acumulado()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(lista_numeros):
    GestorTransformacion.ejecutar_demostracion(lista_numeros)

def ejecutar_ejercicio2(lista_numeros, umbral):
    GestorFiltrado.ejecutar_calculo(lista_numeros, umbral)

def ejecutar_ejercicio3(lista_numeros):
    GestorReduccion.ejecutar_analisis(lista_numeros)