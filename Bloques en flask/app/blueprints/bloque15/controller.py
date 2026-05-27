from flask import Blueprint, render_template, request
from app.blueprints.bloque15.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b15_bp = Blueprint('bloque15', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Utiliza List Comprehension para generar dinámicamente una lista compacta que contenga los cuadrados de una secuencia numérica consecutiva.",
        "codigo_fuente": "cuadrados = [x**2 for x in range(1, 6)]\nprint(cuadrados)",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Filtra de manera elegante una lista de números enteros para conservar únicamente los valores que sean pares mediante una cláusula inline.",
        "codigo_fuente": "numeros = [1, 2, 3, 4, 5, 6]\npares = [x for x in numeros if x % 2 == 0]\nprint(pares)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Toma un conjunto de palabras en formato de lista y procésalas utilizando una única línea de código para transformar todos los caracteres a letras mayúsculas.",
        "codigo_fuente": "palabras = ['python', 'clase', 'web']\nmayusculas = [p.upper() for p in palabras]\nprint(mayusculas)",
        "es_interactivo": True
    }
}

@b15_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    limite_web = int(request.form.get("limite_input", 5))
                    ejecutar_ejercicio1(limite_web)
                elif num_ej == 2:
                    entrada_numerica = request.form.get("lista_numeros_input", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
                    lista_numeros = [int(n.strip()) for n in entrada_numerica.split(",") if n.strip().isdigit() or (n.strip().startswith('-') and n.strip()[1:].isdigit())]
                    ejecutar_ejercicio2(lista_numeros)
                elif num_ej == 3:
                    entrada_texto = request.form.get("lista_palabras_input", "hola, mundo, programación, objetos")
                    lista_palabras = [p.strip() for p in entrada_texto.split(",") if p.strip()]
                    ejecutar_ejercicio3(lista_palabras)
            except Exception as e:
                print(f"❌ Error al evaluar expresiones de comprensión de listas: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque15",
        bloque_titulo="Bloque 15: List Comprehensions",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )