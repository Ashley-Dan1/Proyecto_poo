from flask import Blueprint, render_template, request
from app.blueprints.bloque07.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b07_bp = Blueprint('bloque07', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea una lista con 5 frutas. Escribe un programa que acceda e imprima la primera y la última fruta de forma dinámica.",
        "codigo_fuente": "frutas = ['Manzana', 'Plátano', 'Pera', 'Naranja', 'Uva']\nprint(frutas[0])\nprint(frutas[-1])",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Modifica el tercer elemento de tu lista de frutas por otra diferente y añade una fruta nueva al final de la colección utilizando métodos de lista.",
        "codigo_fuente": "frutas[2] = 'Mango'\nfrutas.append('Sandía')",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Elimina una fruta de la lista buscando por su nombre específico y luego extrae el último elemento de la lista restante usando el método .pop().",
        "codigo_fuente": "frutas.remove('Plátano')\nfrutas.pop()",
        "es_interactivo": True
    }
}

@b07_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
        
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    # Lista base por defecto para el ejercicio
    lista_defecto = ["Manzana", "Plátano", "Pera", "Naranja", "Uva"]

    if request.method == 'POST':
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                # Recogemos los valores de las frutas enviados por el usuario desde la web
                frutas_crudo = request.form.get("lista_frutas", "Manzana,Plátano,Pera,Naranja,Uva")
                lista_usuario = [fruta.strip() for fruta in frutas_crudo.split(",") if fruta.strip()]
                
                if not lista_usuario:
                    lista_usuario = lista_defecto

                if num_ej == 1:
                    ejecutar_ejercicio1(lista_usuario)
                elif num_ej == 2:
                    reemplazo_web = request.form.get("reemplazo_input", "Mango")
                    adicional_web = request.form.get("adicional_input", "Sandía")
                    ejecutar_ejercicio2(lista_usuario, reemplazo_web, adicional_web)
                elif num_ej == 3:
                    eliminar_web = request.form.get("eliminar_input", "Plátano")
                    ejecutar_ejercicio3(lista_usuario, eliminar_web)
            except Exception as e:
                print(f"❌ Error al manipular colecciones en el servidor: {str(e)}")
        salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque07",
        bloque_titulo="Bloque 07: Listas",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )