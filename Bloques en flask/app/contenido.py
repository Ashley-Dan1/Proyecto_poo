# app/contenido_pdf.py

COMPENDIO = {
    "bloque00": {
        "titulo": "Bloque 0: Introducción a la POO",
        "concepto": """¿Qué es la POO?
La Programación Orientada a Objetos (POO) es un paradigma que organiza el software alrededor de objetos, representando entidades del mundo real.
En lugar de pensar solo en funciones y pasos, la POO propone modelar el sistema como un conjunto de clases y objetos que interactúan entre sí.

Idea central: POO = Modelar la realidad en código

Clase vs Objeto
• Clase: molde o plantilla que define atributos y métodos → es el plano de una casa.
• Objeto: instancia de una clase, elemento real creado a partir del molde → es la casa construida.

¿Por qué usar POO?
• Organización: estructurar programas grandes de forma clara.
• Reutilización: usar clases en múltiples partes del sistema.
• Escalabilidad: el sistema puede crecer sin volverse caótico.""",
        "ejemplo": """class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

cli = Cliente("Daniel")
print(cli.nombre)  # Salida: Daniel
# cli es el OBJETO""",
        "total_ejercicios": 3
    },

    "bloque01": {
        "titulo": "Bloque 1: Sintaxis Básica e Impresión",
        "concepto": """Sintaxis Básica en Python
Python destaca por su sintaxis limpia y legible. A diferencia de otros lenguajes, no utiliza llaves {} para definir bloques de código, sino que se apoya estrictamente en la indentación (espacios o tabulaciones).

Variables y Asignación
En Python no es necesario declarar explícitamente el tipo de dato de una variable; el intérprete lo infiere de forma dinámica en tiempo de ejecución.

Impresión en Consola
La función integrada `print()` es la herramienta fundamental para enviar información a la salida estándar (stdout). Permite interpolar variables de forma elegante mediante f-strings.""",
        "ejemplo": """# Ejemplo de sintaxis e impresión
nombre_curso = "POO Avanzado"
print(f"Bienvenidos al curso de: {nombre_curso}")""",
        "total_ejercicios": 4
    },

    "bloque02": {
        "titulo": "Bloque 2: Variables y Tipos de Datos",
        "concepto": """Tipos de Datos Primitivos
Python maneja varios tipos de datos nativos esenciales para cualquier algoritmo:
• Enteros (int): Números sin decimales (ej. 25, -10).
• Flotantes (float): Números con precisión decimal (ej. 3.14, -0.5).
• Cadenas (str): Texto delimitado por comillas simples o dobles.
• Booleanos (bool): Valores de lógica binaria: True o False.

Tipado Dinámico
Una variable puede cambiar de tipo en cualquier momento simplemente asignándole un nuevo valor.""",
        "ejemplo": """edad = 25          # int
precio = 19.99      # float
nombre = "Carlos"   # str
activo = True       # bool

print(type(edad))   # <class 'int'>""",
        "total_ejercicios": 3
    },

    "bloque03": {
        "titulo": "Bloque 3: Operadores Aritméticos",
        "concepto": """Operaciones Matemáticas Básicas
Python incluye todos los operadores matemáticos estándar para realizar cálculos numéricos:
• Suma (+), Resta (-), Multiplicación (*) y División (/).
• División Entera (//): Descarta la parte decimal devolviendo solo el entero.
• Módulo (%): Devuelve el residuo de una división entera.
• Exponente (**): Eleva un número a la potencia de otro.""",
        "ejemplo": """a = 10
b = 3

print(a / b)   # 3.3333333333333335 (División flotante)
print(a // b)  # 3 (División entera)
print(a % b)   # 1 (Residuo)
print(a ** b)  # 1000 (Potencia)""",
        "total_ejercicios": 3
    },

    "bloque04": {
        "titulo": "Bloque 4: Formateo de Cadenas",
        "concepto": """Manipulación y Estilo de Textos
El formateo de cadenas nos permite construir textos dinámicos insertando variables de manera legible y ordenada.

Métodos de Formateo:
1. Concatenación tradicional utilizando el operador (+).
2. Método clásico `.format()`.
3. f-strings (Formated String Literals): Introducidos en Python 3.6, es la manera moderna, rápida y recomendada por su alta legibilidad.""",
        "ejemplo": """producto = "Laptop"
precio = 799.99

# El método moderno f-string
mensaje = f"El artículo {producto} tiene un costo de ${precio:.2f}"
print(mensaje)""",
        "total_ejercicios": 3
    },

    "bloque05": {
        "titulo": "Bloque 5: Estructuras Condicionales",
        "concepto": """Control de Flujo Lógico
Las estructuras condicionales permiten que el programa tome decisiones y ejecute diferentes bloques de código dependiendo de si una condición se cumple o no.

Palabras Clave:
• `if`: Evalúa la primera condición.
• `elif`: Evalúa condiciones adicionales si las anteriores fueron falsas.
• `else`: Se ejecuta por defecto si ninguna de las condiciones previas fue verdadera.""",
        "ejemplo": """nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")""",
        "total_ejercicios": 3
    },

    "bloque06": {
        "titulo": "Bloque 6: Bucles Iterativos (for)",
        "concepto": """Iteración Definida
El bucle `for` se utiliza para recorrer estructuras secuenciales (como listas, tuplas o diccionarios) o para ejecutar un bloque de código un número determinado de veces.

Función `range()`:
Genera una secuencia numérica controlada. Puede recibir hasta tres parámetros: inicio, fin (no inclusivo) y el paso del incremento.""",
        "ejemplo": """# Imprimir números pares del 2 al 10
for i in range(2, 11, 2):
    print(f"Número: {i}")""",
        "total_ejercicios": 3
    },

    "bloque07": {
        "titulo": "Bloque 7: Bucles de Condición (while)",
        "concepto": """Iteración Indefinida
El bucle `while` ejecuta un bloque de código continuamente **mientras** una condición lógica dada permanezca como verdadera (`True`).

Control de Bucles:
• Es crítico actualizar las variables de control dentro del bucle para evitar bucles infinitos que congelen el servidor.
• `break`: Rompe y sale del bucle inmediatamente.
• `continue`: Salta el resto del código actual y pasa a la siguiente iteración.""",
        "ejemplo": """contador = 1
while contador <= 5:
    print(f"Vuelta {contador}")
    contador += 1  # Incremento de control""",
        "total_ejercicios": 3
    },

    "bloque08": {
        "titulo": "Bloque 8: Listas y Métodos Nativos",
        "concepto": """Estructuras Secuenciales Mutables
Las listas son colecciones ordenadas de elementos que pueden modificarse (mutables). Pueden contener diferentes tipos de datos simultáneamente.

Métodos de Listas Comunes:
• `.append(x)`: Añade un elemento al final.
• `.insert(i, x)`: Inserta un elemento en una posición específica.
• `.remove(x)`: Elimina la primera ocurrencia de un valor.
• `.pop()`: Elimina y retorna el último elemento.""",
        "ejemplo": """frutas = ["Manzana", "Pera"]
frutas.append("Uva")
frutas.insert(1, "Mango")

print(frutas)  # ['Manzana', 'Mango', 'Pera', 'Uva']""",
        "total_ejercicios": 3
    },

    "bloque09": {
        "titulo": "Bloque 9: Tuplas y Sets (Inmutables)",
        "concepto": """Colecciones Especializadas
• Tuplas (`tuple`): Colecciones ordenadas de elementos que **no se pueden modificar** después de su creación (inmutables). Se definen con paréntesis `()`. Ofrecen mayor velocidad y seguridad de datos.
• Conjuntos (`set`): Colecciones no ordenadas de elementos únicos. No permiten duplicados y se definen con llaves `{}`. Ideales para operaciones matemáticas de conjuntos.""",
        "ejemplo": """# Tupla inmutable
mi_tupla = (1, 2, 3)
# mi_tupla[0] = 99  --> Lanza TypeError

# Set sin duplicados
mi_set = {1, 2, 2, 3}
print(mi_set)  # {1, 2, 3}""",
        "total_ejercicios": 3
    },

    "bloque10": {
        "titulo": "Bloque 10: Diccionarios de Datos",
        "concepto": """Estructuras Clave-Valor
Los diccionarios son colecciones indexadas mediante llaves personalizadas (claves) en lugar de índices numéricos. Son mutables y de alta velocidad para búsquedas.

Características:
• Las claves deben ser únicas e inmutables (cadenas, números o tuplas).
• Los valores pueden ser de cualquier tipo de datos, incluyendo listas u otros diccionarios anidados.""",
        "ejemplo": """usuario = {
    "username": "dev123",
    "rol": "admin",
    "puntos": 150
}
print(usuario["username"])  # dev123
usuario["puntos"] += 10    # Modificación""",
        "total_ejercicios": 3
    },

    "bloque11": {
        "titulo": "Bloque 11: Funciones y Argumentos",
        "concepto": """Bloques de Código Reutilizables
Las funciones estructuran el código en unidades lógicas independientes que realizan tareas específicas. Se declaran con la palabra clave `def`.

Parámetros Avanzados:
• Argumentos por defecto: Asignan valores predeterminados.
• `*args`: Permite recibir una cantidad indeterminada de argumentos posicionales como una tupla.
• `**kwargs`: Permite recibir múltiples argumentos de palabras clave como un diccionario.""",
        "ejemplo": """def registrar_usuario(nombre, rol="Invitado"):
    return f"Usuario: {nombre} | Rol: {rol}"

print(registrar_usuario("Ana"))
print(registrar_usuario("Luis", "Admin"))""",
        "total_ejercicios": 3
    },

    "bloque12": {
        "titulo": "Bloque 12: Manejo de Excepciones",
        "concepto": """Control de Errores en Tiempo de Ejecución
El manejo de excepciones evita que una aplicación colapse abruptamente cuando ocurre un error imprevisto (como divisiones por cero o datos inválidos).

Estructura Completa:
• `try`: Código que se va a intentar ejecutar.
• `except`: Captura y maneja un error específico si este ocurre.
• `else`: Se ejecuta solo si el bloque `try` no lanzó ninguna excepción.
• `finally`: Bloque de código que se ejecutará siempre, haya o no error (ideal para cerrar archivos o conexiones).""",
        "ejemplo": """try:
    num = int("hola")
except ValueError:
    print("❌ Error: No se puede convertir texto a número.")
finally:
    print("Limpieza completada.")""",
        "total_ejercicios": 3
    },

    "bloque13": {
        "titulo": "Bloque 13: Decoradores de Código",
        "concepto": """Modificación Dinámica de Funciones
Un decorador es una función que recibe otra función como argumento, le añade alguna funcionalidad extra (como validaciones o registros de logs) y retorna una nueva función modificada sin alterar su código fuente original.

Sintaxis:
Se aplican de forma elegante encima de una función utilizando el símbolo `@` seguido del nombre del decorador.""",
        "ejemplo": """def mi_decorador(funcion_original):
    def envoltura():
        print("Antes de ejecutar...")
        funcion_original()
        print("Después de ejecutar...")
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()""",
        "total_ejercicios": 3
    },

    "bloque14": {
        "titulo": "Bloque 14: Desempaquetado (Unpacking)",
        "concepto": """Extracción Eficiente de Estructuras
El desempaquetado permite asignar elementos de colecciones iterables (como listas o tuplas) directamente a variables individuales en una sola línea de código.

Operadores Especiales:
• Operador asterisco (`*`): Agrupa elementos restantes en una sublista durante el desempaquetado.
• Desempaquetado de Diccionarios (`**`): Útil para fusionar diccionarios o pasar configuraciones masivas.""",
        "ejemplo": """numeros = [1, 2, 3, 4]
a, b, *resto = numeros

print(a)      # 1
print(b)      # 2
print(resto)  # [3, 4]""",
        "total_ejercicios": 3
    },

    "bloque15": {
        "titulo": "Bloque 15: Funciones de Orden Superior",
        "concepto": """Programación Funcional
Las funciones de orden superior son aquellas que pueden recibir otras funciones como argumentos o devolver funciones como resultado.

Herramientas Nativas Clave:
• `lambda`: Declaración abreviada de funciones anónimas en una línea.
• `map(f, iterable)`: Aplica una función a cada elemento de una secuencia.
• `filter(f, iterable)`: Filtra elementos que cumplan una condición lógica.""",
        "ejemplo": """numeros = [1, 2, 3, 4]
# Multiplicar todos los elementos por 2 usando lambda y map
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # [2, 4, 6, 8]""",
        "total_ejercicios": 3
    },

    "bloque16": {
        "titulo": "Bloque 16: Comprensión de Listas",
        "concepto": """Sintaxis Compacta para Colecciones
La comprensión de listas (List Comprehensions) provee una forma elegante y optimizada en rendimiento para crear nuevas listas a partir de iterables existentes.

Ventajas:
• Reduce múltiples líneas de bucles `for` tradicionales a una sola línea.
• Es más veloz en tiempo de procesamiento interno de Python e incorpora condicionales internos de filtrado.""",
        "ejemplo": """# Crear lista de cuadrados de números pares
cuadrados_pares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(cuadrados_pares)  # [4, 16]""",
        "total_ejercicios": 3
    },

    "bloque17": {
        "titulo": "Bloque 17: Manejo de Archivos I/O",
        "concepto": """Persistencia de Datos en Disco
Python permite interactuar con el sistema de archivos del sistema operativo para leer o escribir datos de forma permanente.

Sentencia `with` (Context Manager):
Es el estándar profesional para abrir archivos. Garantiza la liberación segura de recursos del sistema cerrando el archivo de forma automática al finalizar el bloque, incluso si ocurren errores inesperados.""",
        "ejemplo": """# Escritura segura de un archivo de texto
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea guardada en el sistema.")

# El archivo se cierra automáticamente aquí""",
        "total_ejercicios": 3
    },

    "bloque18": {
        "titulo": "Bloque 18: POO Clases y Objetos",
        "concepto": """Estructura Fundamental de Instanciación
La Programación Orientada a Objetos formaliza las plantillas conceptuales mediante clases.

Componentes Críticos:
• `__init__`: El método constructor de la clase. Se ejecuta de forma automática al instanciar un nuevo objeto.
• `self`: Variable de autoreferencia obligatoria que representa al objeto específico que está ejecutando el código actual, permitiendo acceder a sus atributos y métodos particulares.""",
        "ejemplo": """class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad

p1 = Persona("Laura", 22)  # Instanciación de objeto
print(p1.nombre)""",
        "total_ejercicios": 3
    },

    "bloque19": {
        "titulo": "Bloque 19: POO Herencia Avanzada",
        "concepto": """Reutilización de Estructuras Jerárquicas
La herencia permite crear una clase nueva (clase hija) que adopta automáticamente todos los atributos y comportamientos de una clase existente (clase padre).

Función `super()`:
Es una herramienta nativa fundamental que permite invocar de manera limpia y segura los métodos y el constructor de la clase padre desde la clase hija, evitando la duplicación innecesaria de lógica de inicialización.""",
        "ejemplo": """class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Llama al padre
        self.modelo = modelo

mi_auto = Auto("Toyota", "Corolla")
print(mi_auto.marca)  # Acceso heredado""",
        "total_ejercicios": 3
    }
}