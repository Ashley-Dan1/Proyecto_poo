# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 15: LIST COMPREHENSIONS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crea una lista con los cuadrados de los números del 1 al 5 usando List Comprehension.
# ---------------------------------------------------------------------
class GeneradorCuadradosComprimido:
    def __init__(self, limite_maximo: int):
        self.limite = limite_maximo

    def generar_lista_cuadrados(self):
        print(f"⚡ GENERACIÓN DE CUADRADOS (1 AL {self.limite})")
        print("--------------------------------------------------")
        
        # Sintaxis de List Comprehension pura: [expresión for elemento in iterable]
        lista_cuadrados = [numero ** 2 for numero in range(1, self.limite + 1)]
        
        print(f"➡️ Lista resultante generada de forma compacta: {lista_cuadrados}")
        return lista_cuadrados


class GestorCuadradosComprension:
    @staticmethod
    def ejecutar_demostracion(limite: int):
        generador = GeneradorCuadradosComprimido(limite)
        generador.generar_lista_cuadrados()


# ---------------------------------------------------------------------
# EJERCICIO 2: Filtra una lista de números para obtener solo los pares usando List Comprehension.
# ---------------------------------------------------------------------
class FiltroParesComprimido:
    def __init__(self, lista_origen: list):
        self.datos = lista_origen

    def extraer_solo_pares(self):
        print("🔍 FILTRADO COMPACTO DE ELEMENTOS PARES")
        print("--------------------------------------------------")
        print(f"Lista de entrada provista: {self.datos}")
        
        # List Comprehension con condicional integrado: [expresión for elemento in iterable if condición]
        lista_pares = [elemento for elemento in self.datos if elemento % 2 == 0]
        
        print(f"➡️ Lista filtrada resultante: {lista_pares}")
        return lista_pares


class GestorFiltroPares:
    @staticmethod
    def ejecutar_calculo(lista_numeros: list):
        filtrador = FiltroParesComprimido(lista_numeros)
        filtrador.extraer_solo_pares()


# ---------------------------------------------------------------------
# EJERCICIO 3: Crea una lista que contenga las palabras en mayúsculas de otra lista.
# ---------------------------------------------------------------------
class ConvertidorTextoComprimido:
    def __init__(self, lista_palabras: list):
        self.palabras = lista_palabras

    def transformar_a_mayusculas(self):
        print("🔠 TRANSICIÓN DE TEXTO A MAYÚSCULAS")
        print("--------------------------------------------------")
        print(f"Palabras de entrada: {self.palabras}")
        
        # Aplicación del método de cadena .upper() dentro de la comprensión
        lista_mayusculas = [palabra.upper() for palabra in self.palabras]
        
        print(f"➡️ Lista de palabras normalizadas: {lista_mayusculas}")
        return lista_mayusculas


class GestorMayusculasComprension:
    @staticmethod
    def ejecutar_analisis(lista_cadenas: list):
        convertidor = ConvertidorTextoComprimido(lista_cadenas)
        convertidor.transformar_a_mayusculas()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(limite):
    GestorCuadradosComprension.ejecutar_demostracion(limite)

def ejecutar_ejercicio2(lista_numeros):
    GestorFiltroPares.ejecutar_calculo(lista_numeros)

def ejecutar_ejercicio3(lista_palabras):
    GestorMayusculasComprension.ejecutar_analisis(lista_palabras)