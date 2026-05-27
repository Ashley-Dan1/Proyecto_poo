# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 3: OPERADORES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Con a=20, b=4 imprime todos los operadores aritméticos y sus resultados.
# ---------------------------------------------------------------------
class CalculadoraAritmetica:
    def __init__(self, numero_a: float, numero_b: float):
        self.a = numero_a
        self.b = numero_b

    def ejecutar_operaciones(self):
        print(f"📊 OPERACIONES ARITMÉTICAS ENTRE {self.a} Y {self.b}")
        print("--------------------------------------------------")
        # Se calculan y despliegan todos los operadores solicitados por el compendio
        print(f"➕ Suma (a + b)            = {self.a + self.b}")
        print(f"➖ Resta (a - b)           = {self.a - self.b}")
        print(f"✖️ Multiplicación (a * b)   = {self.a * self.b}")
        print(f"➗ División Decimal (a / b) = {self.a / self.b}")
        print(f"🧮 División Entera (a // b) = {self.a // self.b}")
        print(f"🛑 Módulo / Residuo (a % b) = {self.a % self.b}")
        print(f"⚡ Potencia (a ** b)        = {self.a ** self.b}")


class GestorAritmetico:
    @staticmethod
    def ejecutar_demostracion(num_a: float, num_b: float):
        # La clase envuelve el flujo e inicializa los parámetros interactivos
        calculadora = CalculadoraAritmetica(num_a, num_b)
        calculadora.ejecutar_operaciones()


# ---------------------------------------------------------------------
# EJERCICIO 2: Crea dos listas idénticas y demuestra que == es True pero is es False.
# ---------------------------------------------------------------------
class ComparadorIdentidad:
    def __init__(self, elemento1, elemento2):
        # Guardamos dos elementos para armar colecciones idénticas en contenido
        self.elem1 = elemento1
        self.elem2 = elemento2

    def analizar_referencias(self):
        print("🧪 COMPARACIÓN DE CONTENIDO (==) VS IDENTIDAD EN MEMORIA (is)")
        print("--------------------------------------------------")
        
        # Creamos dos listas físicamente distintas pero con el mismo contenido
        lista_a = [self.elem1, self.elem2]
        lista_b = [self.elem1, self.elem2]
        
        # Creamos una tercera variable que apunta exactamente a la misma dirección que lista_a
        lista_c = lista_a

        print(f"Lista A: {lista_a} | ID Memoria: {id(lista_a)}")
        print(f"Lista B: {lista_b} | ID Memoria: {id(lista_b)}")
        print(f"Lista C (Apunta a A): {lista_c} | ID Memoria: {id(lista_c)}\n")

        # Demostración del operador de valor (==)
        print(f"❓ ¿lista_a == lista_b? -> {lista_a == lista_b} (Tienen el mismo contenido de valores)")
        
        # Demostración del operador de identidad (is)
        print(f"❓ ¿lista_a is lista_b? -> {lista_a is lista_b} (False: Son dos objetos distintos en la RAM)")
        print(f"❓ ¿lista_a is lista_c? -> {lista_a is lista_c} (True: Apuntan exactamente a la misma referencia)")


class GestorIdentidad:
    @staticmethod
    def ejecutar_prueba(valor1, valor2):
        comparador = ComparadorIdentidad(valor1, valor2)
        comparador.analizar_referencias()


# ---------------------------------------------------------------------
# EJERCICIO 3: Evalúa: x = 2 + 1 * 2 % 2 + (2 ** 1) // 2 -> explica el orden.
# ---------------------------------------------------------------------
class AnalizadorPrecedencia:
    def __init__(self):
        # La expresión matemática original del compendio
        self.expresion_texto = "2 + 1 * 2 % 2 + (2 ** 1) // 2"

    def resolver_y_explicar(self):
        print("🧠 RESOLUCIÓN Y ORDEN DE EVALUACIÓN DE OPERADORES")
        print("--------------------------------------------------")
        print(f"Expresión a evaluar: {self.expresion_texto}\n")
        
        # Explicación del paso a paso técnico según la jerarquía de Python
        print("1° Paréntesis y Potencia: (2 ** 1) -> 2")
        print("2° Multiplicación y Módulo: 1 * 2 % 2 -> 2 % 2 -> 0")
        print("3° División entera: 2 // 2 -> 1")
        print("4° Sumas finales de izquierda a derecha: 2 + 0 + 1 -> 3\n")
        
        # Cálculo real en el motor de Python
        resultado_real = 2 + 1 * 2 % 2 + (2 ** 1) // 2
        print(f"✅ Resultado final obtenido por la máquina: {resultado_real}")


class GestorPrecedencia:
    @staticmethod
    def ejecutar_analisis():
        analizador = AnalizadorPrecedencia()
        analizador.resolver_y_explicar()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(a_web, b_web):
    GestorAritmetico.ejecutar_demostracion(a_web, b_web)

def ejecutar_ejercicio2(item1, item2):
    GestorIdentidad.ejecutar_prueba(item1, item2)

def ejecutar_ejercicio3():
    GestorPrecedencia.ejecutar_analisis()