# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 7: FUNCIONES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Función que calcule el doble de un número.
# ---------------------------------------------------------------------
class CalculadorDoble:
    def __init__(self, valor: float):
        self.valor = valor

    def calcular(self):
        resultado = self.valor * 2
        print("🔢 FUNCIÓN — doble(x)")
        print("--------------------------------------------------")
        print(f"  def doble(x): return x * 2")
        print(f"\n  doble({self.valor}) → {resultado}")


class GestorDoble:
    @staticmethod
    def ejecutar_demostracion(numero: float):
        CalculadorDoble(numero).calcular()


# ---------------------------------------------------------------------
# EJERCICIO 2: Función que sume con *args.
# ---------------------------------------------------------------------
class SumadorArgs:
    def __init__(self, numeros: list):
        self.numeros = numeros

    def sumar(self):
        total = sum(self.numeros)
        print("🧮 FUNCIÓN CON *args — sumar_varios(*numeros)")
        print("--------------------------------------------------")
        print(f"  Argumentos recibidos : {tuple(self.numeros)}")
        print(f"  Proceso              : {' + '.join(str(n) for n in self.numeros)} = {total}")
        print(f"\n  Resultado            : {total}")
        print("\n💡 *args empaqueta todos los argumentos posicionales en una tupla.")


class GestorSumadorArgs:
    @staticmethod
    def ejecutar_demostracion(lista: list):
        SumadorArgs(lista).sumar()


# ---------------------------------------------------------------------
# EJERCICIO 3: Factorial recursivo.
# ---------------------------------------------------------------------
class CalculadorFactorial:
    def __init__(self, n: int):
        self.n = n

    def factorial(self, n: int) -> int:
        if n == 0:
            return 1                    # caso base
        return n * self.factorial(n - 1)  # llamada recursiva

    def mostrar(self):
        print("🧬 RECURSIVIDAD — factorial(n)")
        print("--------------------------------------------------")
        if self.n < 0:
            print("❌ El factorial no está definido para números negativos.")
            return
        resultado = self.factorial(self.n)
        # Traza visual del proceso
        pasos = " × ".join(str(i) for i in range(self.n, 0, -1)) + " × 1"
        print(f"  factorial({self.n}) = {pasos}")
        print(f"\n  Resultado : {resultado}")
        print("\n💡 Caso base: factorial(0) = 1. Sin él el bucle sería infinito.")


class GestorFactorial:
    @staticmethod
    def ejecutar_demostracion(n: int):
        CalculadorFactorial(n).mostrar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(numero):
    GestorDoble.ejecutar_demostracion(numero)

def ejecutar_ejercicio2(lista):
    GestorSumadorArgs.ejecutar_demostracion(lista)

def ejecutar_ejercicio3(n):
    GestorFactorial.ejecutar_demostracion(n)

def ejecutar_ejercicio3(lista, fruta_eliminar):
    GestorDepuracion.ejecutar_analisis(lista, fruta_eliminar)
