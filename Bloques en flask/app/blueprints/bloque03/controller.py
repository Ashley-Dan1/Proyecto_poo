from flask import Blueprint, render_template, request
from app.blueprints.bloque03.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b03_bp = Blueprint('bloque03', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Dados dos números 'a' y 'b', imprime el resultado de todos los operadores aritméticos (+, -, *, /, //, %, **).",
        "codigo_fuente": "print(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)\nprint(a // b)\nprint(a % b)\nprint(a ** b)",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Crea dos listas idénticas y demuestra con código por qué el operador '==' devuelve True pero el operador 'is' devuelve False.",
        "codigo_fuente": "a = [1, 2]\nb = [1, 2]\nprint(a == b)  # True (mismo valor)\nprint(a is b)  # False (distinta memoria RAM)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Evalúa paso a paso la expresión: x = 2 + 1 * 2 % 2 + (2 ** 1) // 2 y explica el orden de precedencia de sus operadores.",
        "codigo_fuente": "# Orden de ejecución en Python:\n# 1. Paréntesis y Potencia (**)\n# 2. Multiplicación (*), Módulo (%) y División Entera (//)\n# 3. Suma (+)",
        "es_interactivo": False
    }
}

@b03_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    # Capturamos los operandos interactivos desde el formulario web
                    a_web = float(request.form.get("valor_a_input", 20))
                    b_web = float(request.form.get("valor_b_input", 4))
                    ejecutar_ejercicio1(a_web, b_web)
                elif num_ej == 2:
                    # Capturamos dos elementos interactivos para rellenar las listas
                    item1 = request.form.get("item1_input", "Objeto1")
                    item2 = request.form.get("item2_input", "Objeto2")
                    ejecutar_ejercicio2(item1, item2)
                elif num_ej == 3:
                    ejecutar_ejercicio3()
            except Exception as e:
                print(f"❌ Error al procesar operaciones en el servidor: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque03",
        bloque_titulo="Bloque 03: Operadores",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )