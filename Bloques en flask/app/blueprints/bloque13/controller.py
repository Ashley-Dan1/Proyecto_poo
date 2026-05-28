from flask import Blueprint, render_template, request
from app.blueprints.bloque13.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b13_bp = Blueprint('bloque13', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea un decorador que imprima 'Iniciando...' antes de ejecutar la función decorada y 'Ejecución completada.' después.",
        "codigo_fuente": "def decorador_inicio(f):\n    def wrapper(*args, **kwargs):\n        print('Iniciando...')\n        resultado = f(*args, **kwargs)\n        print('Ejecución completada.')\n        return resultado\n    return wrapper\n\n@decorador_inicio\ndef mi_funcion():\n    print('Ejecutando...')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Crea un decorador que verifique que el argumento sea positivo antes de calcular su cuadrado. Si es negativo, no ejecuta la función.",
        "codigo_fuente": "def validar_positivo(f):\n    def wrapper(n):\n        if n < 0:\n            print('No es positivo')\n            return None\n        return f(n)\n    return wrapper\n\n@validar_positivo\ndef cuadrado(n):\n    return n ** 2",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Analiza: @log aplicado a suma(a, b). ¿Qué imprime suma(2, 3)? El decorador @log debe imprimir 'Llamando función...' y el retorno.",
        "codigo_fuente": "def log(f):\n    def wrapper(*args, **kwargs):\n        print(f'Llamando función {f.__name__} con args={args}')\n        resultado = f(*args, **kwargs)\n        print(f'Retorno: {resultado}')\n        return resultado\n    return wrapper\n\n@log\ndef suma(a, b):\n    return a + b\n\nsuma(2, 3)",
        "es_interactivo": True
    }
}


@b13_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque13", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque13",
        bloque_titulo=info.get("titulo", "Bloque 13"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b13_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    # CORREGIDO: sin default silencioso, valida campo vacío
                    nombre_web = request.form.get("nombre_funcion_input", "").strip()
                    if nombre_web == "":
                        print("⚠️ Debes ingresar el nombre de la función.")
                    else:
                        ejecutar_ejercicio1(nombre_web)

                elif num_ej == 2:
                    # CORREGIDO: sin default silencioso
                    numero_str = request.form.get("numero_input", "").strip()
                    if numero_str == "":
                        print("⚠️ Debes ingresar un número.")
                    else:
                        ejecutar_ejercicio2(float(numero_str))

                elif num_ej == 3:
                    # CORREGIDO: sin defaults silenciosos
                    a_str = request.form.get("valor_a_input", "").strip()
                    b_str = request.form.get("valor_b_input", "").strip()
                    if a_str == "" or b_str == "":
                        print("⚠️ Debes ingresar ambos valores (A y B).")
                    else:
                        ejecutar_ejercicio3(float(a_str), float(b_str))

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque13",
        bloque_titulo="Bloque 13: Decoradores",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
