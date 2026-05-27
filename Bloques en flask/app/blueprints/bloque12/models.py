# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 12: DECORADORES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crea un decorador que imprima "Iniciando..." antes de ejecutar.
# ---------------------------------------------------------------------
class GestorDecoradorAviso:
    @staticmethod
    def decorador_inicio(funcion_original):
        # El wrapper empaqueta los argumentos dinámicos de forma segura
        def wrapper(*args, **kwargs):
            print("🚀 [Decorador] Iniciando ejecución de la subrutina...")
            resultado = funcion_original(*args, **kwargs)
            print("🏁 [Decorador] Ejecución finalizada con éxito.")
            return resultado
        return wrapper


class ComponenteMensaje:
    def __init__(self, contenido_texto: str):
        self.texto = contenido_texto

    # Aplicamos el método decorador estático de la clase gestora
    @GestorDecoradorAviso.decorador_inicio
    def mostrar_notificacion(self):
        print(f"💬 Mensaje procesado internamente: {self.texto}")


class GestorAvisoSimple:
    @staticmethod
    def ejecutar_demostracion(texto_usuario: str):
        componente = ComponenteMensaje(texto_usuario)
        componente.mostrar_notificacion()


# ---------------------------------------------------------------------
# EJERCICIO 2: Crea un decorador que verifique que el argumento sea positivo.
# ---------------------------------------------------------------------
class GestorDecoradorValidacion:
    @staticmethod
    def verificar_positivo(funcion_original):
        def wrapper(instancia, valor_numerico: float):
            # Filtro lógico de control antes de disparar la función núcleo
            if valor_numerico < 0:
                print(f"❌ [Decorador Error] El valor ingresado ({valor_numerico}) es negativo. Operación cancelada.")
                return None
            return funcion_original(instancia, valor_numerico)
        return wrapper


class CalculadorMatematico:
    def __init__(self):
        pass

    # Aplicamos el decorador para blindar el parámetro de entrada del método
    @GestorDecoradorValidacion.verificar_positivo
    def obtener_cuadrado(self, numero: float):
        resultado = numero ** 2
        print(f"📐 [Método] El cuadrado matemático de {numero} es: {resultado}")
        return resultado


class GestorValidacionFiltro:
    @staticmethod
    def ejecutar_calculo(numero_web: float):
        calculador = CalculadorMatematico()
        calculador.obtain_area = calculador.obtener_cuadrado(numero_web)


# ---------------------------------------------------------------------
# EJERCICIO 3: Analiza @log def suma(a,b). ¿Qué imprime suma(2,3)?
# ---------------------------------------------------------------------
class SimuladorDecoradorLog:
    @staticmethod
    def log_trazabilidad(funcion_original):
        def wrapper(instancia, a: float, b: float):
            print(f"📊 [Log] Llamando función con argumentos de entrada: a={a}, b={b}")
            resultado = funcion_original(instancia, a, b)
            print(f"📊 [Log] Retorno de la función calculado: {resultado}")
            return resultado
        return wrapper


class OperacionAritmetica:
    def __init__(self):
        pass

    @SimuladorDecoradorLog.log_trazabilidad
    def calcular_suma(self, a: float, b: float):
        return a + b


class GestorAnalisisLog:
    @staticmethod
    def ejecutar_analisis(operando_a: float, operando_b: float):
        operacion = OperacionAritmetica()
        print("🧠 SIMULACIÓN Y ANÁLISIS DEL DECORADOR @LOG")
        print("--------------------------------------------------")
        operacion.calcular_suma(operando_a, operando_b)


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(texto):
    GestorAvisoSimple.ejecutar_demostracion(texto)

def ejecutar_ejercicio2(numero):
    GestorValidacionFiltro.ejecutar_calculo(numero)

def ejecutar_ejercicio3(a, b):
    GestorAnalisisLog.ejecutar_analisis(a, b)