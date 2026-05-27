# =====================================================================
# BLOQUE 19: RELACIONES UML EN CÓDIGO
# =====================================================================
from abc import ABC, abstractmethod

# ── Interfaces y clases base ──────────────────────────────────────────
class ICrud(ABC):
    @abstractmethod
    def crear(self): pass

class Empresa:
    def __init__(self, nombre: str):
        self.razonsocial = nombre

class Persona:
    def __init__(self, id_: str, nombre: str):
        self.id     = id_
        self.nombre = nombre

# ---------------------------------------------------------------------
# EJERCICIO 1: Identificar relaciones en el ejemplo integrado.
# ---------------------------------------------------------------------
class Cliente(Persona):          # HERENCIA
    def __init__(self, id_: str, nombre: str, correo: str):
        super().__init__(id_, nombre)
        self.correo = correo

class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class DetalleVenta:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto  = producto
        self.cantidad  = cantidad

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad

class Venta(ICrud):              # INTERFAZ
    def __init__(self, cliente: Cliente):   # AGREGACIÓN
        self.cliente  = cliente
        self.detalles = []

    def agregar(self, producto: Producto, cantidad: int):
        self.detalles.append(DetalleVenta(producto, cantidad))  # COMPOSICIÓN

    def crear(self, empresa: Empresa):      # ASOCIACIÓN
        print(f"🏢 Empresa     : {empresa.razonsocial}")
        print(f"👤 Cliente     : {self.cliente.nombre}")
        for d in self.detalles:
            print(f"   📦 {d.producto.nombre} x{d.cantidad} → ${d.subtotal()}")
        print(f"💰 Total       : ${self.total()}")

    def total(self) -> float:
        return sum(d.subtotal() for d in self.detalles)

    def listar(self):     pass
    def actualizar(self): pass
    def eliminar(self):   pass


class GestorRelacionesUML:
    @staticmethod
    def ejecutar_demostracion():
        print("🗺️ RELACIONES UML — Ejemplo integrado")
        print("--------------------------------------------------")
        print("Relaciones presentes:")
        print("  • Herencia   → Cliente ES una Persona")
        print("  • Interfaz   → Venta CUMPLE ICrud")
        print("  • Agregación → Venta RECIBE un Cliente externo")
        print("  • Composición→ Venta CREA sus propios DetalleVenta")
        print("  • Asociación → Venta USA una Empresa en crear()\n")

        emp   = Empresa("SuperMaxi")
        cli   = Cliente("001", "Daniel", "d@mail.com")
        p1    = Producto("P01", "Laptop", 900.0)
        p2    = Producto("P02", "Mouse",  25.0)
        venta = Venta(cli)
        venta.agregar(p1, 1)
        venta.agregar(p2, 2)
        venta.crear(emp)


# ---------------------------------------------------------------------
# EJERCICIO 2: Empleado hereda de Persona — relación de Herencia.
# ---------------------------------------------------------------------
class Empleado(Persona):
    def __init__(self, nombre: str, salario: float):
        super().__init__("EMP-AUTO", nombre)
        self.salario = salario

    def mostrar(self):
        print(f"👔 Empleado: {self.nombre} | Salario: ${self.salario}")
        print(f"   (hereda id y nombre de Persona → Herencia)")


class GestorEmpleado:
    @staticmethod
    def ejecutar_calculo(nombre: str, salario: float):
        print("👔 HERENCIA — Empleado ES una Persona")
        print("--------------------------------------------------")
        e = Empleado(nombre, salario)
        e.mostrar()
        print(f"\n✅ Relación UML: HERENCIA")
        print("   Empleado extiende Persona: reutiliza id y nombre,")
        print("   y agrega el atributo propio salario.")


# ---------------------------------------------------------------------
# EJERCICIO 3: Factura con composición hacia DetalleFactura.
# ---------------------------------------------------------------------
class DetalleFactura:
    def __init__(self, descripcion: str, valor: float):
        self.descripcion = descripcion
        self.valor       = valor


class Factura:
    def __init__(self):
        self.detalles = []   # Factura CREA y POSEE sus detalles → COMPOSICIÓN

    def agregar_detalle(self, descripcion: str, valor: float):
        self.detalles.append(DetalleFactura(descripcion, valor))

    def total(self) -> float:
        return sum(d.valor for d in self.detalles)

    def mostrar(self):
        print("🧾 COMPOSICIÓN — Factura contiene DetalleFactura")
        print("--------------------------------------------------")
        for i, d in enumerate(self.detalles, 1):
            print(f"  [{i}] {d.descripcion}: ${d.valor}")
        print(f"\n💰 Total: ${self.total()}")
        print("\n💡 Composición: DetalleFactura solo existe dentro de Factura.")
        print("   Si se destruye la factura, los detalles también desaparecen.")


class GestorFactura:
    @staticmethod
    def ejecutar_analisis(detalles: list):
        factura = Factura()
        for desc, valor in detalles:
            factura.agregar_detalle(desc, valor)
        factura.mostrar()


# =====================================================================
# FUNCIONES DISPARADORAS
# =====================================================================
def ejecutar_ejercicio1():
    GestorRelacionesUML.ejecutar_demostracion()

def ejecutar_ejercicio2(nombre, salario):
    GestorEmpleado.ejecutar_calculo(nombre, salario)

def ejecutar_ejercicio3(detalles):
    GestorFactura.ejecutar_analisis(detalles)