# =====================================================================
# BLOQUE 09: TUPLAS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Inmutabilidad — intentar modificar una tupla lanza TypeError.
# ---------------------------------------------------------------------
class DemostradorInmutabilidad:
    def __init__(self, tupla: tuple):
        self.tupla = tupla

    def intentar_mutacion(self):
        print("🔒 TUPLAS — Inmutabilidad")
        print("--------------------------------------------------")
        print(f"Tupla original: {self.tupla}")
        print("Intentando modificar el índice 0...")
        try:
            self.tupla[0] = 10
        except TypeError as e:
            print(f"\n❌ TypeError capturado:")
            print(f"   {e}")
            print("\n💡 Las tuplas son inmutables: no se pueden modificar tras crearse.")


class GestorInmutabilidad:
    @staticmethod
    def ejecutar_demostracion(tupla: tuple):
        DemostradorInmutabilidad(tupla).intentar_mutacion()


# ---------------------------------------------------------------------
# EJERCICIO 2: Unpacking con * — a, b, *resto = tupla.
# ---------------------------------------------------------------------
class DesempaquetadorTupla:
    def __init__(self, tupla: tuple):
        self.tupla = tupla

    def desempaquetar(self):
        print("📦 TUPLAS — Unpacking con *")
        print("--------------------------------------------------")
        print(f"Tupla de origen: {self.tupla}")

        if len(self.tupla) < 2:
            print("❌ Se necesitan al menos 2 elementos para el unpacking.")
            return

        a, b, *resto = self.tupla
        print(f"➡️ a     = {a}")
        print(f"➡️ b     = {b}")
        print(f"➡️ resto = {list(resto)}")


class GestorDesempaquetado:
    @staticmethod
    def ejecutar_calculo(tupla: tuple):
        DesempaquetadorTupla(tupla).desempaquetar()


# ---------------------------------------------------------------------
# EJERCICIO 3: Recorrer lista de coordenadas (tuplas) con unpacking en for.
# ---------------------------------------------------------------------
class RecorredorCoordenadas:
    def __init__(self, coordenadas: list):
        self.coordenadas = coordenadas

    def recorrer(self):
        print("🗺️ TUPLAS — Coordenadas con unpacking en for")
        print("--------------------------------------------------")
        print(f"Lista de coordenadas: {self.coordenadas}\n")
        for x, y in self.coordenadas:
            print(f"  x={x}, y={y}")


class GestorCoordenadas:
    @staticmethod
    def ejecutar_analisis(coordenadas: list):
        RecorredorCoordenadas(coordenadas).recorrer()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(tupla):
    GestorInmutabilidad.ejecutar_demostracion(tupla)

def ejecutar_ejercicio2(tupla):
    GestorDesempaquetado.ejecutar_calculo(tupla)

def ejecutar_ejercicio3(coordenadas):
    GestorCoordenadas.ejecutar_analisis(coordenadas)