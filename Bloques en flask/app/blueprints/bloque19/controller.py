from flask import Blueprint, render_template, request
from app.blueprints.bloque19.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b19_bp = Blueprint('bloque19', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Identifica y nombra todas las relaciones UML del ejemplo integrado: Venta usa Cliente (asociación), Venta contiene DetalleVenta (composición), Venta recibe cliente externo (agregación), Cliente hereda de Persona (herencia) y Venta implementa ICrud (interfaz).",
        "codigo_fuente": "class Venta(ICrud):        # interfaz\n    def __init__(self, cliente):  # agregación\n        self.cliente = cliente\n        self.detalles = []\n\n    def agregar(self, producto, cantidad):\n        self.detalles.append(          # composición\n            DetalleVenta(producto, cantidad))\n\n    def crear(self, emp):              # asociación\n        print('Empresa:', emp.razonsocial)",
        "es_interactivo": False
    },
    2: {
        "enunciado": "Agrega la clase Empleado que herede de Persona con un atributo salario. Identifica qué relación UML representa.",
        "codigo_fuente": "class Empleado(Persona):  # HERENCIA\n    def __init__(self, id, nombre, salario):\n        super().__init__(id, nombre)\n        self.salario = salario",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Crea la clase Factura con composición hacia DetalleFactura: la factura crea y destruye sus propios detalles internamente.",
        "codigo_fuente": "class DetalleFactura:\n    def __init__(self, descripcion, valor):\n        self.descripcion = descripcion\n        self.valor = valor\n\nclass Factura:\n    def __init__(self):\n        self.detalles = []\n\n    def agregar_detalle(self, desc, valor):\n        self.detalles.append(DetalleFactura(desc, valor))\n\n    def total(self):\n        return sum(d.valor for d in self.detalles)",
        "es_interactivo": True
    }
}

@b19_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1

    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        import io, contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                if num_ej == 1:
                    ejecutar_ejercicio1()
                elif num_ej == 2:
                    nombre_web = request.form.get("nombre_input", "Laura")
                    salario_web = float(request.form.get("salario_input", 1500.0))
                    ejecutar_ejercicio2(nombre_web, salario_web)
                elif num_ej == 3:
                    desc1 = request.form.get("desc1_input", "Laptop")
                    val1  = float(request.form.get("val1_input", 900.0))
                    desc2 = request.form.get("desc2_input", "Mouse")
                    val2  = float(request.form.get("val2_input", 25.0))
                    ejecutar_ejercicio3([(desc1, val1), (desc2, val2)])
            except Exception as e:
                print(f"❌ Error al procesar relaciones UML: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque19",
        bloque_titulo="Bloque 19: Relaciones UML en Código",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )