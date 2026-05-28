from flask import Blueprint, render_template, request
from app.blueprints.bloque11.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b11_bp = Blueprint('bloque11', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea dos conjuntos A y B y calcula su unión, intersección y diferencia.",
        "codigo_fuente": "A = {1, 2, 3, 4}\nB = {3, 4, 5, 6}\nprint(A | B)  # unión\nprint(A & B)  # intersección\nprint(A - B)  # diferencia",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Elimina los duplicados de la lista [1, 2, 2, 3, 3, 3, 4] usando set y convierte el resultado de vuelta a lista.",
        "codigo_fuente": "lista = [1, 2, 2, 3, 3, 3, 4]\nsin_dup = list(set(lista))\nprint(sin_dup)  # [1, 2, 3, 4]",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Calcula (A | B) - (A & B) y explica el resultado. ¿Coincide con la diferencia simétrica (A ^ B)?",
        "codigo_fuente": "A = {1, 2, 3, 4}\nB = {3, 4, 5, 6}\nresultado = (A | B) - (A & B)\nprint(resultado)   # {1, 2, 5, 6}\nprint(A ^ B)       # {1, 2, 5, 6}",
        "es_interactivo": True
    }
}


@b11_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque11", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque11",
        bloque_titulo=info.get("titulo", "Bloque 11"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b11_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej in (1, 3):
            a_str = request.form.get("set_a_input", "").strip()
            b_str = request.form.get("set_b_input", "").strip()
            if campos_vacios(a_str, b_str):
                salida_consola = "⚠️ Debes ingresar ambos conjuntos."
            else:
                set_a = set(float(x.strip()) for x in a_str.split(",") if x.strip())
                set_b = set(float(x.strip()) for x in b_str.split(",") if x.strip())
                fn = ejecutar_ejercicio1 if num_ej == 1 else ejecutar_ejercicio3
                salida_consola = ejecutar_y_capturar(fn, set_a, set_b)

        elif num_ej == 2:
            lista_str = request.form.get("lista_input", "").strip()
            if campos_vacios(lista_str):
                salida_consola = "⚠️ Debes ingresar la lista con duplicados."
            else:
                lista = [float(x.strip()) for x in lista_str.split(",") if x.strip()]
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio2, lista)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque11",
        bloque_titulo="Bloque 11: Conjuntos (set)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
