from flask import Blueprint, render_template, request
from app.blueprints.bloque10.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b10_bp = Blueprint('bloque10', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Implementa una función que calcule y retorne el doble de un número provisto por el usuario.",
        "codigo_fuente": "def doble(x):\n    return x * 2\n\nprint(doble(4))", #[cite: 331]
        "es_interactivo": True
    },
    2: {
        "enunciado": "Desarrolla una función capaz de recibir una cantidad indeterminada de argumentos numéricos usando *args y devuelva su sumatoria.",
        "codigo_fuente": "def sumar_varios(*numeros):\n    return sum(numeros)\n\nprint(sumar_varios(1, 2, 3, 4))", #[cite: 329, 330]
        "es_interactivo": True
    },
    3: {
        "enunciado": "Escribe una función puramente recursiva que calcule el factorial de un número entero 'n' positivo de forma sucesiva.",
        "codigo_fuente": "def factorial(n):\n    if n == 0: return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))", #[cite: 330]
        "es_interactivo": True
    }
}

@b10_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    num_web = float(request.form.get("numero_input", 5.0))
                    ejecutar_ejercicio1(num_web)
                elif num_ej == 2:
                    valores_crudo = request.form.get("args_input", "10, 20, 30, 40")
                    lista_valores = [float(v.strip()) for v in valores_crudo.split(",") if v.strip()]
                    ejecutar_ejercicio2(lista_valores)
                elif num_ej == 3:
                    fact_web = int(request.form.get("factorial_input", 5))
                    ejecutar_ejercicio3(fact_web)
            except Exception as e:
                print(f"❌ Error al procesar subrutinas y funciones: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque10",
        bloque_titulo="Bloque 10: Funciones",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )