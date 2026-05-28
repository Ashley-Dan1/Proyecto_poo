from flask import Blueprint, render_template, request
from app.blueprints.bloque14.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

b14_bp = Blueprint('bloque14', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Toma una lista de números e impleméntale una transformación utilizando la función de orden superior 'map()' junto con una expresión lambda para elevar cada elemento al cuadrado.",
        "codigo_fuente": "numeros = [1, 2, 3, 4]\ncuadrados = list(map(lambda x: x**2, numeros))\nprint(cuadrados)",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Utiliza la función de orden superior 'filter()' para cribar una lista numérica de datos y conservar únicamente aquellos elementos que superen un determinado umbral.",
        "codigo_fuente": "numeros = [5, 12, 7, 20, 3]\nfiltrados = list(filter(lambda x: x > 10, numeros))\nprint(filtrados)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Importa la herramienta 'reduce()' desde el módulo functools y utilízala para calcular el producto multiplicativo acumulado de todos los integrantes de una lista.",
        "codigo_fuente": "from functools import reduce\nnumeros = [1, 2, 3, 4]\nproducto = reduce(lambda acc, x: acc * x, numeros)\nprint(producto)",
        "es_interactivo": True
    }
}

@b14_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque14", {})
    return render_template(
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
        bloque_id="bloque14",
        bloque_titulo=info.get("titulo", "Bloque 14"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
 

@b14_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                # Capturamos y limpiamos la lista de números del formulario web
                entrada_cruda = request.form.get("lista_numeros_input", "1, 2, 3, 4, 5")
                lista_numeros = [float(n.strip()) for n in entrada_cruda.split(",") if n.strip()]
                
                if num_ej == 1:
                    ejecutar_ejercicio1(lista_numeros)
                elif num_ej == 2:
                    umbral_web = float(request.form.get("umbral_input", 10.0))
                    ejecutar_ejercicio2(lista_numeros, umbral_web)
                elif num_ej == 3:
                    ejecutar_ejercicio3(lista_numeros)
            except Exception as e:
                print(f"❌ Error en el procesamiento funcional de colecciones: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque14",
        bloque_titulo="Bloque 14: Funciones de Orden Superior",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
