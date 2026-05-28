from flask import Blueprint, render_template, request
from app.blueprints.bloque17.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

b17_bp = Blueprint('bloque17', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea un Mixin llamado ValidacionMixin con los métodos validar_nombre(nombre) y validar_edad(edad). Úsalo en una clase SistemaEstudiantes.",
        "codigo_fuente": "class ValidacionMixin:\n    def validar_nombre(self, nombre):\n        if not nombre:\n            raise ValueError('Nombre vacío')\n    def validar_edad(self, edad):\n        if edad < 0:\n            raise ValueError('Edad inválida')\n\nclass SistemaEstudiantes(ValidacionMixin):\n    def registrar(self, nombre, edad):\n        self.validar_nombre(nombre)\n        self.validar_edad(edad)\n        print(f'Registrado: {nombre}, {edad}')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Agrega un PromedioMixin con el método calcular_promedio(notas) e intégralo junto con ValidacionMixin en una clase Sistema.",
        "codigo_fuente": "class PromedioMixin:\n    def calcular_promedio(self, notas):\n        return sum(notas) / len(notas) if notas else 0\n\nclass Sistema(ValidacionMixin, PromedioMixin):\n    pass",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Dada la jerarquía class C(A, B) donde A y B tienen el mismo método metodo(), ¿qué imprime C().metodo()? Explica el MRO.",
        "codigo_fuente": "class A:\n    def metodo(self): print('A')\n\nclass B:\n    def metodo(self): print('B')\n\nclass C(A, B):\n    pass\n\nC().metodo()  # imprime: A",
        "es_interactivo": False
    }
}

@b17_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque17", {})
    return render_template(
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
        bloque_id="bloque17",
        bloque_titulo=info.get("titulo", "Bloque 17"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
 

@b17_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    nombre_web = request.form.get("nombre_input", "Daniel")
                    edad_web   = int(request.form.get("edad_input", 20))
                    ejecutar_ejercicio1(nombre_web, edad_web)
                elif num_ej == 2:
                    notas_crudas = request.form.get("notas_input", "18, 15, 20, 14")
                    notas = [float(x.strip()) for x in notas_crudas.split(",") if x.strip()]
                    nombre_web = request.form.get("nombre_input", "María")
                    edad_web   = int(request.form.get("edad_input", 21))
                    ejecutar_ejercicio2(nombre_web, edad_web, notas)
                elif num_ej == 3:
                    ejecutar_ejercicio3()
            except Exception as e:
                print(f"❌ Error al procesar Mixins: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque17",
        bloque_titulo="Bloque 17: Mixins",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
