from flask import Blueprint, render_template, request
from app.blueprints.bloque04.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

b04_bp = Blueprint('bloque04', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Solicita el nombre y la edad del usuario, y muestra un mensaje personalizado utilizando f-strings.",
        "codigo_fuente": "nombre = input('Ingrese su nombre: ')\nedad = int(input('Ingrese su edad: '))\nprint(f'Nombre: {nombre}, Edad: {edad}')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Lee dos números desde el teclado, calcula su suma y su promedio, y despliega ambos resultados aplicando el casting correspondiente.",
        "codigo_fuente": "num1 = float(input())\nnum2 = float(input())\nsuma = num1 + num2\npromedio = suma / 2",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Sin convertir la entrada del usuario (dejándola como str), intenta sumar el texto '5'. Explica detalladamente qué sucede.",
        "codigo_fuente": "numero = input('Número: ')  # Es str\nprint(numero + '5')  # Se concatenan",
        "es_interactivo": True
    }
}

@b04_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque04", {})
    return render_template(
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
        bloque_id="bloque04",
        bloque_titulo=info.get("titulo", "Bloque 04"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
 

@b04_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                if num_ej == 1:
                    nombre_web = request.form.get("nombre_input", "Ana")
                    edad_web = int(request.form.get("edad_input", 25))
                    ejecutar_ejercicio1(nombre_web, edad_web)
                elif num_ej == 2:
                    n1_web = float(request.form.get("num1_input", 10))
                    n2_web = float(request.form.get("num2_input", 20))
                    ejecutar_ejercicio2(n1_web, n2_web)
                elif num_ej == 3:
                    entrada_web = request.form.get("entrada_cruda_input", "10")
                    ejecutar_ejercicio3(entrada_web)
            except Exception as e:
                print(f"❌ Error al procesar entrada de datos: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque04",
        bloque_titulo="Bloque 04: Entrada y Salida (input/print)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
