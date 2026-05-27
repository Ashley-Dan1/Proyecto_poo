# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 10: FUNCIONES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Función que calcule el doble de un número.
# ---------------------------------------------------------------------
class OperadorMatematico:
    def __init__(self, valor_base: float):
        self.valor = valor_base

    def calcular_doble(self):
        print("🔢 CÁLCULO DE VALOR DUPLICADO")
        print("--------------------------------------------------")
        # Implementación de la lógica básica solicitada
        resultado = self.valor * 2  # [cite: 331]
        print(f"El doble del número {self.valor} es: {resultado}")
        return resultado


class GestorDuplicador:
    @staticmethod
    def ejecutar_demostracion(numero: float):
        operador = OperadorMatematico(numero)
        operador.calcular_doble()


# ---------------------------------------------------------------------
# EJERCICIO 2: Función que sume todos los elementos de una lista con *args.
# ---------------------------------------------------------------------
class AgregadorDinamico:
    def __init__(self):
        # El constructor inicializa la estructura sin necesidad de estados rígidos
        pass

    def sumar_elementos(self, *numeros: float):  # [cite: 329]
        print("🧮 SUMATORIA DINÁMICA UTILIZANDO *ARGS")
        print("--------------------------------------------------")
        print(f"Argumentos posicionales recibidos (*args): {numeros}")
        
        # Se procesa la tupla dinámica generada por el empaquetamiento *args
        total_acumulado = sum(numeros)  # [cite: 329]
        
        print(f"➡️ Resultado final de la suma: {total_acumulado}")
        return total_acumulado


class GestorSumadorArgs:
    @staticmethod
    def ejecutar_calculo(lista_numeros: list):
        agregador = AgregadorDinamico()
        # Se desempaqueta la lista usando '*' para pasar los valores como *args al método
        agregador.sumar_elementos(*lista_numeros)


# ---------------------------------------------------------------------
# EJERCICIO 3: Función recursiva para calcular el factorial de n.
# ---------------------------------------------------------------------
class CalculadorRecursivo:
    def __init__(self, numero_limite: int):
        self.limite = numero_limite

    def obtener_factorial(self, n: int) -> int:
        # Caso base obligatorio de la recursividad [cite: 330]
        if n == 0:
            return 1  # [cite: 330]
        # Llamada recursiva disminuyendo el estado [cite: 330]
        return n * self.obtener_factorial(n - 1)  # [cite: 330]

    def mostrar_resultado(self):
        print("🧬 CÁLCULO DE FACTORIAL MEDIANTE RECURSIVIDAD")
        print("--------------------------------------------------")
        if self.limite < 0:
            print("❌ Error: No se puede calcular el factorial de un número negativo.")
            return
            
        resultado_final = self.obtener_factorial(self.limite) #[cite: 332]
        print(f"➡️ El factorial de {self.limite}! es igual a: {resultado_final}")


class GestorFactorial:
    @staticmethod
    def ejecutar_analisis(numero_entero: int):
        calculador = CalculadorRecursivo(numero_entero)
        calculador.mostrar_resultado()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(numero):
    GestorDuplicador.ejecutar_demostracion(numero)

def ejecutar_ejercicio2(lista_valores):
    GestorSumadorArgs.ejecutar_calculo(lista_valores)

def ejecutar_ejercicio3(numero_factorial):
    GestorFactorial.ejecutar_analisis(numero_factorial)