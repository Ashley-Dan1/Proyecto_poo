# =====================================================================
# BLOQUE 17: MIXINS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: ValidacionMixin + SistemaEstudiantes.
# ---------------------------------------------------------------------
class ValidacionMixin:
    """Mixin de validación — no se instancia sola."""
    def validar_nombre(self, nombre: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

    def validar_edad(self, edad: int):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")


class SistemaEstudiantes(ValidacionMixin):
    def __init__(self):
        self.estudiantes = []

    def registrar(self, nombre: str, edad: int):
        self.validar_nombre(nombre)
        self.validar_edad(edad)
        self.estudiantes.append({"nombre": nombre, "edad": edad})
        print(f"✅ Registrado exitosamente: {nombre}, {edad} años")


class GestorValidacionMixin:
    @staticmethod
    def ejecutar_demostracion(nombre: str, edad: int):
        print("🧩 MIXIN — ValidacionMixin en SistemaEstudiantes")
        print("--------------------------------------------------")
        sistema = SistemaEstudiantes()
        try:
            sistema.registrar(nombre, edad)
            print(f"📋 Estudiantes registrados: {sistema.estudiantes}")
        except ValueError as e:
            print(f"❌ Validación fallida: {e}")


# ---------------------------------------------------------------------
# EJERCICIO 2: PromedioMixin integrado junto con ValidacionMixin.
# ---------------------------------------------------------------------
class PromedioMixin:
    """Mixin de cálculo de promedio — no se instancia sola."""
    def calcular_promedio(self, notas: list) -> float:
        if not notas:
            return 0.0
        return sum(notas) / len(notas)


class SistemaCompleto(ValidacionMixin, PromedioMixin):
    def __init__(self):
        self.registro = []

    def registrar_con_promedio(self, nombre: str, edad: int, notas: list):
        self.validar_nombre(nombre)
        self.validar_edad(edad)
        promedio = self.calcular_promedio(notas)
        self.registro.append({"nombre": nombre, "edad": edad, "promedio": promedio})
        print(f"✅ {nombre} registrado | Edad: {edad} | Notas: {notas}")
        print(f"   Promedio calculado por PromedioMixin: {promedio:.2f}")


class GestorSistemaCompleto:
    @staticmethod
    def ejecutar_calculo(nombre: str, edad: int, notas: list):
        print("🧩 MIXINS COMBINADOS — ValidacionMixin + PromedioMixin")
        print("--------------------------------------------------")
        sistema = SistemaCompleto()
        try:
            sistema.registrar_con_promedio(nombre, edad, notas)
        except ValueError as e:
            print(f"❌ Error: {e}")


# ---------------------------------------------------------------------
# EJERCICIO 3: MRO — class C(A, B), ¿qué imprime C().metodo()?
# ---------------------------------------------------------------------
class ClaseA:
    def metodo(self):
        print("A")

class ClaseB:
    def metodo(self):
        print("B")

class ClaseC(ClaseA, ClaseB):
    pass


class ExplicadorMRO:
    def mostrar(self):
        print("🔍 MRO — Orden de Resolución de Métodos")
        print("--------------------------------------------------")
        print("Jerarquía: class C(A, B)")
        print("Ambas clases tienen metodo(). ¿Cuál ejecuta C?\n")
        print("Resultado de C().metodo():")
        ClaseC().metodo()
        print(f"\nMRO de C: {[cls.__name__ for cls in ClaseC.__mro__]}")
        print("\n💡 Python busca el método de izquierda a derecha en la herencia.")
        print("   C → A → B → object")
        print("   Encuentra metodo() en A primero → imprime 'A'.")


class GestorMRO:
    @staticmethod
    def ejecutar_analisis():
        ExplicadorMRO().mostrar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(nombre, edad):
    GestorValidacionMixin.ejecutar_demostracion(nombre, edad)

def ejecutar_ejercicio2(nombre, edad, notas):
    GestorSistemaCompleto.ejecutar_calculo(nombre, edad, notas)

def ejecutar_ejercicio3():
    GestorMRO.ejecutar_analisis()