# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 13: DECORADORES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Decorador que imprime "Iniciando..." antes de ejecutar.
# ---------------------------------------------------------------------
def decorador_inicio(funcion_original):
    def wrapper(*args, **kwargs):
        print("🚀 Iniciando...")
        resultado = funcion_original(*args, **kwargs)
        print("✅ Ejecución completada.")
        return resultado
    return wrapper


class DemostradorDecoradorSimple:
    def mostrar(self, nombre_funcion: str):
        print("🎨 DECORADORES — @decorador_inicio")
        print("--------------------------------------------------")
        print("Definición del decorador:")
        print("  def decorador_inicio(f):")
        print("      def wrapper(*args, **kwargs):")
        print("          print('🚀 Iniciando...')")
        print("          resultado = f(*args, **kwargs)")
        print("          print('✅ Ejecución completada.')")
        print("          return resultado")
        print("      return wrapper\n")

        @decorador_inicio
        def mi_funcion():
            print(f"  ▶ Ejecutando: {nombre_funcion}()")

        print(f"Llamando a {nombre_funcion}() decorada:\n")
        mi_funcion()
        print("\n💡 El decorador envuelve la función original sin modificar su código.")


class GestorDecoradorSimple:
    @staticmethod
    def ejecutar_demostracion(nombre_funcion: str):
        DemostradorDecoradorSimple().mostrar(nombre_funcion)


# ---------------------------------------------------------------------
# EJERCICIO 2: Decorador que verifica que el argumento sea positivo.
# ---------------------------------------------------------------------
def validar_positivo(funcion_original):
    def wrapper(numero):
        if numero < 0:
            print(f"  ❌ Validación fallida: {numero} no es positivo. La función no se ejecuta.")
            return None
        return funcion_original(numero)
    return wrapper


class DemostradorDecoradorValidacion:
    def mostrar(self, numero: float):
        print("🛡️ DECORADORES — Validación de argumento positivo")
        print("--------------------------------------------------")

        @validar_positivo
        def calcular_cuadrado(n):
            resultado = n ** 2
            print(f"  ✅ cuadrado({n}) = {resultado}")
            return resultado

        print(f"Probando con número: {numero}")
        calcular_cuadrado(numero)
        print()
        if numero >= 0:
            print("Probando también con un número negativo (-5):")
            calcular_cuadrado(-5)
        print("\n💡 El decorador actúa como guardián antes de que la función se ejecute.")


class GestorDecoradorValidacion:
    @staticmethod
    def ejecutar_calculo(numero: float):
        DemostradorDecoradorValidacion().mostrar(numero)


# ---------------------------------------------------------------------
# EJERCICIO 3: @log → ¿qué imprime suma(2, 3)?
# ---------------------------------------------------------------------
class DemostradorDecoradorLog:
    def mostrar(self, a: float, b: float):
        print("📋 DECORADORES — @log aplicado a suma(a, b)")
        print("--------------------------------------------------")

        def log(funcion_original):
            def wrapper(*args, **kwargs):
                print(f"  📝 Llamando función '{funcion_original.__name__}' con args={args}")
                resultado = funcion_original(*args, **kwargs)
                print(f"  📝 Retorno: {resultado}")
                return resultado
            return wrapper

        @log
        def suma(x, y):
            return x + y

        print(f"Ejecutando: suma({a}, {b})\n")
        resultado_final = suma(a, b)
        print(f"\n  Resultado final obtenido: {resultado_final}")
        print("\n💡 El decorador @log registra la llamada y el retorno sin tocar el cuerpo de suma().")


class GestorDecoradorLog:
    @staticmethod
    def ejecutar_analisis(a: float, b: float):
        DemostradorDecoradorLog().mostrar(a, b)


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(nombre_funcion):
    GestorDecoradorSimple.ejecutar_demostracion(nombre_funcion)

def ejecutar_ejercicio2(numero):
    GestorDecoradorValidacion.ejecutar_calculo(numero)

def ejecutar_ejercicio3(a, b):
    GestorDecoradorLog.ejecutar_analisis(a, b)
