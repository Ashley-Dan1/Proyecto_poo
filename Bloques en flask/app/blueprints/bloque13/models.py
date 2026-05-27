# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 13: UNPACKING (DESEMPAQUETADO)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Desempaqueta (10, 20, 30, 40) → primera, *mitad, ultima.
# ---------------------------------------------------------------------
class DesempaquetadorEstructural:
    def __init__(self, tupla_datos: tuple):
        self.datos = tupla_datos

    def ejecutar_extraccion(self):
        print("📦 DESEMPAQUETADO CON OPERADOR COMODÍN (*)")
        print("--------------------------------------------------")
        print(f"Tupla de origen: {self.datos}")
        
        # Desempaquetado dinámico usando el operador asterisco
        primera, *mitad, ultima = self.datos
        
        print(f"🥇 Primera posición: {primera}")
        print(f"🧱 Segmento medio (*mitad): {mitad}")
        print(f"🏁 Última posición: {ultima}")


class GestorDesempaquetado:
    @staticmethod
    def ejecutar_demostracion(tupla_entrada: tuple):
        procesador = DesempaquetadorEstructural(tupla_entrada)
        procesador.ejecutar_extraccion()


# ---------------------------------------------------------------------
# EJERCICIO 2: Usa *lista para pasar [2,3,4] como argumentos a multiplicar(a,b,c).
# ---------------------------------------------------------------------
class OperadorMultiplicacion:
    def __init__(self):
        pass

    def multiplicar(self, a: float, b: float, c: float):
        # Método núcleo que requiere tres parámetros independientes
        resultado = a * b * c
        print(f"🔢 Argumentos posicionales recibidos -> a: {a}, b: {b}, c: {c}")
        print(f"➡️ Resultado de la multiplicación: {resultado}")
        return resultado


class GestorInyeccionArgumentos:
    @staticmethod
    def ejecutar_calculo(lista_factores: list):
        print("🧮 INYECCIÓN DE ARGUMENTOS MEDIANTE DESEMPAQUETADO DE LISTA")
        print("--------------------------------------------------")
        print(f"Lista original enviada: {lista_factores}")
        
        calculador = OperadorMultiplicacion()
        # Desempaquetamos la lista utilizando el operador '*' al vuelo en los parámetros
        calculador.multiplicar(*lista_factores)


# ---------------------------------------------------------------------
# EJERCICIO 3: Combina dos diccionarios usando ** sin sobrescribir el original.
# ---------------------------------------------------------------------
class FusionadorDiccionarios:
    def __init__(self, diccionario_a: dict, diccionario_b: dict):
        self.dict_a = diccionario_a
        self.dict_b = diccionario_b

    def mezclar_estructuras(self):
        print("🗺️ FUSIÓN INMUTABLE DE DICCIONARIOS CON **")
        print("--------------------------------------------------")
        print(f"Diccionario A (Original): {self.dict_a}")
        print(f"Diccionario B (Original): {self.dict_b}")
        
        # Combinación limpia usando doble asterisco en una nueva expresión literal
        diccionario_combinado = {**self.dict_a, **self.dict_b}
        
        print(f"🔄 Mapa unificado resultante: {diccionario_combinado}")
        print(f"🛡️ Verificación de integridad A: {self.dict_a} (Sin alteraciones)")


class GestorFusionMapas:
    @staticmethod
    def ejecutar_analisis(mapa_uno: dict, mapa_dos: dict):
        fusionador = FusionadorDiccionarios(mapa_uno, mapa_dos)
        fusionador.mezclar_estructuras()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(tupla_valores):
    GestorDesempaquetado.ejecutar_demostracion(tupla_valores)

def ejecutar_ejercicio2(lista_valores):
    GestorInyeccionArgumentos.ejecutar_calculo(lista_valores)

def ejecutar_ejercicio3(mapa_uno, mapa_dos):
    GestorFusionMapas.ejecutar_analisis(mapa_uno, mapa_dos)