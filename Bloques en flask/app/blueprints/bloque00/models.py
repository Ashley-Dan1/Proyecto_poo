# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 0: INTRODUCCIÓN A LA POO
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Identificar 5 clases para un sistema de biblioteca
# ---------------------------------------------------------------------
# El enunciado pide identificar clases. Para cumplir con la regla de clases
# obligatorias, creamos un contenedor que simula el plano de la biblioteca.

class SistemaBiblioteca:
    def __init__(self):
        # Mapeamos las 5 clases sugeridas por el compendio como la estructura
        self.clases_identificadas = ["Libro", "Usuario", "Prestamo", "Autor", "Categoria"]

    def mostrar_analisis(self):
        print("📚 ANALISIS DE MODELADO UML - SISTEMA DE BIBLIOTECA")
        print("--------------------------------------------------")
        print("Para estructurar el sistema se definieron los siguientes moldes:")
        for indice, clase in enumerate(self.clases_identificadas, 1):
            print(f"  [{indice}] Clase '{clase}' -> Representa una entidad del negocio.")
        print("\n💡 Conclusión POO: Cada clase agrupará sus propios atributos y métodos.")


# ---------------------------------------------------------------------
# EJERCICIO 2: Clase Persona con nombre y edad. Instanciar 3 objetos
# ---------------------------------------------------------------------
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"👤 Objeto Instanciado -> Nombre: {self.nombre} | Edad: {self.edad} años")


class GestorPersonas:
    @staticmethod
    def ejecutar_demostracion():
        print("🎭 CREACIÓN E IDENTIDAD DE OBJETOS EN MEMORIA RAM")
        print("--------------------------------------------------")
        # Instanciamos los 3 objetos diferentes requeridos
        persona1 = Persona("Carlos", 20)
        persona2 = Persona("Ana", 25)
        persona3 = Persona("Daniel", 19)
        
        # Ejecutamos sus métodos para comprobar su estado independiente
        persona1.presentarse()
        persona2.presentarse()
        persona3.presentarse()


# ---------------------------------------------------------------------
# EJERCICIO 3: Explicación de la diferencia entre Clase y Objeto
# ---------------------------------------------------------------------
class ExplicadorConceptos:
    def __init__(self):
        self.definicion_clase = "Molde, plano o plantilla conceptual que define qué propiedades y acciones tendrá un elemento."
        self.definicion_objeto = "La instancia física y real creada a partir de una clase; ocupa un lugar real en la memoria RAM."

    def mostrar_diferencia(self):
        print("🧠 CLARIFICACIÓN CONCEPTUAL: CLASE VS OBJETO")
        print("--------------------------------------------------")
        print(f"🏠 LA CLASE : {self.definicion_clase}")
        print(f"🔑 EL OBJETO: {self.definicion_objeto}")
        print("\n💻 Ejemplo Práctico: 'class Cliente' es el plano arquitectónico. El objeto 'cli = Cliente(\"Daniel\")' es la casa ya construida en la que puedes vivir.")


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1():
    biblioteca = SistemaBiblioteca()
    biblioteca.mostrar_analisis()

def ejecutar_ejercicio2():
    GestorPersonas.ejecutar_demostracion()

def ejecutar_ejercicio3():
    explicador = ExplicadorConceptos()
    explicador.mostrar_diferencia()