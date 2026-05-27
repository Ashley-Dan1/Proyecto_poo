# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 2: VARIABLES Y TIPOS DE DATOS
# =====================================================================
from typing import List, Tuple, Dict, Set, Any

# ---------------------------------------------------------------------
# EJERCICIO 1: Declarar una variable de cada tipo simple y complejo.
# ---------------------------------------------------------------------
class DemostradorTipos:
    def __init__(self):
        # Tipos simples
        self.entero: int       = 19
        self.flotante: float   = 3.14
        self.cadena: str       = "Hello World"
        self.booleano: bool    = True
        self.nulo              = None
        # Tipos complejos
        self.lista: List[Any]          = [1, 2, 3, "python"]
        self.tupla: Tuple              = (1, "hello", 3.14)
        self.diccionario: Dict[str, Any] = {"nombre": "Juan", "edad": 25}
        self.conjunto: Set[int]        = {1, 2, 3, 4, 5}

    def mostrar_todos(self):
        print("🔢 TIPOS SIMPLES")
        print("--------------------------------------------------")
        print(f"  int   → {self.entero}   | tipo: {type(self.entero).__name__}")
        print(f"  float → {self.flotante}  | tipo: {type(self.flotante).__name__}")
        print(f"  str   → '{self.cadena}'  | tipo: {type(self.cadena).__name__}")
        print(f"  bool  → {self.booleano}  | tipo: {type(self.booleano).__name__}")
        print(f"  None  → {self.nulo}      | tipo: {type(self.nulo).__name__}")
        print("\n📦 TIPOS COMPLEJOS")
        print("--------------------------------------------------")
        print(f"  list  → {self.lista}")
        print(f"  tuple → {self.tupla}")
        print(f"  dict  → {self.diccionario}")
        print(f"  set   → {self.conjunto}")


class GestorTiposSimples:
    @staticmethod
    def ejecutar_demostracion():
        demo = DemostradorTipos()
        demo.mostrar_todos()


# ---------------------------------------------------------------------
# EJERCICIO 2: Lista con 5 elementos → primero, último, lista[1:4].
# ---------------------------------------------------------------------
class InspectorLista:
    def __init__(self, elementos: list):
        self.lista = elementos

    def mostrar_accesos(self):
        print("📋 ACCESO POR ÍNDICE Y SLICING")
        print("--------------------------------------------------")
        print(f"Lista completa : {self.lista}")
        print(f"Primero [0]    : {self.lista[0]}")
        print(f"Último  [-1]   : {self.lista[-1]}")
        print(f"Slice [1:4]    : {self.lista[1:4]}")
        print("\n💡 Slicing [inicio:fin] — incluye inicio, NO incluye fin.")


class GestorInspectorLista:
    @staticmethod
    def ejecutar_demostracion(lista: list):
        inspector = InspectorLista(lista)
        inspector.mostrar_accesos()


# ---------------------------------------------------------------------
# EJERCICIO 3: Clase con str, list y dict → primer carácter, último
#              elemento, valor de una clave.
# ---------------------------------------------------------------------
class DemoTiposEnMetodo:
    def mostrar(self):
        texto      = "Python"
        lista      = [10, 20, 30]
        datos      = {"curso": "POO"}

        print("🧱 TIPOS DENTRO DE UN MÉTODO DE CLASE")
        print("--------------------------------------------------")
        print(f"  str   → '{texto}'  | primer carácter : '{texto[0]}'")
        print(f"  list  → {lista}  | último elemento : {lista[-1]}")
        print(f"  dict  → {datos} | valor de 'curso': '{datos['curso']}'")


class GestorDemoTipos:
    @staticmethod
    def ejecutar_demostracion():
        demo = DemoTiposEnMetodo()
        demo.mostrar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1():
    GestorTiposSimples.ejecutar_demostracion()

def ejecutar_ejercicio2(lista):
    GestorInspectorLista.ejecutar_demostracion(lista)

def ejecutar_ejercicio3():
    GestorDemoTipos.ejecutar_demostracion()
