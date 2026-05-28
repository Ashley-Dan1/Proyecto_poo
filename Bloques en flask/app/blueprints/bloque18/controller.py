from flask import Blueprint, render_template, request
from app.blueprints.bloque18.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)
from app.contenido import COMPENDIO
from app.utils import ejecutar_y_capturar, campos_vacios

b18_bp = Blueprint('bloque18', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea la clase abstracta Figura con el método abstracto area(). Implementa la clase concreta Triangulo que reciba base y altura y calcule su área.",
        "codigo_fuente": "from abc import ABC, abstractmethod\n\nclass Figura(ABC):\n    @abstractmethod\n    def area(self): pass\n\nclass Triangulo(Figura):\n    def __init__(self, base, altura):\n        self.base = base\n        self.altura = altura\n    def area(self):\n        return (self.base * self.altura) / 2",
        "es_interactivo": True
    },
    2: {
        "enunciado": "Agrega @property con setter a la clase Producto para validar que el precio siempre sea >= 0.",
        "codigo_fuente": "class Producto:\n    def __init__(self):\n        self.__precio = 0\n\n    @property\n    def precio(self):\n        return self.__precio\n\n    @precio.setter\n    def precio(self, valor):\n        if valor < 0:\n            raise ValueError('Precio inválido')\n        self.__precio = valor",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Crea la jerarquía Animal → Perro, Gato, Vaca. Cada subclase implementa su propio método sonido(). Recorre una lista de animales y llama a sonido() en cada uno.",
        "codigo_fuente": "class Animal:\n    def sonido(self): pass\n\nclass Perro(Animal):\n    def sonido(self): print('Ladra')\n\nclass Gato(Animal):\n    def sonido(self): print('Maulla')\n\nclass Vaca(Animal):\n    def sonido(self): print('Muge')\n\nfor a in [Perro(), Gato(), Vaca()]:\n    a.sonido()",
        "es_interactivo": True
    }
}


@b18_bp.route('/concepto')
def ver_concepto():
    info = COMPENDIO.get("bloque18", {})
    return render_template(
        'ejercicio_concepto.html',
        bloque_id="bloque18",
        bloque_titulo=info.get("titulo", "Bloque 18"),
        concepto_texto=info.get("concepto", ""),
        ejemplo_codigo=info.get("ejemplo", ""),
        datos_retos_nav=list(DATOS_RETOS.keys())
    )


@b18_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
def gestionar_ejercicio(num_ej):
    if num_ej not in DATOS_RETOS:
        num_ej = 1
    reto = DATOS_RETOS[num_ej]
    salida_consola = ""

    if request.method == 'POST':
        if num_ej == 1:
            base_str = request.form.get("base_input", "").strip()
            altura_str = request.form.get("altura_input", "").strip()
            if campos_vacios(base_str, altura_str):
                salida_consola = "⚠️ Debes ingresar base y altura."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio1, float(base_str), float(altura_str))

        elif num_ej == 2:
            nombre = request.form.get("nombre_input", "").strip()
            precio_str = request.form.get("precio_input", "").strip()
            if campos_vacios(nombre, precio_str):
                salida_consola = "⚠️ Debes ingresar nombre y precio."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio2, nombre, float(precio_str))

        elif num_ej == 3:
            perro = request.form.get("perro_input", "").strip()
            gato = request.form.get("gato_input", "").strip()
            vaca = request.form.get("vaca_input", "").strip()
            if campos_vacios(perro, gato, vaca):
                salida_consola = "⚠️ Debes ingresar el nombre de los tres animales."
            else:
                salida_consola = ejecutar_y_capturar(ejecutar_ejercicio3, perro, gato, vaca)

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque18",
        bloque_titulo="Bloque 18: Principios de POO",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )
