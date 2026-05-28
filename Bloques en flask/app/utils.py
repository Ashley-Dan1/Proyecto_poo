# =====================================================================
# app/utils.py
# Utilidades compartidas por todos los blueprints
# =====================================================================
import io
import contextlib


def ejecutar_y_capturar(funcion, *args, **kwargs):
    """
    Ejecuta 'funcion(*args, **kwargs)' capturando todo lo que
    imprima en stdout y devolviéndolo como string.

    Uso en cualquier controller:
        from app.utils import ejecutar_y_capturar
        salida = ejecutar_y_capturar(ejecutar_ejercicio1, param1, param2)
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        try:
            funcion(*args, **kwargs)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    return buffer.getvalue()


def campos_vacios(*valores):
    """
    Devuelve True si alguno de los valores recibidos está vacío
    (None o cadena vacía tras strip).

    Uso:
        if campos_vacios(nombre, edad):
            return "⚠️ Completa todos los campos."
    """
    for v in valores:
        if v is None or str(v).strip() == "":
            return True
    return False
