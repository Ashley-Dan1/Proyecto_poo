from flask import Blueprint, render_template, request
from app.blueprints.bloque15.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

b12_bp = Blueprint('bloque12', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Usa map() para incrementar en 1 cada elemento de una lista. Ejemplo: [2, 4, 6] → [3, 5, 7].",
        "codigo_fuente": "numeros = [2, 4, 6]\nresultado = list(map(lambda x: x + 1, numeros))\nprint(resultado)  # [3, 5, 7]",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Usa filter() para obtener los elementos mayores a 3 de una lista. Ejemplo: [1,2,3,4,5] → [4, 5].",
        "codigo_fuente": "numeros = [1, 2, 3, 4, 5]\nresultado = list(filter(lambda x: x > 3, numeros))\nprint(resultado)  # [4, 5]",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Usa reduce() para multiplicar todos los elementos de una lista. Ejemplo: [1,2,3,4] → 24.",
        "codigo_fuente": "from functools import reduce\nnumeros = [1, 2, 3, 4]\nresultado = reduce(lambda x, y: x * y, numeros)\nprint(resultado)  # 24",
        "es_interactivo": True
    }
}

@b12_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque12", {})
    return render_template(
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
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
                entrada = request.form.get("lista_numeros_input", "1, 2, 3, 4")
                lista   = [float(x.strip()) for x in entrada.split(",") if x.strip()]

                if num_ej == 1:
                    ejecutar_ejercicio1(lista)
                elif num_ej == 2:
                    umbral = float(request.form.get("umbral_input", 3))
                    ejecutar_ejercicio2(lista, umbral)
                elif num_ej == 3:
                    ejecutar_ejercicio3(lista)
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque12",
        bloque_titulo="Bloque 12: Funciones de Orden Superior",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
