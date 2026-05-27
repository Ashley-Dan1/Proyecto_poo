# =====================================================================
# BLOQUE 18: PRINCIPIOS DE POO
# (Abstracción, Encapsulamiento, Herencia, Polimorfismo, @property)
# =====================================================================
from abc import ABC, abstractmethod

# ---------------------------------------------------------------------
# EJERCICIO 1: Clase abstracta Figura + Triangulo concreto.
# ---------------------------------------------------------------------
class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base   = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2


class GestorFiguraAbstracta:
    @staticmethod
    def ejecutar_demostracion(base: float, altura: float):
        print("🔷 ABSTRACCIÓN — Clase abstracta Figura + Triangulo")
        print("--------------------------------------------------")
        print("Figura es abstracta: no se puede instanciar directamente.")
        try:
            Figura()
        except TypeError as e:
            print(f"❌ Intentar instanciar Figura() → {e}\n")

        t = Triangulo(base, altura)
        print(f"✅ Triangulo creado → base={t.base}, altura={t.altura}")
        print(f"➡️ Área = (base × altura) / 2 = {t.area()}")


# ---------------------------------------------------------------------
# EJERCICIO 2: @property con setter — validar precio >= 0.
# ---------------------------------------------------------------------
class Producto:
    def __init__(self, nombre: str):
        self.nombre   = nombre
        self.__precio = 0.0

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor

    def mostrar(self):
        print(f"📦 Producto: {self.nombre} | Precio: ${self.__precio}")


class GestorProperty:
    @staticmethod
    def ejecutar_calculo(nombre: str, precio: float):
        print("🔐 ENCAPSULAMIENTO + @property — Producto con setter validado")
        print("--------------------------------------------------")
        p = Producto(nombre)
        try:
            p.precio = precio
            p.mostrar()
        except ValueError as e:
            print(f"❌ Setter rechazó el valor: {e}")
        print("\nProbando con precio negativo (-50)...")
        try:
            p.precio = -50
        except ValueError as e:
            print(f"❌ Setter rechazó -50: {e}")


# ---------------------------------------------------------------------
# EJERCICIO 3: Polimorfismo — Animal → Perro, Gato, Vaca.
# ---------------------------------------------------------------------
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        print(f"🐶 {self.nombre} ladra: ¡Guau!")


class Gato(Animal):
    def sonido(self):
        print(f"🐱 {self.nombre} maulla: ¡Miau!")


class Vaca(Animal):
    def sonido(self):
        print(f"🐄 {self.nombre} muge: ¡Muuu!")


class GestorPolimorfismo:
    @staticmethod
    def ejecutar_analisis(nombre_perro: str, nombre_gato: str, nombre_vaca: str):
        print("🧬 POLIMORFISMO — Animal → Perro, Gato, Vaca")
        print("--------------------------------------------------")
        animales = [
            Perro(nombre_perro),
            Gato(nombre_gato),
            Vaca(nombre_vaca)
        ]
        print("Recorriendo lista de animales y llamando a sonido():\n")
        for animal in animales:
            animal.sonido()
        print("\n💡 Mismo método sonido(), comportamiento diferente en cada clase.")


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1(base, altura):
    GestorFiguraAbstracta.ejecutar_demostracion(base, altura)

def ejecutar_ejercicio2(nombre, precio):
    GestorProperty.ejecutar_calculo(nombre, precio)

def ejecutar_ejercicio3(nombre_perro, nombre_gato, nombre_vaca):
    GestorPolimorfismo.ejecutar_analisis(nombre_perro, nombre_gato, nombre_vaca)