from flask import Blueprint, render_template, request
from app.blueprints.bloque02.models import (
    ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3
)

b02_bp = Blueprint('bloque02', __name__, template_folder='../../templates')

DATOS_RETOS = {
    1: {
        "enunciado": "Crea la clase CuentaBancaria con titular y saldo (atributos de instancia). Instancia 2 cuentas con saldos diferentes.",
        "codigo_fuente": "class CuentaBancaria:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo",
        "es_interactivo": False
    },
    2: {
        "enunciado": "Agrega un atributo de clase llamado 'tasa_interes' = 0.05 y un método para aplicar este interés al saldo actual de la cuenta.",
        "codigo_fuente": "class CuentaConInteres:\n    tasa_interes = 0.05  # Atributo de clase\n    def aplicar_interes(self):\n        self.saldo += self.saldo * self.tasa_interes",
        "es_interactivo": True
    },
    3: {
        "enunciado": "Demuestra el tipado dinámico cambiando temporalmente el atributo 'saldo' de un tipo numérico a una cadena de texto (String) y viceversa.",
        "codigo_fuente": "self.saldo = 'CUENTA_CONGELADA'\n# Python permite cambiar el tipo de un atributo en caliente",
        "es_interactivo": True
    }
}

@b02_bp.route('/ejercicio/<int:num_ej>', methods=['GET', 'POST'])
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
                    ejecutar_ejercicio1()
                elif num_ej == 2:
                    titular_web = request.form.get("titular_input", "Roberto")
                    saldo_web = float(request.form.get("saldo_input", 1000.0))
                    ejecutar_ejercicio2(titular_web, saldo_web)
                elif num_ej == 3:
                    titular_web = request.form.get("titular_input", "María")
                    alerta_web = request.form.get("alerta_input", "ALERTA: FONDOS_BLOQUEADOS")
                    reinicio_web = float(request.form.get("reinicio_input", 250.75))
                    ejecutar_ejercicio3(titular_web, alerta_web, reinicio_web)
            except Exception as e:
                print(f"❌ Error al procesar datos del formulario: {str(e)}")
        salida_consola = f.getvalue()

    salida_consola = f.getvalue()

    return render_template(
        'ejercicio_detalle.html',
        bloque_id="bloque02",
        bloque_titulo="Bloque 02: Variables y Tipos de Datos",
        ej_actual=num_ej,
        enunciado=reto["enunciado"],
        codigo=reto["codigo_fuente"],
        es_interactivo=reto["es_interactivo"],
        consola=salida_consola,
        datos_retos_nav=list(DATOS_RETOS.keys())
    )