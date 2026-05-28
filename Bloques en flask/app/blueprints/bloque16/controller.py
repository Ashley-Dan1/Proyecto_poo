import os
from flask import Blueprint, render_template, request
from app.blueprints.bloque16.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b16_bp = Blueprint('bloque16', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Escribe una cadena de texto personalizada dentro de un archivo llamado 'datos.txt' utilizando el modo de escritura ('w').",
        "codigo_fuente": "with open('datos.txt', 'w') as archivo:\n    archivo.write('Hola Mundo')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Abre el archivo de texto generado en el disco en modo lectura ('r') y recupera todo su contenido para mostrarlo en consola.",
        "codigo_fuente": "with open('datos.txt', 'r') as archivo:\n    print(archivo.read())",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Usa el modo 'a' (append) para agregar una nueva línea al final del archivo sin destruir el texto existente.",
        "codigo_fuente": "with open('datos.txt', 'a') as archivo:\n    archivo.write('\\nNueva línea')",
        "es_interactivo": True
    }
}

RUTA_ARCHIVO = os.path.join(os.getcwd(), "datos.txt")


@b16_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque16", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque16",
        bloque_titulo=info.get("titulo", "Bloque 16"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b16_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej == 1:
            texto = request.form.get("texto_input", "").strip()
            if campos_vacios(texto):
                salida_consola = "⚠️ Debes ingresar el texto a escribir en el archivo."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio1, RUTA_ARCHIVO, texto)

        elif num_ej == 2:
            salida_consola = ejecutar_y_capturar(ejecutar_ejercicio2, RUTA_ARCHIVO)

        elif num_ej == 3:
            texto_anexo = request.form.get("texto_anexo_input", "").strip()
            if campos_vacios(texto_anexo):
                salida_consola = "⚠️ Debes ingresar la línea a añadir al archivo."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio3, RUTA_ARCHIVO, texto_anexo)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque16",
        bloque_titulo="Bloque 16: Archivos y JSON",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
