from flask import Blueprint, render_template, request
from app.blueprints.bloque01.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3, ejecutar_ejercicio4
)
from app.contenido import COMPENDIO

b01_bp = Blueprint('bloque01', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea la clase Producto con código, nombre y precio. Instancia 2 productos.",
        "codigo_fuente": "class ProductoSimple:\n    def __init__(self, codigo, nombre, precio):\n        self.codigo = codigo\n        self.nombre = nombre\n        self.precio = precio",
        "es_interactivo": False
    },
    2: {
        "enunciado": "Agrega validación para que el precio no sea negativo.",
        "codigo_fuente": "if precio < 0:\n    raise ValueError('El precio no puede ser un valor negativo')",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Crea Estudiante con nombre y notas=None. Si no hay notas, inicia lista vacía.",
        "codigo_fuente": "if notas is None:\n    self.notas = []\nelse:\n    self.notas = notas",
        "es_interactivo": True
    },
    4: {
        "enunciado": "Agrega un @classmethod desde_diccionario que cree un Estudiante desde un dict.",
        "codigo_fuente": "@classmethod\ndef desde_diccionario(cls, datos):\n    return cls(datos['nombre'], datos.get('notas', []))",
        "es_interactivo": True
    }
}


@b01_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque01", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque01",
        bloque_titulo=info.get("titulo", "Bloque 01"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b01_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    precio_str = request.form.get("precio_input", "").strip()
                    if precio_str == "":
                        print("⚠️ Debes ingresar un precio en el campo interactivo.")
                    else:
                        precio_web = float(precio_str)
                        ejecutar_ejercicio2(precio_web)

                elif num_ej == 3:
                    nombre_web = request.form.get("nombre_input", "").strip()
                    if nombre_web == "":
                        print("⚠️ Debes ingresar un nombre en el campo interactivo.")
                    else:
                        modo_notas = request.form.get("modo_notas") == "con_notas"
                        ejecutar_ejercicio3(nombre_web, modo_notas)

                elif num_ej == 4:
                    nombre_web = request.form.get("nombre_dict_input", "").strip()
                    if nombre_web == "":
                        print("⚠️ Debes ingresar un nombre en el campo interactivo.")
                    else:
                        ejecutar_ejercicio4(nombre_web)

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque01",
        bloque_titulo="Bloque 01: El Constructor __init__",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
