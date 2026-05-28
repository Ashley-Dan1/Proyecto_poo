from flask import Blueprint, render_template, request
from app.blueprints.bloque05.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b05_bp = Blueprint('bloque05', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Escribe un programa que determine si un número ingresado es par o impar usando el operador módulo.",
        "codigo_fuente": "numero = 15\nif numero % 2 == 0:\n    print('Par')\nelse:\n    print('Impar')",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Evalúa una calificación numérica (0-100) y asigna su equivalente en letra: >=90 → A, >=80 → B, >=70 → C, <70 → D.",
        "codigo_fuente": "if nota >= 90: print('A')\nelif nota >= 80: print('B')\nelif nota >= 70: print('C')\nelse: print('D')",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Sistema de login: si usuario=='admin' y password=='123' imprime 'Bienvenido'; en cualquier otro caso imprime 'Acceso denegado'.",
        "codigo_fuente": "if usuario == 'admin' and password == '123':\n    print('Bienvenido')\nelse:\n    print('Acceso denegado')",
        "es_interactivo": True
    }
}


@b05_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque05", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque05",
        bloque_titulo=info.get("titulo", "Bloque 05"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b05_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej == 1:
            numero_str = request.form.get("numero_input", "").strip()
            if campos_vacios(numero_str):
                salida_consola = "⚠️ Debes ingresar un número."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio1, int(numero_str))

        elif num_ej == 2:
            nota_str = request.form.get("nota_input", "").strip()
            if campos_vacios(nota_str):
                salida_consola = "⚠️ Debes ingresar una calificación."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio2, float(nota_str))

        elif num_ej == 3:
            usuario = request.form.get("usuario_input", "").strip()
            password = request.form.get("password_input", "")
            if campos_vacios(usuario, password):
                salida_consola = "⚠️ Debes ingresar usuario y contraseña."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio3, usuario, password)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque05",
        bloque_titulo="Bloque 05: Condicionales",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
