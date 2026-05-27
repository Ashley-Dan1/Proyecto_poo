from flask import Blueprint, render_template, request
from app.blueprints.bloque06.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b06_bp = Blueprint('bloque06', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Imprime los números del 1 al 10 usando un bucle while.",
        "codigo_fuente": "contador = 1\nwhile contador <= 10:\n    print(contador)\n    contador += 1",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Recorre una lista de frutas usando enumerate() e imprime el índice y el nombre de cada una.",
        "codigo_fuente": "frutas = ['manzana', 'pera', 'uva']\nfor indice, fruta in enumerate(frutas):\n    print(indice, fruta)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Crea una lista con los cuadrados de los números pares del 1 al 10 usando list comprehension.",
        "codigo_fuente": "cuadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]\nprint(cuadrados_pares)  # [4, 16, 36, 64, 100]",
        "es_interactivo": True
    }
}

@b06_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    limite_web = int(request.form.get("limite_input", 10))
                    ejecutar_ejercicio1(limite_web)
                elif num_ej == 2:
                    frutas_crudas = request.form.get("frutas_input", "manzana, pera, uva")
                    lista_frutas = [f.strip() for f in frutas_crudas.split(",") if f.strip()]
                    ejecutar_ejercicio2(lista_frutas)
                elif num_ej == 3:
                    limite_web = int(request.form.get("limite_input", 10))
                    ejecutar_ejercicio3(limite_web)
            except Exception as e:
                print(f"❌ Error al procesar bucles: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque06",
        bloque_titulo="Bloque 06: Bucles (for / while)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )