from flask import Blueprint, render_template, request
from app.blueprints.bloque02.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b02_bp = Blueprint('bloque02', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Declara una variable de cada tipo simple (int, float, str, bool, None) y cada tipo complejo (list, tuple, dict, set) e imprímelas todas.",
        "codigo_fuente": "entero: int = 19\nflotante: float = 3.14\ncadena: str = 'Hello World'\nbooleano: bool = True\nnulo = None\nlista = [1, 2, 3, 'python']\ntupla = (1, 'hello', 3.14)\ndiccionario = {'nombre': 'Juan', 'edad': 25}\nconjunto = {1, 2, 3, 4, 5}",
        "es_interactivo": False
    },
    2: {
        "enunciado": "Crea una lista con 5 elementos. Imprime el primero, el último y lista[1:4].",
        "codigo_fuente": "lista = [10, 20, 30, 40, 50]\nprint(lista[0])    # primero\nprint(lista[-1])   # último\nprint(lista[1:4])  # [20, 30, 40]",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Crea una clase con un método que declare un str, una list y un dict. Imprime: primer carácter del texto, último elemento de la lista y el valor de una clave del dict.",
        "codigo_fuente": "class DemoTipos:\n    def mostrar(self):\n        texto = 'Python'\n        lista = [10, 20, 30]\n        datos = {'curso': 'POO'}\n        print(texto[0])       # P\n        print(lista[-1])      # 30\n        print(datos['curso']) # POO",
        "es_interactivo": False
    }
}


@b02_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque02", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque02",
        bloque_titulo=info.get("titulo", "Bloque 02"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b02_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    ejecutar_ejercicio1()

                elif num_ej == 2:
                    elementos_str = request.form.get("elementos_input", "").strip()
                    if elementos_str == "":
                        print("⚠️ Debes ingresar los elementos de la lista.")
                    else:
                        # Convertir a número (float) para que el modelo los muestre como números
                        lista = []
                        for x in elementos_str.split(","):
                            x = x.strip()
                            if x:
                                try:
                                    lista.append(int(x) if '.' not in x else float(x))
                                except ValueError:
                                    lista.append(x)  # si no es número, dejarlo como string
                        if len(lista) < 1:
                            print("⚠️ La lista debe tener al menos 1 elemento.")
                        else:
                            ejecutar_ejercicio2(lista)

                elif num_ej == 3:
                    ejecutar_ejercicio3()

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque02",
        bloque_titulo="Bloque 02: Variables y Tipos de Datos",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
