from flask import Blueprint, render_template, request
from app.blueprints.bloque10.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO   # ← import del compendio

b10_bp = Blueprint('bloque10', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea un diccionario de persona con nombre, edad y ciudad. Accede a sus valores usando [] y también usando get().",
        "codigo_fuente": "persona = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Quito'}\nprint(persona['nombre'])              # acceso directo\nprint(persona.get('ciudad'))          # acceso seguro\nprint(persona.get('telefono', 'N/A')) # valor por defecto",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Itera sobre los items() del diccionario de persona e imprime cada clave y su valor.",
        "codigo_fuente": "for clave, valor in persona.items():\n    print(clave, '→', valor)",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Demuestra qué pasa si haces copia=datos y luego copia['b']=2. ¿Cambia el original? Usa .copy() para evitarlo.",
        "codigo_fuente": "datos = {'a': 1}\ncopia_ref  = datos          # misma referencia\ncopia_real = datos.copy()   # objeto nuevo\n\ncopia_ref['b'] = 2\nprint(datos)      # {'a':1, 'b':2} ← también cambió\nprint(copia_real) # {'a':1}        ← no cambió",
        "es_interactivo": True
    }
}

@b10_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque10", {})
    return render_template(
        'ejercicio_concepto.html',          # nombre corregido (sin typo)
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
        import io, contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                if num_ej == 1:
                    nombre_web = request.form.get("nombre_input", "Juan")
                    edad_web   = int(request.form.get("edad_input", 25))
                    ciudad_web = request.form.get("ciudad_input", "Quito")
                    ejecutar_ejercicio1(nombre_web, edad_web, ciudad_web)
                elif num_ej == 2:
                    nombre_web = request.form.get("nombre_input", "Juan")
                    edad_web   = int(request.form.get("edad_input", 25))
                    ciudad_web = request.form.get("ciudad_input", "Quito")
                    ejecutar_ejercicio2(nombre_web, edad_web, ciudad_web)
                elif num_ej == 3:
                    ejecutar_ejercicio3()
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        salida_consola = f.getvalue()

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

