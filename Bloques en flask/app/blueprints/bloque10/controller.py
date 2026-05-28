from flask import Blueprint, render_template, request
from app.blueprints.bloque10.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b10_bp = Blueprint('bloque10', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea un diccionario de persona con nombre, edad y ciudad. Accede a sus valores usando [] y también usando get().",
        "codigo_fuente": "persona = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Quito'}\nprint(persona['nombre'])\nprint(persona.get('ciudad'))\nprint(persona.get('telefono', 'No existe'))",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Itera sobre los items() del diccionario de persona e imprime cada clave y su valor.",
        "codigo_fuente": "for clave, valor in persona.items():\n    print(clave, '→', valor)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Demuestra qué pasa si haces copia=datos y luego copia['b']=2. ¿Cambia el original? Usa .copy() para evitarlo.",
        "codigo_fuente": "datos = {'a': 1}\ncopia_ref  = datos\ncopia_real = datos.copy()\ncopia_ref['b'] = 2\nprint(datos)      # {'a':1, 'b':2}\nprint(copia_real) # {'a':1}",
        "es_interactivo": False
    }
}


@b10_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque10", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque10",
        bloque_titulo=info.get("titulo", "Bloque 10"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b10_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej in (1, 2):
            nombre = request.form.get("nombre_input", "").strip()
            edad_str = request.form.get("edad_input", "").strip()
            ciudad = request.form.get("ciudad_input", "").strip()
            if campos_vacios(nombre, edad_str, ciudad):
                salida_consola = "⚠️ Debes completar nombre, edad y ciudad."
            else:
                fn = ejecutar_ejercicio1 if num_ej == 1 else ejecutar_ejercicio2
                salida_consola = ejecutar_y_capturar(fn, nombre, int(edad_str), ciudad)

        elif num_ej == 3:
            salida_consola = ejecutar_y_capturar(ejecutar_ejercicio3)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque10",
        bloque_titulo="Bloque 10: Diccionarios",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
