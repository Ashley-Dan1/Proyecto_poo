from flask import Blueprint, render_template, request
from app.blueprints.bloque09.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b09_bp = Blueprint('bloque09', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea una tupla con 4 elementos. Intenta modificar el primero y observa el TypeError que Python lanza.",
        "codigo_fuente": "tupla = (1, 2, 3, 4)\ntupla[0] = 10  # ❌ TypeError: inmutable",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Usa unpacking para asignar los valores (100, 200, 300, 400) a variables: a, b y *resto.",
        "codigo_fuente": "a, b, *resto = (100, 200, 300, 400)\nprint(a)     # 100\nprint(b)     # 200\nprint(resto) # [300, 400]",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Recorre una lista de coordenadas (tuplas) usando for con unpacking y muestra cada x e y.",
        "codigo_fuente": "coordenadas = [(1,2), (3,4), (5,6)]\nfor x, y in coordenadas:\n    print(f'x={x}, y={y}')",
        "es_interactivo": True
    }
}


@b09_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque09", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque09",
        bloque_titulo=info.get("titulo", "Bloque 09"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b09_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    elementos_str = request.form.get("tupla_input", "").strip()
                    if elementos_str == "":
                        print("⚠️ Debes ingresar los elementos de la tupla.")
                    else:
                        tupla = tuple(x.strip() for x in elementos_str.split(",") if x.strip())
                        ejecutar_ejercicio1(tupla)

                elif num_ej == 2:
                    elementos_str = request.form.get("tupla_input", "").strip()
                    if elementos_str == "":
                        print("⚠️ Debes ingresar los valores numéricos.")
                    else:
                        tupla = tuple(int(x.strip()) for x in elementos_str.split(",") if x.strip())
                        if len(tupla) < 2:
                            print("⚠️ Necesitas al menos 2 elementos para el unpacking.")
                        else:
                            ejecutar_ejercicio2(tupla)

                elif num_ej == 3:
                    pares_str = request.form.get("coordenadas_input", "").strip()
                    if pares_str == "":
                        print("⚠️ Debes ingresar las coordenadas.")
                    else:
                        coordenadas = []
                        for par in pares_str.split("|"):
                            partes = par.strip().split(",")
                            if len(partes) == 2:
                                coordenadas.append((partes[0].strip(), partes[1].strip()))
                        if not coordenadas:
                            print("⚠️ Formato inválido. Usa: 1,2 | 3,4 | 5,6")
                        else:
                            ejecutar_ejercicio3(coordenadas)

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque09",
        bloque_titulo="Bloque 09: Tuplas",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
