from flask import Blueprint, render_template, request
from app.blueprints.bloque07.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b07_bp = Blueprint('bloque07', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea una función que calcule y retorne el doble de un número.",
        "codigo_fuente": "def doble(x):\n    return x * 2\n\nprint(doble(4))  # 8",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Crea una función que sume todos los elementos pasados como argumentos usando *args.",
        "codigo_fuente": "def sumar_varios(*numeros):\n    return sum(numeros)\n\nprint(sumar_varios(1, 2, 3, 4))  # 10",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Escribe una función recursiva para calcular el factorial de n. Ejemplo: factorial(5) = 120.",
        "codigo_fuente": "def factorial(n):\n    if n == 0: return 1        # caso base\n    return n * factorial(n - 1) # llamada recursiva\n\nprint(factorial(5))  # 120",
        "es_interactivo": True
    }
}


@b07_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque07", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque07",
        bloque_titulo=info.get("titulo", "Bloque 07"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b07_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    num_str = request.form.get("numero_input", "").strip()
                    if num_str == "":
                        print("⚠️ Debes ingresar un número.")
                    else:
                        ejecutar_ejercicio1(float(num_str))

                elif num_ej == 2:
                    args_crudos = request.form.get("args_input", "").strip()
                    if args_crudos == "":
                        print("⚠️ Debes ingresar al menos un número.")
                    else:
                        lista = [float(x.strip()) for x in args_crudos.split(",") if x.strip()]
                        ejecutar_ejercicio2(lista)

                elif num_ej == 3:
                    n_str = request.form.get("factorial_input", "").strip()
                    if n_str == "":
                        print("⚠️ Debes ingresar un número entre 0 y 12.")
                    else:
                        n_web = int(n_str)
                        # Validación server-side: limitar recursión profunda
                        if n_web < 0:
                            print("⚠️ El factorial no está definido para números negativos.")
                        elif n_web > 12:
                            print("⚠️ Por seguridad, el límite máximo es 12.")
                        else:
                            ejecutar_ejercicio3(n_web)

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque07",
        bloque_titulo="Bloque 07: Funciones",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
