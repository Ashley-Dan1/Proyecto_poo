from flask import Blueprint, render_template, request
from app.blueprints.bloque12.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b12_bp = Blueprint('bloque12', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Implementa un decorador personalizado que imprima una traza de inicialización antes de disparar el método núcleo de la clase.",
        "codigo_fuente": "def log(f):\n    def w(*a):\n        print('Iniciando...')\n        return f(*a)\n    return w",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Diseña un decorador de validación matemática que evalúe si el argumento numérico provisto es positivo antes de calcular su potencia al cuadrado.",
        "codigo_fuente": "@verificar_positivo\ndef cuadrado(n):\n    return n ** 2",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Analiza la trazabilidad y salida en consola producida por el decorador de logs al interceptar una suma aritmética ordinaria.",
        "codigo_fuente": "@log\ndef suma(a, b):\n    return a + b\n\nsuma(2, 3)",
        "es_interactivo": True
    }
}

@b12_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
        
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                if num_ej == 1:
                    texto_web = request.form.get("texto_decorador", "Procesando Datos de Nómina")
                    ejecutar_ejercicio1(texto_web)
                elif num_ej == 2:
                    num_web = float(request.form.get("numero_positivo", 5.0))
                    ejecutar_ejercicio2(num_web)
                elif num_ej == 3:
                    val_a = float(request.form.get("valor_a", 2.0))
                    val_b = float(request.form.get("valor_b", 3.0))
                    ejecutar_ejercicio3(val_a, val_b)
            except Exception as e:
                print(f"❌ Error en la interceptación del decorador: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque12",
        bloque_titulo="Bloque 12: Decoradores",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )