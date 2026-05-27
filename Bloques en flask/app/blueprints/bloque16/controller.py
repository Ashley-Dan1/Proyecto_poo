from flask import Blueprint, render_template, request
import os
from app.blueprints.bloque16.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b16_bp = Blueprint('bloque16', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Escribe una cadena de texto personalizada (por defecto 'Hola Mundo') dentro de un archivo físico llamado 'datos.txt' utilizando el modo de escritura.",
        "codigo_fuente": "with open('datos.txt', 'w') as archivo:\n    archivo.write('Hola Mundo')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Abre el archivo de texto generado en el disco en modo lectura y recupera todo su contenido para desplegarlo de manera íntegra en la terminal de salida.",
        "codigo_fuente": "with open('datos.txt', 'r') as archivo:\n    print(archivo.read())",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Utiliza el modificador o modo 'a' (append) para incorporar una nueva línea informativa al final de tu archivo sin destruir ni sobrescribir el texto existente.",
        "codigo_fuente": "with open('datos.txt', 'a') as archivo:\n    archivo.write('\\nNueva línea')",
        "es_interactivo": True
    }
}

@b16_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
        
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""
    
    # Definimos una ruta temporal controlada para no ensuciar el directorio raíz del proyecto
    ruta_archivo_datos = os.path.join(os.getcwd(), "datos.txt")

    if request.method == 'POST':
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                if num_ej == 1:
                    texto_web = request.form.get("texto_input", "Hola Mundo de persistencia")
                    ejecutar_ejercicio1(ruta_archivo_datos, texto_web)
                elif num_ej == 2:
                    ejecutar_ejercicio2(ruta_archivo_datos)
                elif num_ej == 3:
                    texto_anexo_web = request.form.get("texto_anexo_input", "Esta es una línea añadida posteriormente.")
                    ejecutar_ejercicio3(ruta_archivo_datos, texto_anexo_web)
            except Exception as e:
                print(f"❌ Error en los flujos de lectura/escritura física: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque16",
        bloque_titulo="Bloque 16: Archivos (I/O)",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )