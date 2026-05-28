from flask import Blueprint, render_template, request
from app.blueprints.bloque11.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

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
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
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
        import io, contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                if num_ej == 1:
                    a_crudo = request.form.get("set_a_input", "1, 2, 3, 4")
                    b_crudo = request.form.get("set_b_input", "3, 4, 5, 6")
                    set_a = set(float(x.strip()) for x in a_crudo.split(",") if x.strip())
                    set_b = set(float(x.strip()) for x in b_crudo.split(",") if x.strip())
                    ejecutar_ejercicio1(set_a, set_b)
                elif num_ej == 2:
                    lista_cruda = request.form.get("lista_input", "1, 2, 2, 3, 3, 3, 4")
                    lista = [float(x.strip()) for x in lista_cruda.split(",") if x.strip()]
                    ejecutar_ejercicio2(lista)
                elif num_ej == 3:
                    a_crudo = request.form.get("set_a_input", "1, 2, 3, 4")
                    b_crudo = request.form.get("set_b_input", "3, 4, 5, 6")
                    set_a = set(float(x.strip()) for x in a_crudo.split(",") if x.strip())
                    set_b = set(float(x.strip()) for x in b_crudo.split(",") if x.strip())
                    ejecutar_ejercicio3(set_a, set_b)
            except Exception as e:
                print(f"❌ Error al procesar conjuntos: {str(e)}")
        salida_consola = f.getvalue()

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
