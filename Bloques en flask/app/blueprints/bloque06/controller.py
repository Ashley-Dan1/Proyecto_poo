from flask import Blueprint, render_template, request
from app.blueprints.bloque06.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

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
        "enunciado": "Crea una lista con los cuadrados de los números pares del 1 al 10 usando list comprehension. Resultado esperado: [4, 16, 36, 64, 100]",
        "codigo_fuente": "cuadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]\nprint(cuadrados_pares)  # [4, 16, 36, 64, 100]",
        "es_interactivo": True
    }
}


@b06_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque06", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque06",
        bloque_titulo=info.get("titulo", "Bloque 06"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


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
                    # Nombre único: limite_while_input
                    limite_str = request.form.get("limite_while_input", "").strip()
                    if limite_str == "":
                        print("⚠️ Debes ingresar el límite del conteo.")
                    else:
                        limite = int(limite_str)
                        if limite > 100:
                            limite = 100
                            print("ℹ️ Límite ajustado a 100 para evitar salidas muy largas.")
                        ejecutar_ejercicio1(limite)

                elif num_ej == 2:
                    frutas_crudas = request.form.get("frutas_input", "").strip()
                    if frutas_crudas == "":
                        print("⚠️ Debes ingresar al menos una fruta.")
                    else:
                        lista_frutas = [x.strip() for x in frutas_crudas.split(",") if x.strip()]
                        ejecutar_ejercicio2(lista_frutas)

                elif num_ej == 3:
                    # Nombre único: limite_range_input
                    limite_str = request.form.get("limite_range_input", "").strip()
                    if limite_str == "":
                        print("⚠️ Debes ingresar el límite del rango.")
                    else:
                        limite = int(limite_str)
                        if limite > 100:
                            limite = 100
                            print("ℹ️ Límite ajustado a 100.")
                        ejecutar_ejercicio3(limite)

            except Exception as e:
                print(f"❌ Error: {str(e)}")
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
