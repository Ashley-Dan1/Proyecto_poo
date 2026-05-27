# =====================================================================
# BLOQUE 05: CONDICIONALES
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Determina si un número es par o impar.
# ---------------------------------------------------------------------
class EvaluadorParImpar:
    def __init__(self, numero: int):
        self.numero = numero

    def evaluar(self):
        print("🔢 PAR O IMPAR")
        print("--------------------------------------------------")
        print(f"Número ingresado: {self.numero}")
        if self.numero % 2 == 0:
            print(f"➡️ {self.numero} es PAR")
        else:
            print(f"➡️ {self.numero} es IMPAR")


class GestorParImpar:
    @staticmethod
    def ejecutar_demostracion(numero: int):
        EvaluadorParImpar(numero).evaluar()


# ---------------------------------------------------------------------
# EJERCICIO 2: Calificación numérica → letra (A, B, C, D).
# ---------------------------------------------------------------------
class EvaluadorNota:
    def __init__(self, nota: float):
        self.nota = nota

    def determinar_letra(self):
        print("🎓 CALIFICACIÓN EN LETRA (A / B / C / D)")
        print("--------------------------------------------------")
        print(f"Nota ingresada: {self.nota}")

        if self.nota < 0 or self.nota > 100:
            print("❌ La nota debe estar entre 0 y 100.")
            return

        if self.nota >= 90:
            letra = "A"
        elif self.nota >= 80:
            letra = "B"
        elif self.nota >= 70:
            letra = "C"
        else:
            letra = "D"

        print(f"➡️ Calificación equivalente: {letra}")


class GestorNota:
    @staticmethod
    def ejecutar_calculo(nota: float):
        EvaluadorNota(nota).determinar_letra()


# ---------------------------------------------------------------------
# EJERCICIO 3: Sistema de login — usuario=='admin' y password=='123'.
# ---------------------------------------------------------------------
class SistemaLogin:
    USUARIO_CORRECTO = "admin"
    PASSWORD_CORRECTA = "123"

    def __init__(self, usuario: str, password: str):
        self.usuario = usuario
        self.password = password

    def validar_acceso(self):
        print("🔐 SISTEMA DE LOGIN")
        print("--------------------------------------------------")
        print(f"Usuario ingresado: '{self.usuario}'")

        if self.usuario == self.USUARIO_CORRECTO and self.password == self.PASSWORD_CORRECTA:
            print("✅ Bienvenido")
        else:
            print("🔒 Acceso denegado")


class GestorLogin:
    @staticmethod
    def ejecutar_analisis(usuario: str, password: str):
        SistemaLogin(usuario, password).validar_acceso()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(numero):
    GestorParImpar.ejecutar_demostracion(numero)

def ejecutar_ejercicio2(nota):
    GestorNota.ejecutar_calculo(nota)

def ejecutar_ejercicio3(usuario, password):
    GestorLogin.ejecutar_analisis(usuario, password)