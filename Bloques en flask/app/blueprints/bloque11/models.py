# =====================================================================
# BLOQUE 11: CONJUNTOS (set)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Unión, intersección y diferencia entre dos conjuntos.
# ---------------------------------------------------------------------
class OperadorConjuntos:
    def __init__(self, set_a: set, set_b: set):
        self.A = set_a
        self.B = set_b

    def operar(self):
        print("🔢 CONJUNTOS — Operaciones matemáticas")
        print("--------------------------------------------------")
        print(f"A = {self.A}")
        print(f"B = {self.B}\n")
        print(f"➡️ Unión         (A | B) = {self.A | self.B}")
        print(f"➡️ Intersección  (A & B) = {self.A & self.B}")
        print(f"➡️ Diferencia    (A - B) = {self.A - self.B}")


class GestorOperaciones:
    @staticmethod
    def ejecutar_demostracion(set_a: set, set_b: set):
        OperadorConjuntos(set_a, set_b).operar()


# ---------------------------------------------------------------------
# EJERCICIO 2: Eliminar duplicados de una lista usando set.
# ---------------------------------------------------------------------
class EliminadorDuplicados:
    def __init__(self, lista: list):
        self.lista = lista

    def eliminar(self):
        print("🧹 CONJUNTOS — Eliminar duplicados")
        print("--------------------------------------------------")
        print(f"Lista original : {self.lista}")
        sin_duplicados = list(set(self.lista))
        sin_duplicados.sort()
        print(f"➡️ Sin duplicados: {sin_duplicados}")
        print(f"\n💡 set() elimina repetidos automáticamente; list() lo convierte de vuelta.")


class GestorDuplicados:
    @staticmethod
    def ejecutar_calculo(lista: list):
        EliminadorDuplicados(lista).eliminar()


# ---------------------------------------------------------------------
# EJERCICIO 3: (A | B) - (A & B) == diferencia simétrica A ^ B.
# ---------------------------------------------------------------------
class AnalizadorSimetrico:
    def __init__(self, set_a: set, set_b: set):
        self.A = set_a
        self.B = set_b

    def analizar(self):
        print("🔀 CONJUNTOS — Diferencia simétrica")
        print("--------------------------------------------------")
        print(f"A = {self.A}")
        print(f"B = {self.B}\n")
        manual  = (self.A | self.B) - (self.A & self.B)
        simbolo = self.A ^ self.B
        print(f"➡️ (A | B) - (A & B) = {manual}")
        print(f"➡️ A ^ B             = {simbolo}")
        print(f"\n✅ ¿Son iguales? {manual == simbolo}")
        print("💡 Ambas expresiones representan la diferencia simétrica:")
        print("   elementos que pertenecen a uno u otro conjunto, pero no a ambos.")


class GestorSimetrico:
    @staticmethod
    def ejecutar_analisis(set_a: set, set_b: set):
        AnalizadorSimetrico(set_a, set_b).analizar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(set_a, set_b):
    GestorOperaciones.ejecutar_demostracion(set_a, set_b)

def ejecutar_ejercicio2(lista):
    GestorDuplicados.ejecutar_calculo(lista)

def ejecutar_ejercicio3(set_a, set_b):
    GestorSimetrico.ejecutar_analisis(set_a, set_b)