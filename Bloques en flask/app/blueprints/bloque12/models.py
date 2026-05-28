# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 12: EXCEPCIONES (try / except)
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Captura ValueError al convertir input del usuario a int.
# ---------------------------------------------------------------------
class ConvertidorSeguro:
    def __init__(self, texto: str):
        self.texto = texto

    def convertir_a_entero(self):
        print("🛡️ EXCEPCIONES — Captura de ValueError")
        print("--------------------------------------------------")
        print(f"  Intentando convertir el texto: '{self.texto}' → int()")
        try:
            resultado = int(self.texto)
            print(f"  ✅ Conversión exitosa: {resultado}")
        except ValueError as e:
            print(f"  ❌ ValueError capturado:")
            print(f"     {e}")
            print("\n  💡 int() lanza ValueError cuando el texto no representa un número entero válido.")


class GestorConversionSegura:
    @staticmethod
    def ejecutar_demostracion(texto: str):
        ConvertidorSeguro(texto).convertir_a_entero()


# ---------------------------------------------------------------------
# EJERCICIO 2: Captura IndexError al acceder lista[5] en lista de 3 elementos.
# ---------------------------------------------------------------------
class AccesorListaSeguro:
    def __init__(self, lista: list, indice: int):
        self.lista  = lista
        self.indice = indice

    def acceder(self):
        print(f"🛡️ EXCEPCIONES — Captura de IndexError")
        print("--------------------------------------------------")
        print(f"  Lista   : {self.lista}")
        print(f"  Índice  : {self.indice}")
        try:
            valor = self.lista[self.indice]
            print(f"  ✅ Acceso exitoso: lista[{self.indice}] = {valor}")
        except IndexError as e:
            print(f"  ❌ IndexError capturado:")
            print(f"     {e}")
            print(f"\n  💡 La lista tiene {len(self.lista)} elementos (índices 0 a {len(self.lista)-1}).")
            print(f"     El índice {self.indice} está fuera de rango.")


class GestorAccesoLista:
    @staticmethod
    def ejecutar_demostracion(lista: list, indice: int):
        AccesorListaSeguro(lista, indice).acceder()


# ---------------------------------------------------------------------
# EJERCICIO 3: try/except que maneje ValueError y ZeroDivisionError.
# ---------------------------------------------------------------------
class CalculadoraSegura:
    def __init__(self, texto_num: str, divisor: float):
        self.texto_num = texto_num
        self.divisor   = divisor

    def dividir(self):
        print("🛡️ EXCEPCIONES — Múltiples except (ValueError + ZeroDivisionError)")
        print("--------------------------------------------------")
        print(f"  Texto a convertir : '{self.texto_num}'")
        print(f"  Divisor           : {self.divisor}")
        try:
            numero   = int(self.texto_num)
            resultado = numero / self.divisor
            print(f"\n  ✅ Resultado: {numero} / {self.divisor} = {resultado}")
        except ValueError as e:
            print(f"\n  ❌ ValueError → No se pudo convertir '{self.texto_num}' a entero.")
            print(f"     Detalle: {e}")
        except ZeroDivisionError as e:
            print(f"\n  ❌ ZeroDivisionError → No se puede dividir entre cero.")
            print(f"     Detalle: {e}")
        finally:
            print("\n  ✔ Bloque finally ejecutado siempre (cierre de recursos, logs, etc.).")


class GestorCalculadoraSegura:
    @staticmethod
    def ejecutar_analisis(texto_num: str, divisor: float):
        CalculadoraSegura(texto_num, divisor).dividir()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(texto):
    GestorConversionSegura.ejecutar_demostracion(texto)

def ejecutar_ejercicio2(lista, indice):
    GestorAccesoLista.ejecutar_demostracion(lista, indice)

def ejecutar_ejercicio3(texto_num, divisor):
    GestorCalculadoraSegura.ejecutar_analisis(texto_num, divisor)
