# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 14: UNPACKING (DESEMPAQUETADO)
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

        if len(self.datos) < 2:
            print("❌ Se necesitan al menos 2 elementos para el unpacking.")
            return

        primera, *mitad, ultima = self.datos
        print(f"🥇 Primera posición (primera): {primera}")
        print(f"🧱 Segmento medio (*mitad)   : {list(mitad)}")
        print(f"🏁 Última posición (ultima)  : {ultima}")
        print("\n💡 El operador * captura todos los elementos intermedios en una lista.")


class GestorDesempaquetado:
    @staticmethod
    def ejecutar_demostracion(tupla_entrada: tuple):
        DesempaquetadorEstructural(tupla_entrada).ejecutar_extraccion()


# ---------------------------------------------------------------------
# EJERCICIO 2: Usa *lista para pasar [2, 3, 4] a multiplicar(a, b, c).
# ---------------------------------------------------------------------
class OperadorMultiplicacion:
    def multiplicar(self, a: float, b: float, c: float):
        resultado = a * b * c
        print(f"  Argumentos posicionales → a={a}, b={b}, c={c}")
        print(f"  Resultado: {a} × {b} × {c} = {resultado}")
        return resultado


class GestorInyeccionArgumentos:
    @staticmethod
    def ejecutar_calculo(lista_factores: list):
        print("🧮 DESEMPAQUETADO EN FUNCIONES — *lista como argumentos")
        print("--------------------------------------------------")
        print(f"Lista original: {lista_factores}")
        print("Llamando multiplicar(*lista_factores):\n")
        calculador = OperadorMultiplicacion()
        calculador.multiplicar(*lista_factores)
        print("\n💡 El operador * desempaqueta la lista y la pasa como argumentos individuales.")


# ---------------------------------------------------------------------
# EJERCICIO 3: Combina dos diccionarios con ** sin modificar los originales.
# ---------------------------------------------------------------------
class FusionadorDiccionarios:
    def __init__(self, diccionario_a: dict, diccionario_b: dict):
        self.dict_a = diccionario_a
        self.dict_b = diccionario_b

    def mezclar_estructuras(self):
        print("🗺️ DESEMPAQUETADO DE DICTS — Fusión con **")
        print("--------------------------------------------------")
        print(f"Diccionario A (original): {self.dict_a}")
        print(f"Diccionario B (original): {self.dict_b}")

        diccionario_combinado = {**self.dict_a, **self.dict_b}

        print(f"\nResultado combinado : {diccionario_combinado}")
        print(f"\n🛡️ Verificación A después de combinar: {self.dict_a}  ← sin cambios")
        print(f"🛡️ Verificación B después de combinar: {self.dict_b}  ← sin cambios")
        print("\n💡 ** desempaqueta el diccionario en pares clave:valor dentro de la expresión literal.")


class GestorFusionMapas:
    @staticmethod
    def ejecutar_analisis(mapa_uno: dict, mapa_dos: dict):
        FusionadorDiccionarios(mapa_uno, mapa_dos).mezclar_estructuras()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(tupla_valores):
    GestorDesempaquetado.ejecutar_demostracion(tupla_valores)

def ejecutar_ejercicio2(lista_valores):
    GestorInyeccionArgumentos.ejecutar_calculo(lista_valores)

def ejecutar_ejercicio3(mapa_uno, mapa_dos):
    GestorFusionMapas.ejecutar_analisis(mapa_uno, mapa_dos)
