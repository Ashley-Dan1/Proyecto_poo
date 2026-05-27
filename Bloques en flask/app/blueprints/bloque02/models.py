# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 2: VARIABLES Y TIPOS DE DATOS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crear la clase CuentaBancaria con titular y saldo (instancia).
# Instanciar 2 cuentas con saldos distintos.
# ---------------------------------------------------------------------
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        # Atributos de instancia (pertenecen a cada objeto individual)
        self.titular = titular
        self.saldo = saldo_inicial

    def mostrar_informacion(self):
        print(f"💳 Cuenta -> Titular: {self.titular} | Saldo Disponible: ${self.saldo}")


class GestorCuentasSimples:
    @staticmethod
    def ejecutar_demostracion():
        print("💰 DEMOSTRACIÓN DE ATRIBUTOS DE INSTANCIA")
        print("--------------------------------------------------")
        # Instanciamos los 2 objetos independientes requeridos
        cuenta1 = CuentaBancaria("Carlos", 1500.50)
        cuenta2 = CuentaBancaria("Ana", 2800.00)
        
        cuenta1.mostrar_informacion()
        cuenta2.mostrar_informacion()


# ---------------------------------------------------------------------
# EJERCICIO 2: Agregar un atributo de clase llamado 'tasa_interes' = 0.05.
# Crear un método para aplicar ese interés al saldo.
# ---------------------------------------------------------------------
class CuentaConInteres:
    # Atributo de Clase (compartido por todas las instancias)
    tasa_interes = 0.05

    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def aplicar_interes_anual(self):
        # Calculamos el interés usando el atributo de clase
        interes_calculado = self.saldo * CuentaConInteres.tasa_interes
        self.saldo += interes_calculado
        print(f"📈 Interés del {CuentaConInteres.tasa_interes * 100}% aplicado.")
        print(f"💰 Nuevo saldo de {self.titular}: ${self.saldo:.2f}")


class GestorInteresCuentas:
    @staticmethod
    def probar_calculo(titular_web: str, saldo_web: float):
        print("🏦 APLICACIÓN DE ATRIBUTO DE CLASE (ESTÁTICO)")
        print("--------------------------------------------------")
        # Creamos el objeto con los datos interactivos recibidos de la web
        cuenta_usuario = CuentaConInteres(titular_web, saldo_web)
        print(f"Saldo inicial de {cuenta_usuario.titular}: ${cuenta_usuario.saldo}")
        
        # Ejecutamos el método que muta el atributo usando la tasa de clase
        cuenta_usuario.aplicar_interes_anual()


# ---------------------------------------------------------------------
# EJERCICIO 3: Demostrar el tipado dinámico cambiando el atributo 'saldo'
# de float a un string de advertencia, y luego volver a float.
# ---------------------------------------------------------------------
class EvaluadorTipadoBancario:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial

    def ejecutar_mutacion_tipo(self, mensaje_alerta: str, saldo_reinicio: float):
        print("🧪 PRUEBA DE TIPADO DINÁMICO EN ATRIBUTOS")
        print("--------------------------------------------------")
        print(f"1. Estado Inicial -> Tipo de 'saldo': {type(self.saldo).__name__} | Valor: {self.saldo}")
        
        # Cambiamos dinámicamente el tipo de dato a String (Alerta)
        self.saldo = mensaje_alerta
        print(f"2. Estado Mutado -> Tipo de 'saldo': {type(self.saldo).__name__} | Valor: '{self.saldo}'")
        
        # Restauramos el tipo de dato a Float
        self.saldo = float(saldo_reinicio)
        print(f"3. Estado Restaurado -> Tipo de 'saldo': {type(self.saldo).__name__} | Valor: {self.saldo}")


class GestorTipadoDinamico:
    @staticmethod
    def ejecutar_simulacion(nombre: str, alerta: str, reinicio: float):
        # La clase envuelve obligatoriamente la ejecución de la prueba
        evaluador = EvaluadorTipadoBancario(nombre, 500.0)
        evaluador.ejecutar_mutacion_tipo(alerta, reinicio)


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1():
    GestorCuentasSimples.ejecutar_demostracion()

def ejecutar_ejercicio2(titular, saldo):
    GestorInteresCuentas.probar_calculo(titular, saldo)

def ejecutar_ejercicio3(titular, alerta, reinicio):
    GestorTipadoDinamico.ejecutar_simulacion(titular, alerta, reinicio)