# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 1: EL CONSTRUCTOR __init__
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crear la clase Producto con código, nombre y precio. Instanciar 2 productos.
# ---------------------------------------------------------------------
class ProductoSimple:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self):
        print(f"📦 Producto -> Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio}")


class GestorProductosSimples:
    @staticmethod
    def ejecutar_demostracion():
        print("🛒 INSTANCIACIÓN BÁSICA DE PRODUCTOS")
        print("--------------------------------------------------")
        # Instanciamos los 2 productos solicitados por el compendio
        producto1 = ProductoSimple("P001", "Laptop", 900.0)
        producto2 = ProductoSimple("P002", "Mouse", 25.0)
        
        producto1.mostrar_detalle()
        producto2.mostrar_detalle()


# ---------------------------------------------------------------------
# EJERCICIO 2: Agregar validación para que el precio no sea negativo.
# ---------------------------------------------------------------------
class ProductoConValidacion:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        # Aplicamos la validación obligatoria con raise ValueError
        if precio < 0:
            raise ValueError("El precio no puede ser un valor negativo")
        self.precio = precio

    def mostrar_resultado(self):
        print(f"✅ Objeto creado exitosamente: {self.nombre} (${self.precio})")


class GestorValidacionProductos:
    @staticmethod
    def probar_instancia(precio_recibido: float):
        print("🛡️ PRUEBA DE CONSTRUCTOR CON VALIDACIÓN")
        print("--------------------------------------------------")
        print(f"Intentando crear un Producto con precio: ${precio_recibido}")
        try:
            # Intentamos instanciar la clase con el parámetro interactivo
            prod = ProductoConValidacion("P-TEST", "Monitor Gamer", precio_recibido)
            prod.mostrar_resultado()
        except ValueError as error:
            # Capturamos el error exacto solicitado por el compendio
            print(f"❌ Error capturado en el constructor: {str(error)}")


# ---------------------------------------------------------------------
# EJERCICIO 3: Crear Estudiante con nombre y notas=None. Si no hay notas, inicia lista vacía.
# ---------------------------------------------------------------------
class Estudiante:
    def __init__(self, nombre: str, notas=None):
        self.nombre = nombre
        # Validación lógica solicitada por el compendio
        if notas is None:
            self.notas = []
        else:
            self.notas = notas

    def mostrar_estado(self):
        print(f"🎓 Estudiante: {self.nombre}")
        print(f"📝 Notas en el sistema: {self.notas}")


class GestorEstudiantes:
    @staticmethod
    def probar_inicializacion(nombre: str, tiene_notas_iniciales: bool):
        print("📋 EVALUACIÓN DE PARÁMETROS OPCIONALES MUTABLES")
        print("--------------------------------------------------")
        
        if tiene_notas_iniciales:
            notas_ejemplo = [18, 15, 20]
            print(f"Creando estudiante con notas iniciales: {notas_ejemplo}")
            alumno = Estudiante(nombre, notas_ejemplo)
        else:
            print("Creando estudiante sin pasar el parámetro de notas (debe ser None)...")
            alumno = Estudiante(nombre, None)
            
        alumno.mostrar_estado()


# ---------------------------------------------------------------------
# EJERCICIO 4: Agregar un @classmethod desde_diccionario que cree un Estudiante desde un dict.
# ---------------------------------------------------------------------
class EstudianteFabrica:
    def __init__(self, nombre: str, notas: list):
        self.nombre = nombre
        self.notas = notas

    # Constructor alternativo en español según el compendio
    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(datos["nombre"], datos.get("notas", []))

    def exportar_consola(self):
        print(f"🚀 Objeto fabricado por @classmethod -> Nombre: {self.nombre} | Registro de Notas: {self.notas}")


class GestorFabricaEstudiantes:
    @staticmethod
    def ejecutar_mapeo(nombre_web: str):
        print("🏭 DEMOSTRACIÓN DE CONSTRUCTOR ALTERNATIVO (@classmethod)")
        print("--------------------------------------------------")
        
        # Simulamos el diccionario estructurado con el parámetro interactivo de la web
        diccionario_datos = {
            "nombre": nombre_web,
            "notas": [14, 16, 19]
        }
        
        print(f"Diccionario de origen recibido: {diccionario_datos}")
        # Invocamos la creación mediante el método de clase
        nuevo_alumno = EstudianteFabrica.desde_diccionario(diccionario_datos)
        nuevo_alumno.exportar_consola()


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1():
    GestorProductosSimples.ejecutar_demostracion()

def ejecutar_ejercicio2(precio_interactivo):
    GestorValidacionProductos.probar_instancia(precio_interactivo)

def ejecutar_ejercicio3(nombre_interactivo, con_notas):
    GestorEstudiantes.probar_inicializacion(nombre_interactivo, con_notas)

def ejecutar_ejercicio4(nombre_interactivo):
    GestorFabricaEstudiantes.ejecutar_mapeo(nombre_interactivo)