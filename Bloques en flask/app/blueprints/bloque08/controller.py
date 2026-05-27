from flask import Blueprint, render_template, request
from app.blueprints.bloque08.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b08_bp = Blueprint('bloque08', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea una lista, agrégale 3 elementos con append(), ordénala con sort() y muéstrala.",
        "codigo_fuente": "nums = []\nnums.append(5)\nnums.append(2)\nnums.append(8)\nnums.sort()\nprint(nums)  # [2, 5, 8]",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Dada la lista [5, 3, 8, 1, 9, 3], calcula e imprime su suma, máximo y mínimo usando funciones integradas.",
        "codigo_fuente": "nums = [5, 3, 8, 1, 9, 3]\nprint(sum(nums))   # 29\nprint(max(nums))   # 9\nprint(min(nums))   # 1",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Demuestra la diferencia entre referencia y copia: asigna copia=lista, haz append(4) y observa que ambas cambian. Luego usa .copy() y comprueba que solo cambia una.",
        "codigo_fuente": "lista = [1, 2, 3]\ncopia_ref  = lista\ncopia_real = lista.copy()\ncopia_ref.append(4)\nprint(lista)      # [1, 2, 3, 4]\nprint(copia_real) # [1, 2, 3]",
        "es_interactivo": False
    }
}

@b08_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    elementos = request.form.get("elementos_input", "5, 2, 8")
                    lista = [float(x.strip()) for x in elementos.split(",") if x.strip()]
                    ejecutar_ejercicio1(lista)
                elif num_ej == 2:
                    elementos = request.form.get("elementos_input", "5, 3, 8, 1, 9, 3")
                    lista = [float(x.strip()) for x in elementos.split(",") if x.strip()]
                    ejecutar_ejercicio2(lista)
                elif num_ej == 3:
                    ejecutar_ejercicio3()
            except Exception as e:
                print(f"❌ Error al procesar listas: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque08",
        bloque_titulo="Bloque 08: Listas",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )