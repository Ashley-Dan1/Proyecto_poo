from flask import Blueprint, render_template, request
from app.blueprints.bloque14.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO

b14_bp = Blueprint('bloque14', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Desempaqueta (10, 20, 30, 40) asignando explícitamente el primero, el último y agrupando los intermedios en una sublista con el operador *.",
        "codigo_fuente": "primera, *mitad, ultima = (10, 20, 30, 40)\nprint(primera)  # 10\nprint(mitad)    # [20, 30]\nprint(ultima)   # 40",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Define una función multiplicar(a, b, c) y llámala desempaquetando los datos de una lista con el operador asterisco (*lista).",
        "codigo_fuente": "def multiplicar(a, b, c):\n    return a * b * c\n\nvalores = [2, 3, 4]\nresultado = multiplicar(*valores)  # equivale a multiplicar(2, 3, 4)\nprint(resultado)  # 24",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Une el contenido de dos diccionarios en un nuevo mapa usando ** sin alterar los diccionarios originales.",
        "codigo_fuente": "dict1 = {'a': 1}\ndict2 = {'b': 2}\ncombinado = {**dict1, **dict2}\nprint(combinado)  # {'a': 1, 'b': 2}\nprint(dict1)      # {'a': 1}  ← sin cambios",
        "es_interactivo": True
    }
}


@b14_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque14", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque14",
        bloque_titulo=info.get("titulo", "Bloque 14"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b14_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    # CORREGIDO: sin default silencioso
                    datos_crudos = request.form.get("tupla_input", "").strip()
                    if datos_crudos == "":
                        print("⚠️ Debes ingresar los valores para desempaquetar.")
                    else:
                        tupla_valores = tuple(float(x.strip()) for x in datos_crudos.split(",") if x.strip())
                        if len(tupla_valores) < 3:
                            print("⚠️ Necesitas al menos 3 valores para el unpacking con *mitad.")
                        else:
                            ejecutar_ejercicio1(tupla_valores)

                elif num_ej == 2:
                    # CORREGIDO: sin default silencioso
                    lista_cruda = request.form.get("lista_input", "").strip()
                    if lista_cruda == "":
                        print("⚠️ Debes ingresar los 3 factores separados por coma.")
                    else:
                        lista_valores = [float(x.strip()) for x in lista_cruda.split(",") if x.strip()][:3]
                        while len(lista_valores) < 3:
                            lista_valores.append(1.0)
                        ejecutar_ejercicio2(lista_valores)

                elif num_ej == 3:
                    # CORREGIDO: sin defaults silenciosos
                    llave1 = request.form.get("llave1", "").strip()
                    valor1 = request.form.get("valor1", "").strip()
                    llave2 = request.form.get("llave2", "").strip()
                    valor2 = request.form.get("valor2", "").strip()
                    if llave1 == "" or valor1 == "" or llave2 == "" or valor2 == "":
                        print("⚠️ Debes completar los cuatro campos (llave1, valor1, llave2, valor2).")
                    else:
                        ejecutar_ejercicio3({llave1: valor1}, {llave2: valor2})

            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque14",
        bloque_titulo="Bloque 14: Unpacking (Desempaquetado)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
