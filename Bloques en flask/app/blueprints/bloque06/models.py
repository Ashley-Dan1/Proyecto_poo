# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 6: BUCLES (for / while)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Imprime los números del 1 al 10 con while.
# ---------------------------------------------------------------------
class ContadorWhile:
    def __init__(self, limite: int):
        self.limite = limite

    def contar(self):
        print(f"🔄 BUCLE WHILE — Números del 1 al {self.limite}")
        print("--------------------------------------------------")
        contador = 1
        while contador <= self.limite:
            print(f"  {contador}")
            contador += 1
        print(f"\n✅ Bucle finalizado. Se ejecutó {self.limite} vez/veces.")


class GestorContadorWhile:
    @staticmethod
    def ejecutar_demostracion(limite: int):
        ContadorWhile(limite).contar()


# ---------------------------------------------------------------------
# EJERCICIO 2: Recorre lista de frutas con enumerate() → índice y nombre.
# ---------------------------------------------------------------------
class RecorredorFrutas:
    def __init__(self, frutas: list):
        self.frutas = frutas

    def recorrer_con_enumerate(self):
        print("🍎 BUCLE FOR CON enumerate()")
        print("--------------------------------------------------")
        print(f"Lista: {self.frutas}\n")
        for indice, fruta in enumerate(self.frutas):
            print(f"  [{indice}] → {fruta}")
        print("\n💡 enumerate() devuelve pares (índice, elemento) en cada iteración.")


class GestorFrutas:
    @staticmethod
    def ejecutar_demostracion(lista_frutas: list):
        RecorredorFrutas(lista_frutas).recorrer_con_enumerate()


# ---------------------------------------------------------------------
# EJERCICIO 3: Cuadrados de pares del 1 al N con list comprehension.
# ---------------------------------------------------------------------
class GeneradorCuadradosPares:
    def __init__(self, limite: int):
        self.limite = limite

    def generar(self):
        print(f"⚡ LIST COMPREHENSION — Cuadrados de pares del 1 al {self.limite}")
        print("--------------------------------------------------")
        cuadrados = [x**2 for x in range(1, self.limite + 1) if x % 2 == 0]
        print(f"  Expresión : [x**2 for x in range(1, {self.limite + 1}) if x % 2 == 0]")
        print(f"  Resultado : {cuadrados}")
        print("\n💡 La cláusula 'if' dentro de la comprensión filtra solo los pares.")


class GestorCuadradosPares:
    @staticmethod
    def ejecutar_demostracion(limite: int):
        GeneradorCuadradosPares(limite).generar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(limite):
    GestorContadorWhile.ejecutar_demostracion(limite)

def ejecutar_ejercicio2(lista_frutas):
    GestorFrutas.ejecutar_demostracion(lista_frutas)

def ejecutar_ejercicio3(limite):
    GestorCuadradosPares.ejecutar_demostracion(limite)


def ejecutar_ejercicio2(inicio):
    GestorContadorWhile.ejecutar_calculo(inicio)

def ejecutar_ejercicio3(limite):
    GestorSumadorPares.ejecutar_analisis(limite)
