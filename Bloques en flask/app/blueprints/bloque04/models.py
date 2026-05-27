# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 4: ENTRADA Y SALIDA (INPUT/PRINT)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Solicita nombre y edad; muestra un mensaje personalizado con f-string.
# ---------------------------------------------------------------------
class MensajePersonalizado:
    def __init__(self, nombre_usuario: str, edad_usuario: int):
        self.nombre = nombre_usuario
        self.edad = edad_usuario

    def saludar(self):
        print("💬 MENSAJE PERSONALIZADO CON F-STRING")
        print("--------------------------------------------------")
        # Se utiliza f-string para formatear la salida como pide el compendio
        print(f"👋 ¡Hola, {self.nombre}! El sistema registra que tienes {self.edad} años y estás programando en Python.")


class GestorSaludos:
    @staticmethod
    def ejecutar_demostracion(nombre: str, edad: int):
        usuario = MensajePersonalizado(nombre, edad)
        usuario.saludar()


# ---------------------------------------------------------------------
# EJERCICIO 2: Lee dos números, calcula su suma y promedio, e imprímelos.
# ---------------------------------------------------------------------
class CalculadoraEstadistica:
    def __init__(self, numero1: float, numero2: float):
        # El constructor recibe los datos emulando el casting numérico de los inputs
        self.num1 = numero1
        self.num2 = numero2

    def calcular_y_mostrar(self):
        print("📊 CÁLCULO DE SUMA Y PROMEDIO (CON CASTING)")
        print("--------------------------------------------------")
        suma_total = self.num1 + self.num2
        promedio_calculado = suma_total / 2
        
        print(f"🔢 Primer número : {self.num1}")
        print(f"🔢 Segundo número: {self.num2}")
        print(f"➕ Suma total    : {suma_total}")
        print(f"📈 Promedio      : {promedio_calculado}")


class GestorEstadistico:
    @staticmethod
    def ejecutar_calculo(n1: float, n2: float):
        calculadora = CalculadoraEstadistica(n1, n2)
        calculadora.calcular_y_mostrar()


# ---------------------------------------------------------------------
# EJERCICIO 3: Sin convertir el input, imprime el resultado de número + "5". ¿Qué pasa?
# ---------------------------------------------------------------------
class DemostradorConcatenacion:
    def __init__(self, entrada_cruda: str):
        # Guardamos el input directo como string (sin hacer casting)
        self.entrada = str(entrada_cruda)

    def simular_operacion(self):
        print("🧪 PRUEBA DE COMPORTAMIENTO: TEXTO + TEXTO")
        print("--------------------------------------------------")
        print(f"Valor recibido del input (str): '{self.entrada}'")
        print("Operación a ejecutar: numero + '5'")
        
        # Al no hacer casting, el operador '+' concatena las cadenas en lugar de sumar
        resultado = self.entrada + "5"
        
        print(f"➡️ Resultado obtenido: '{resultado}'")
        print("\n💡 Explicación POO: Al no convertir el input a tipo numérico con int() o float(),")
        print("Python detecta que ambos operandos son cadenas de texto (str). Por lo tanto,")
        print("el operador '+' activa su comportamiento de concatenación en lugar de suma aritmética.")


class GestorConcatenacion:
    @staticmethod
    def ejecutar_analisis(texto_input: str):
        demostrador = DemostradorConcatenacion(texto_input)
        demostrador.simular_operacion()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(nombre, edad):
    GestorSaludos.ejecutar_demostracion(nombre, edad)

def ejecutar_ejercicio2(n1, n2):
    GestorEstadistico.ejecutar_calculo(n1, n2)

def ejecutar_ejercicio3(entrada):
    GestorConcatenacion.ejecutar_analisis(entrada)