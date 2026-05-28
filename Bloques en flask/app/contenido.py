# app/contenido.py
# Contenido del compendio oficial — 20 bloques alineados al PDF

COMPENDIO = {

    "bloque00": {
        "titulo": "Bloque 00: Introducción a la POO",
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
• Escalabilidad: el sistema puede crecer sin volverse caótico.
• Mantenimiento: más fácil modificar una clase específica.
• Modelado real: representar el mundo real en código.
• Base para frameworks: Django, Flask, Spring, .NET usan POO intensivamente.

Diferencia con Programación Estructurada
Estructurada → todo son funciones sueltas: def registrar_cliente(): pass
POO → todo organizado en objetos: class Cliente: def registrar(self): pass""",
        "ejemplo": """class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

cli = Cliente("Daniel")  # cli es el OBJETO
print(cli.nombre)        # Daniel""",
        "total_ejercicios": 3
    },

    "bloque01": {
        "titulo": "Bloque 01: El Constructor __init__",
        "concepto": """¿Qué es el constructor?
El constructor es un método especial que se ejecuta automáticamente cuando se crea un objeto. En Python se escribe __init__ (doble guion bajo).
Su propósito es inicializar el objeto dejándolo preparado con sus datos iniciales.

¿Qué es self?
self representa al objeto actual. Permite guardar atributos dentro de ese objeto específico, por eso cada instancia puede tener sus propios valores.

Constructor con validación
El constructor puede validar datos, evitando crear objetos con valores inválidos.

Parámetros por defecto
Se pueden definir valores por defecto en los parámetros del constructor.

Constructor alternativo con @classmethod
Permite crear objetos desde estructuras como diccionarios, sin llamar directamente a __init__.

Puntos clave
• __init__ inicializa objetos al momento de crearse.
• Se ejecuta automáticamente; no hay que llamarlo.
• Usa self para guardar atributos dentro del objeto.
• No retorna valores.
• Puede recibir parámetros y definir valores por defecto.
• Puede validar datos antes de guardarlos.
• Si no se define, Python crea uno vacío internamente.""",
        "ejemplo": """class Producto:
    def __init__(self, nombre, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.nombre = nombre
        self.precio = precio

p = Producto("Laptop", 900)   # OK
# p = Producto("Mouse", -10) # ValueError""",
        "total_ejercicios": 4
    },

    "bloque02": {
        "titulo": "Bloque 02: Variables y Tipos de Datos",
        "concepto": """Tipos simples
• int: 19, -5, 0
• float: 3.14, -2.5
• str: "Hola", "Python"
• bool: True, False
• None: ausencia de valor

Tipos complejos
• list — colección ordenada y mutable: [1, 2, 3, "python"]
• tuple — colección inmutable: (1, "hello", 3.14)
• dict — pares clave-valor: {"nombre": "Juan", "edad": 25}
• set — elementos únicos sin orden: {1, 2, 3}

Acceso por índice
Python cuenta desde 0: posición 0 = primer elemento, -1 = último elemento.

Slicing (rebanado)
Sintaxis: [inicio:fin] → incluye inicio, NO incluye fin.""",
        "ejemplo": """lista = [1, 2, 3, 4, 5]
print(lista[0])    # 1  (primero)
print(lista[-1])   # 5  (último)
print(lista[1:4])  # [2, 3, 4]

cadena = "Hello World"
print(cadena[0])    # H
print(cadena[0:5])  # Hello""",
        "total_ejercicios": 3
    },

    "bloque03": {
        "titulo": "Bloque 03: Operadores",
        "concepto": """Operadores Aritméticos
+ → suma       - → resta        * → multiplicación
/ → división   // → división entera    % → módulo / residuo    ** → potencia

Operadores de Comparación
== → igual     != → diferente     > → mayor     < → menor
>= → mayor o igual     <= → menor o igual

Operadores Lógicos
and → ambas condiciones verdaderas
or  → al menos una condición verdadera
not → invierte el resultado

CONCEPTO CLAVE: == vs is
== compara el VALOR (contenido).
is compara la REFERENCIA en memoria (¿es el mismo objeto?).

Precedencia de operadores (de mayor a menor)
1° (mayor) → **
2° → *, /, //, %
3° → +, -
4° → ==, !=, >, <, >=, <=
5° → not
6° → and
7° (menor) → or""",
        "ejemplo": """a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True  → mismo contenido
print(a is b)  # False → objetos distintos en memoria
print(a is c)  # True  → misma referencia""",
        "total_ejercicios": 3
    },

    "bloque04": {
        "titulo": "Bloque 04: Entrada y Salida (input / print)",
        "concepto": """print()
Muestra información en pantalla. Admite f-strings, sep y end.

input()
Lee datos del usuario. ⚠ SIEMPRE devuelve str (texto).

Casting (conversión de tipos)
int()   → convierte a entero
float() → convierte a decimal
str()   → convierte a texto

Error común
Sin convertir: edad = input("Edad: ")
print(edad + 5)  → ❌ ERROR: str + int

Con conversión: edad = int(input("Edad: "))
print(edad + 5)  → ✓ OK: int + int""",
        "ejemplo": """nombre = "Ana"
edad   = 25
print(f"Nombre: {nombre}, Edad: {edad}")
print("Python", "Java", sep=" → ", end="!\\n")

# Simulando input
nombre = "Carlos"
edad   = int("30")
print(f"Hola {nombre}, tienes {edad} años.")""",
        "total_ejercicios": 3
    },

    "bloque05": {
        "titulo": "Bloque 05: Condicionales (if / elif / else)",
        "concepto": """Estructura básica
if condicion:
    # se ejecuta si es verdadera
elif otra_condicion:
    # si la anterior era falsa y esta verdadera
else:
    # si ninguna fue verdadera

Operador ternario
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

match-case (Python 3.10+)
Permite comparar un valor contra múltiples patrones de forma limpia.

Evaluación corta (short-circuit)
Si la primera condición de un and es False, Python NO evalúa la segunda. Optimiza rendimiento.""",
        "ejemplo": """nota = 85
if nota >= 90:   print("A")
elif nota >= 80: print("B")
elif nota >= 70: print("C")
else:            print("D")

# Operador ternario
numero = 15
resultado = "Par" if numero % 2 == 0 else "Impar"
print(resultado)  # Impar""",
        "total_ejercicios": 3
    },

    "bloque06": {
        "titulo": "Bloque 06: Bucles (for / while)",
        "concepto": """while
Ejecuta un bloque mientras una condición sea verdadera.

for con range()
Itera sobre una secuencia numérica controlada.
range(5) → 0,1,2,3,4
range(0, 10, 2) → 0,2,4,6,8 (paso 2)

for sobre colecciones
Recorre listas, tuplas y diccionarios directamente.

enumerate()
Devuelve pares (índice, elemento) en cada iteración.

break y continue
break: termina el bucle completamente.
continue: salta la iteración actual y pasa a la siguiente.

List Comprehension
Sintaxis compacta para crear listas:
[expresión for elemento in iterable if condición]""",
        "ejemplo": """# while
contador = 1
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1

# enumerate
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# list comprehension
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]""",
        "total_ejercicios": 3
    },

    "bloque07": {
        "titulo": "Bloque 07: Funciones",
        "concepto": """Estructura básica
def nombre_funcion(parametros):
    return valor

Parámetros por defecto y retorno múltiple
Los parámetros pueden tener valores predeterminados.
Una función puede retornar múltiples valores como tupla.

*args y **kwargs
*args   → múltiples argumentos posicionales (se empaquetan en tupla).
**kwargs → múltiples argumentos con nombre (se empaquetan en dict).

Funciones lambda
Funciones anónimas de una sola línea.
cuadrado = lambda x: x**2

Recursividad
Una función que se llama a sí misma. Siempre debe tener un caso base para detener la recursión.""",
        "ejemplo": """def sumar_varios(*numeros):
    return sum(numeros)

print(sumar_varios(1, 2, 3, 4))  # 10

def factorial(n):
    if n == 0: return 1         # caso base
    return n * factorial(n - 1) # llamada recursiva

print(factorial(5))  # 120""",
        "total_ejercicios": 3
    },

    "bloque08": {
        "titulo": "Bloque 08: Listas",
        "concepto": """Métodos principales
append(x)  → agregar al final
extend(L)  → agregar múltiples elementos
insert(i,x)→ insertar en posición i
pop()      → eliminar y retornar el último
remove(x)  → eliminar primera ocurrencia de x
sort()     → ordenar in-place
reverse()  → invertir in-place
clear()    → vaciar la lista
copy()     → copia superficial
count(x)   → contar ocurrencias de x
index(x)   → posición de x

Funciones integradas sobre listas
len(), sum(), max(), min(), sorted()

CONCEPTO CLAVE — referencia vs copia
Asignar una lista a otra variable NO crea una copia, crea otra referencia al mismo objeto.
Usar .copy() para obtener un objeto independiente.""",
        "ejemplo": """nums = [10, 5, 8, 1, 9]
print(sum(nums))     # 33
print(max(nums))     # 10
print(sorted(nums))  # [1, 5, 8, 9, 10] — no modifica original
nums.sort()          # [1, 5, 8, 9, 10] — sí modifica original

lista      = [1, 2, 3]
copia_ref  = lista         # misma referencia
copia_real = lista.copy()  # objeto nuevo
copia_ref.append(4)
print(lista)       # [1, 2, 3, 4] ← también cambió
print(copia_real)  # [1, 2, 3]    ← no cambió""",
        "total_ejercicios": 3
    },

    "bloque09": {
        "titulo": "Bloque 09: Tuplas",
        "concepto": """Concepto
Las tuplas son INMUTABLES: no se pueden modificar tras crearse.
Son más rápidas que las listas y se usan cuando los datos no deben cambiar.

Métodos disponibles
count(x) → contar ocurrencias de x
index(x) → posición de x

Unpacking (desempaquetado)
Permite asignar elementos de una tupla a variables individuales.
primero, *resto, ultimo = (1, 2, 3, 4, 5)

Conversión
Para modificar una tupla: convertirla a lista, modificar y volver a convertir.""",
        "ejemplo": """tupla = (1, 2, 3)
# tupla[0] = 10  → ❌ TypeError: inmutable

# Unpacking
a, b, c = (1, 2, 3)
primero, *resto, ultimo = (1, 2, 3, 4, 5)
# primero=1, resto=[2,3,4], ultimo=5

# Recorrer coordenadas
coordenadas = [(1,2), (3,4)]
for x, y in coordenadas:
    print(f"x={x}, y={y}")""",
        "total_ejercicios": 3
    },

    "bloque10": {
        "titulo": "Bloque 10: Diccionarios",
        "concepto": """Concepto
Estructura de pares clave:valor. Base de JSON, APIs, configuraciones.

Acceso y modificación
persona["nombre"]              → acceso directo
persona.get("telefono", "N/A") → acceso seguro con valor por defecto
persona["edad"] = 26           → modificar
del persona["telefono"]        → eliminar

Métodos útiles
.keys(), .values(), .items(), .update(), .copy()

Dict comprehension y anidados
{x: x**2 for x in range(5)} → {0:0, 1:1, 2:4, 3:9, 4:16}

Diccionarios anidados
Pueden contener otros diccionarios como valores.""",
        "ejemplo": """persona = {"nombre": "Juan", "edad": 25}

print(persona["nombre"])              # Juan
print(persona.get("telefono", "N/A")) # N/A

for clave, valor in persona.items():
    print(clave, "→", valor)

cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # {0:0, 1:1, 2:4, 3:9, 4:16}""",
        "total_ejercicios": 3
    },

    "bloque11": {
        "titulo": "Bloque 11: Conjuntos (set)",
        "concepto": """Concepto
• Sin duplicados, sin orden garantizado.
• Muy útil para eliminar repetidos y operaciones matemáticas.

Operaciones matemáticas
Unión          |  ó .union()
Intersección   &  ó .intersection()
Diferencia     -  ó .difference()
Dif. simétrica ^  ó .symmetric_difference()

Métodos
add(x)     → agregar elemento
remove(x)  → eliminar; lanza KeyError si no existe
discard(x) → eliminar; sin error si no existe
pop()      → eliminar y retornar aleatorio""",
        "ejemplo": """A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A & B)  # {3, 4}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 5, 6}

# Eliminar duplicados de una lista
lista    = [1, 2, 2, 3, 3, 3]
sin_dup  = list(set(lista))
print(sin_dup)  # [1, 2, 3]""",
        "total_ejercicios": 3
    },

    "bloque12": {
        "titulo": "Bloque 12: Excepciones (try / except)",
        "concepto": """Estructura completa
try:
    # código que puede fallar
except TipoError as e:
    # manejar el error
else:
    # se ejecuta si NO hubo error
finally:
    # se ejecuta SIEMPRE

Tipos de error comunes
ValueError        → valor inválido (ej. int("abc"))
TypeError         → tipo incorrecto (str + int)
IndexError        → índice fuera de rango
KeyError          → clave no existe en dict/set
ZeroDivisionError → división por cero
FileNotFoundError → archivo no encontrado

raise manual
Permite lanzar un error personalizado: raise ValueError("Edad inválida")

assert
Verifica una condición; si es falsa lanza AssertionError.""",
        "ejemplo": """try:
    n = int("abc")
except ValueError as e:
    print("Error de conversión:", e)

def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad inválida")
    return edad

class MiError(Exception):
    pass""",
        "total_ejercicios": 3
    },

    "bloque13": {
        "titulo": "Bloque 13: Decoradores",
        "concepto": """Concepto
Un decorador es una función que recibe otra función, modifica su comportamiento y retorna una nueva función.
Se aplica con @nombre_decorador antes de la función que se quiere decorar.

Estructura
def mi_decorador(funcion_original):
    def wrapper(*args, **kwargs):
        # código antes
        resultado = funcion_original(*args, **kwargs)
        # código después
        return resultado
    return wrapper

Usos reales
• Validar datos antes de ejecutar.
• Controlar acceso (autenticación en Django/Flask).
• Registrar logs de ejecución.
• Medir tiempo de ejecución.""",
        "ejemplo": """def mi_decorador(f):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar")
        resultado = f(*args, **kwargs)
        print("Después de ejecutar")
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("Hola mundo")

saludar()
# Antes de ejecutar
# Hola mundo
# Después de ejecutar""",
        "total_ejercicios": 3
    },

    "bloque14": {
        "titulo": "Bloque 14: Unpacking (Desempaquetado)",
        "concepto": """Concepto
Unpacking = extraer valores de una estructura y asignarlos a variables individuales.

Básico
a, b = [1, 2]
a, b, c = (1, 2, 3)

Con operador *
primero, *resto, ultimo = [1, 2, 3, 4, 5]
# primero=1, resto=[2,3,4], ultimo=5

En funciones
def suma(a, b, c): return a + b + c
numeros = [1, 2, 3]
suma(*numeros)  # equivale a suma(1, 2, 3)

Combinar diccionarios con **
dict1 = {"a": 1}
dict2 = {"b": 2}
combinado = {**dict1, **dict2}  # {"a":1, "b":2}""",
        "ejemplo": """primera, *mitad, ultima = (10, 20, 30, 40)
print(primera)  # 10
print(mitad)    # [20, 30]
print(ultima)   # 40

coordenadas = [(1,2), (3,4), (5,6)]
for x, y in coordenadas:
    print(f"x={x}, y={y}")""",
        "total_ejercicios": 3
    },

    "bloque15": {
        "titulo": "Bloque 15: Funciones de Orden Superior",
        "concepto": """Concepto
Una función de orden superior recibe otra función como parámetro o devuelve una función.

map()
Aplica una función a cada elemento de una colección.
list(map(lambda x: x**2, [1,2,3,4])) → [1, 4, 9, 16]

filter()
Filtra elementos según condición (True/False).
list(filter(lambda x: x % 2 == 0, [1,2,3,4])) → [2, 4]

reduce()
Reduce la colección a un único valor acumulado.
from functools import reduce
reduce(lambda x, y: x + y, [1,2,3,4]) → 10""",
        "ejemplo": """from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

# Cuadrado de los pares
resultado = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numeros))
)
print(resultado)  # [4, 16, 36]

# Producto total con reduce
producto = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(producto)  # 24""",
        "total_ejercicios": 3
    },

    "bloque16": {
        "titulo": "Bloque 16: Archivos y JSON",
        "concepto": """Modos de apertura
"r" → lectura
"w" → escritura (sobrescribe)
"a" → append — agrega al final
"x" → crear; error si ya existe

Lectura y escritura de texto
La sentencia with garantiza el cierre automático del archivo.

JSON
import json
json.dump(datos, f, indent=2)  → guardar
json.load(f)                   → cargar

Permite guardar y cargar estructuras Python (dicts, listas) como archivos de texto estructurado.""",
        "ejemplo": """import json

# Guardar JSON
datos = {"nombre": "Juan", "edad": 25, "activo": True}
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)

# Cargar JSON
with open("datos.json", "r") as f:
    cargado = json.load(f)
print(cargado["nombre"])  # Juan""",
        "total_ejercicios": 3
    },

    "bloque17": {
        "titulo": "Bloque 17: Mixins",
        "concepto": """Concepto
Un Mixin es una clase que NO se usa sola. Se diseña para agregar funcionalidad a otras clases mediante herencia, evitando duplicar código.
Regla: si una clase es un Mixin, su nombre suele terminar en Mixin.

Uso
class MiClase(MixinA, MixinB):
    ...

MRO — Orden de Resolución de Métodos
Python busca los métodos de izquierda a derecha en la lista de herencia.
class C(A, B): → Python busca en C → A → B → object""",
        "ejemplo": """class ValidacionMixin:
    def validar_nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre vacío")
    def validar_edad(self, edad):
        if edad < 0:
            raise ValueError("Edad inválida")

class SistemaEstudiantes(ValidacionMixin):
    def __init__(self):
        self.estudiantes = []
    def registrar(self, nombre, edad):
        self.validar_nombre(nombre)
        self.validar_edad(edad)
        self.estudiantes.append({"nombre": nombre, "edad": edad})

sistema = SistemaEstudiantes()
sistema.registrar("Daniel", 20)""",
        "total_ejercicios": 3
    },

    "bloque18": {
        "titulo": "Bloque 18: Principios de POO y Conceptos Avanzados",
        "concepto": """1. Abstracción
Mostrar lo esencial y ocultar lo innecesario.

2. Encapsulamiento
Proteger los datos controlando el acceso a los atributos.
Atributo privado con doble guion bajo: self.__saldo

3. Herencia
Una clase hija reutiliza atributos y métodos de la clase padre.
class Cliente(Persona): super().__init__(nombre)

4. Polimorfismo
El mismo método se comporta diferente en cada subclase.

5. Property (getters y setters)
@property → getter (leer atributo)
@atributo.setter → setter con validación

6. Clases Abstractas e Interfaces
from abc import ABC, abstractmethod
Obligan a las subclases a implementar métodos específicos.""",
        "ejemplo": """from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self): pass

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base, self.altura = base, altura
    def area(self):
        return (self.base * self.altura) / 2

class Cuenta:
    def __init__(self):
        self.__saldo = 0  # privado
    def depositar(self, valor):
        self.__saldo += valor
    def ver_saldo(self):
        return self.__saldo""",
        "total_ejercicios": 3
    },

    "bloque19": {
        "titulo": "Bloque 19: Relaciones UML en Código",
        "concepto": """Resumen de Relaciones
Asociación  → una clase USA otra
              Código típico: Venta(cliente)

Agregación  → una clase CONTIENE objetos externos
              Código típico: carrito.agregar(producto)

Composición → una clase CREA objetos internamente
              Código típico: self.detalles.append(Detalle(...))

Herencia    → una clase ES una especialización
              Código típico: class Cliente(Persona)

Interfaz    → una clase CUMPLE un contrato
              Código típico: class Venta(ICrud)""",
        "ejemplo": """class Venta(ICrud):           # INTERFAZ
    def __init__(self, cliente):  # AGREGACIÓN
        self.cliente  = cliente
        self.detalles = []

    def agregar(self, producto, cantidad):
        self.detalles.append(           # COMPOSICIÓN
            DetalleVenta(producto, cantidad))

    def crear(self, emp):
        print("Empresa:", emp.razonsocial)  # ASOCIACIÓN

class Cliente(Persona):  # HERENCIA
    pass""",
        "total_ejercicios": 3
    }
}
