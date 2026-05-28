from flask import Blueprint, render_template, request
from app.blueprints.bloque12.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b12_bp = Blueprint('bloque12', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Captura el ValueError que ocurre al intentar convertir un texto no numérico a int. Prueba con un texto válido y uno inválido.",
        "codigo_fuente": "try:\n    n = int(texto)\n    print('Conversión exitosa:', n)\nexcept ValueError as e:\n    print('ValueError:', e)",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Captura el IndexError que ocurre al acceder a un índice fuera de rango en una lista de 3 elementos.",
        "codigo_fuente": "lista = [10, 20, 30]\ntry:\n    print(lista[indice])\nexcept IndexError as e:\n    print('IndexError:', e)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Escribe un try/except que maneje tanto ValueError (texto inválido) como ZeroDivisionError (divisor igual a cero). Incluye un bloque finally.",
        "codigo_fuente": "try:\n    numero = int(texto)\n    resultado = numero / divisor\nexcept ValueError as e:\n    print('ValueError:', e)\nexcept ZeroDivisionError as e:\n    print('ZeroDivisionError:', e)\nfinally:\n    print('finally siempre se ejecuta')",
        "es_interactivo": True
    }
}

@b12_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque12", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque12",
        bloque_titulo=info.get("titulo", "Bloque 12"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )

@b12_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    texto_web = request.form.get("texto_input", "abc")
                    ejecutar_ejercicio1(texto_web)
                elif num_ej == 2:
                    indice_web = int(request.form.get("indice_input", 5))
                    ejecutar_ejercicio2([10, 20, 30], indice_web)
                elif num_ej == 3:
                    texto_web   = request.form.get("texto_num_input", "10")
                    divisor_web = float(request.form.get("divisor_input", 0))
                    ejecutar_ejercicio3(texto_web, divisor_web)
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque12",
        bloque_titulo="Bloque 12: Excepciones (try / except)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
