from flask import Blueprint, render_template, request
from app.blueprints.bloque00.models import ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b00_bp = Blueprint('bloque00', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Identifica 5 clases para modelar un sistema de biblioteca.",
        "codigo_fuente": "class SistemaBiblioteca:\n    def __init__(self):\n        self.clases_identificadas = ['Libro', 'Usuario', 'Prestamo', 'Autor', 'Categoria']",
        "es_interactivo": False
    },
    2: {
        "enunciado": "Crea la clase Persona con nombre y edad. Instancia 3 objetos diferentes.",
        "codigo_fuente": "class Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad\n\np1 = Persona('Carlos', 20)\np2 = Persona('Ana', 25)\np3 = Persona('Daniel', 19)",
        "es_interactivo": False
    },
    3: {
        "enunciado": "Explica con tus palabras la diferencia entre clase y objeto.",
        "codigo_fuente": "class ExplicadorConceptos:\n    def mostrar_diferencia(self):\n        pass",
        "es_interactivo": False
    }
}


@b00_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque00", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque00",
        bloque_titulo=info.get("titulo", "Bloque 00"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b00_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej == 1:
            salida_consola = ejecutar_y_capturar(ejecutar_ejercicio1)
        elif num_ej == 2:
            salida_consola = ejecutar_y_capturar(ejecutar_ejercicio2)
        elif num_ej == 3:
            salida_consola = ejecutar_y_capturar(ejecutar_ejercicio3)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque00",
        bloque_titulo="Bloque 00: Introducción a la POO",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
