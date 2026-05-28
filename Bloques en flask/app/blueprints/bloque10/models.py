# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 10: DICCIONARIOS
# =====================================================================

class InspectorDiccionario:
    def __init__(self, nombre: str, edad: int, ciudad: str):
        self.persona = {
            "nombre": nombre,
            "edad":   edad,
            "ciudad": ciudad
        }

    def mostrar_accesos(self):
        print("📖 DICCIONARIOS — Acceso con [] y get()")
        print("--------------------------------------------------")
        print(f"  Diccionario : {self.persona}")
        print(f"\n  Acceso directo []:")
        print(f"    persona['nombre'] → {self.persona['nombre']}")
        print(f"    persona['edad']   → {self.persona['edad']}")
        print(f"\n  Acceso seguro get():")
        print(f"    persona.get('ciudad')              → {self.persona.get('ciudad')}")
        print(f"    persona.get('telefono', 'N/A')     → {self.persona.get('telefono', 'N/A')}")
        print("\n💡 get() evita KeyError si la clave no existe; devuelve None o el valor por defecto.")


class GestorAccesoDiccionario:
    @staticmethod
    def ejecutar_demostracion(nombre: str, edad: int, ciudad: str):
        InspectorDiccionario(nombre, edad, ciudad).mostrar_accesos()


class IteradorDiccionario:
    def __init__(self, nombre: str, edad: int, ciudad: str):
        self.persona = {
            "nombre": nombre,
            "edad":   edad,
            "ciudad": ciudad
        }

    def iterar(self):
        print("🔄 DICCIONARIOS — Iteración con items()")
        print("--------------------------------------------------")
        print(f"  Diccionario : {self.persona}\n")
        for clave, valor in self.persona.items():
            print(f"    {clave:10} → {valor}")
        print("\n💡 .items() retorna pares (clave, valor) como una vista iterable.")


class GestorIteracionDiccionario:
    @staticmethod
    def ejecutar_demostracion(nombre: str, edad: int, ciudad: str):
        IteradorDiccionario(nombre, edad, ciudad).iterar()


class DemostradorCopiaDict:
    def __init__(self):
        self.datos_originales = {"a": 1}

    def demostrar(self):
        print("🔍 DICCIONARIOS — referencia vs copia (.copy())")
        print("--------------------------------------------------")
        datos      = dict(self.datos_originales)
        copia_ref  = datos
        copia_real = datos.copy()

        print(f"  datos      = {datos}")
        print(f"  copia_ref  = datos        → misma referencia en memoria")
        print(f"  copia_real = datos.copy() → objeto nuevo independiente\n")

        copia_ref["b"] = 2
        print(f"  Después de copia_ref['b'] = 2 :")
        print(f"    datos      : {datos}      ← también cambió")
        print(f"    copia_real : {copia_real}  ← no cambió")
        print("\n💡 Usa .copy() cuando necesites un diccionario independiente.")


class GestorCopiaDict:
    @staticmethod
    def ejecutar_demostracion():
        DemostradorCopiaDict().demostrar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(nombre, edad, ciudad):
    GestorAccesoDiccionario.ejecutar_demostracion(nombre, edad, ciudad)

def ejecutar_ejercicio2(nombre, edad, ciudad):
    GestorIteracionDiccionario.ejecutar_demostracion(nombre, edad, ciudad)

def ejecutar_ejercicio3():
    GestorCopiaDict.ejecutar_demostracion()
