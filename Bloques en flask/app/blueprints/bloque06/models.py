# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 6: BUCLES (LOOPS)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Imprime los números del 1 al 10 usando un bucle for.
# ---------------------------------------------------------------------
class ContadorAscendente:
    def __init__(self, limite_maximo: int):
        self.limite = limite_maximo

    def generar_conteo(self):
        print(f"🔄 SECUENCIA NUMÉRICA CON BUCLE FOR (1 AL {self.limite})")
        print("--------------------------------------------------")
        # El rango en Python es exclusivo al final, por eso sumamos 1
        for numero in range(1, self.limite + 1):
            print(f"👉 Número actual: {numero}")


class GestorContadorFor:
    @staticmethod
    def ejecutar_demostracion(limite: int):
        contador = ContadorAscendente(limite)
        contador.generar_conteo()


# ---------------------------------------------------------------------
# EJERCICIO 2: Imprime los números del 10 al 1 usando un bucle while.
# ---------------------------------------------------------------------
class ContadorDescendente:
    def __init__(self, inicio_conteo: int):
        self.inicio = inicio_conteo

    def disminuir_conteo(self):
        print(f"⏳ CUENTA REGRESIVA CON BUCLE WHILE ({self.inicio} AL 1)")
        print("--------------------------------------------------")
        controlador = self.inicio
        # El ciclo se ejecuta mientras la condición lógica sea verdadera
        while controlador >= 1:
            print(f"⏱️ Valor actual del bucle: {controlador}")
            controlador -= 1  # Modificador crucial para evitar bucles infinitos
        print("🏁 ¡Ciclo finalizado!")


class GestorContadorWhile:
    @staticmethod
    def ejecutar_calculo(inicio: int):
        contador = ContadorDescendente(inicio)
        contador.disminuir_conteo()


# ---------------------------------------------------------------------
# EJERCICIO 3: Suma todos los números pares del 1 al 50.
# ---------------------------------------------------------------------
class SumadorPares:
    def __init__(self, rango_maximo: int):
        self.rango = rango_maximo
        self.acumulador_suma = 0

    def procesar_suma(self):
        print(f"🧮 ACUMULACIÓN DE VALORES PARES (1 AL {self.rango})")
        print("--------------------------------------------------")
        
        for numero in range(1, self.rango + 1):
            # Condición para verificar si el número es par
            if numero % 2 == 0:
                self.acumulador_suma += numero
                
        print(f"✅ La suma total de los números pares encontrados es: {self.acumulador_suma}")


class GestorSumadorPares:
    @staticmethod
    def ejecutar_analisis(limite: int):
        sumador = SumadorPares(limite)
        sumador.procesar_suma()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(limite):
    GestorContadorFor.ejecutar_demostracion(limite)

def ejecutar_ejercicio2(inicio):
    GestorContadorWhile.ejecutar_calculo(inicio)

def ejecutar_ejercicio3(limite):
    GestorSumadorPares.ejecutar_analisis(limite)