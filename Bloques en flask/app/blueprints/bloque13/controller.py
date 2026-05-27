from flask import Blueprint, render_template, request
from app.blueprints.bloque13.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b13_bp = Blueprint('bloque13', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Desempaqueta dinámicamente una estructura de 4 elementos asignando explícitamente el primero, el último y agrupando los intermedios en una sublista.",
        "codigo_fuente": "primera, *mitad, ultima = (10, 20, 30, 40)\nprint(primera, mitad, ultima)",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Define una función de tres parámetros posicionales y llámala desempaquetando los datos almacenados dentro de una lista ordinaria mediante el operador asterisco.",
        "codigo_fuente": "valores = [2, 3, 4]\nmultiplicar(*valores)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Une el contenido de dos diccionarios independientes en un nuevo mapa utilizando el operador de doble asterisco, asegurando no alterar las fuentes.",
        "codigo_fuente": "combinado = {**dict1, **dict2}",
        "es_interactivo": True
    }
}

@b13_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    datos_crudos = request.form.get("tupla_input", "10, 20, 30, 40")
                    tupla_valores = tuple(float(x.strip()) for x in datos_crudos.split(",") if x.strip())
                    ejecutar_ejercicio1(tupla_valores)
                elif num_ej == 2:
                    lista_cruda = request.form.get("lista_input", "2, 3, 4")
                    lista_valores = [float(x.strip()) for x in lista_cruda.split(",") if x.strip()][:3]
                    # Rellenamos por si el usuario manda menos de 3 parámetros
                    while len(lista_valores) < 3:
                        lista_valores.append(1.0)
                    ejecutar_ejercicio2(lista_valores)
                elif num_ej == 3:
                    llave1 = request.form.get("llave1", "a")
                    valor1 = request.form.get("valor1", "10")
                    llave2 = request.form.get("llave2", "b")
                    valor2 = request.form.get("valor2", "20")
                    
                    dict_uno = {llave1: valor1}
                    dict_dos = {llave2: valor2}
                    ejecutar_ejercicio3(dict_uno, dict_dos)
            except Exception as e:
                print(f"❌ Error en los flujos de desempaquetado: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque13",
        bloque_titulo="Bloque 13: Unpacking (Desempaquetado)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )