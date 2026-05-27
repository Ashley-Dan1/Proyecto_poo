# =====================================================================
# BLOQUE 08: LISTAS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crear lista vacía, append x3, sort y mostrar.
# ---------------------------------------------------------------------
class ConstructorLista:
    def __init__(self, elementos: list):
        self.lista = list(elementos)

    def agregar_y_ordenar(self):
        print("📋 LISTAS — append() y sort()")
        print("--------------------------------------------------")
        print(f"Lista recibida: {self.lista}")
        self.lista.sort()
        print(f"➡️ Lista ordenada: {self.lista}")
        print(f"   Longitud: {len(self.lista)} elementos")


class GestorConstructorLista:
    @staticmethod
    def ejecutar_demostracion(elementos: list):
        ConstructorLista(elementos).agregar_y_ordenar()


# ---------------------------------------------------------------------
# EJERCICIO 2: sum(), max(), min() sobre una lista.
# ---------------------------------------------------------------------
class AnalizadorLista:
    def __init__(self, numeros: list):
        self.numeros = numeros

    def calcular_estadisticas(self):
        print("📊 LISTAS — sum(), max(), min()")
        print("--------------------------------------------------")
        print(f"Lista: {self.numeros}")
        print(f"➡️ Suma  : {sum(self.numeros)}")
        print(f"➡️ Máximo: {max(self.numeros)}")
        print(f"➡️ Mínimo: {min(self.numeros)}")


class GestorAnalizadorLista:
    @staticmethod
    def ejecutar_calculo(numeros: list):
        AnalizadorLista(numeros).calcular_estadisticas()


# ---------------------------------------------------------------------
# EJERCICIO 3: Referencia vs copia con .copy().
# ---------------------------------------------------------------------
class DemostradorCopiaLista:
    def __init__(self):
        self.lista_original = [1, 2, 3]

    def demostrar_diferencia(self):
        print("🔍 LISTAS — referencia vs copia (.copy())")
        print("--------------------------------------------------")
        lista        = self.lista_original[:]
        copia_ref    = lista
        copia_real   = lista.copy()

        print(f"lista original   : {lista}")
        print(f"copia_ref  = lista        → misma referencia en memoria")
        print(f"copia_real = lista.copy() → objeto nuevo independiente\n")

        copia_ref.append(4)
        print(f"Después de copia_ref.append(4):")
        print(f"  lista      : {lista}      ← también cambió")
        print(f"  copia_real : {copia_real}   ← no cambió")
        print("\n💡 Usa .copy() cuando necesites una lista independiente.")


class GestorCopiaLista:
    @staticmethod
    def ejecutar_analisis():
        DemostradorCopiaLista().demostrar_diferencia()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(lista):
    GestorConstructorLista.ejecutar_demostracion(lista)

def ejecutar_ejercicio2(lista):
    GestorAnalizadorLista.ejecutar_calculo(lista)

def ejecutar_ejercicio3():
    GestorCopiaLista.ejecutar_analisis()