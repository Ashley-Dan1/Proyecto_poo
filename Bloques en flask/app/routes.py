import os
import json
import sqlite3
from flask import Blueprint, render_template, current_app, session
from app.models_auth import DB_PATH

main_bp = Blueprint('main', __name__)

def obtener_porcentaje_progreso():
    """Calcula el porcentaje de avance real del usuario logueado."""
    if 'usuario_id' not in session:
        return 0
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM progreso WHERE usuario_id = ?', (session['usuario_id'],))
    completados = cursor.fetchone()[0]
    conexion.close()

    # 20 bloques totales = 5% por cada bloque completo
    return int((completados / 20) * 100)


@main_bp.route('/')
def inicio():
    progreso_porcentaje = obtener_porcentaje_progreso()
    return render_template('inicio.html', progreso=progreso_porcentaje)


@main_bp.route('/ejercicios')
def lista_ejercicios_global():
    progreso_porcentaje = obtener_porcentaje_progreso()

    # Obtener qué bloques específicos ya guardó el usuario
    bloques_hechos = []
    if 'usuario_id' in session:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute('SELECT bloque_id FROM progreso WHERE usuario_id = ?', (session['usuario_id'],))
        bloques_hechos = [fila[0] for fila in cursor.fetchall()]
        conexion.close()

    return render_template(
        'ejercicios.html',
        progreso=progreso_porcentaje,
        bloques_hechos=bloques_hechos    # CORREGIDO: ya se pasa correctamente
    )


@main_bp.route('/acerca-de')
def acerca_de():
    # CORREGIDO: cargamos el JSON y pasamos la variable 'plataforma' al template
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'portada.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            plataforma = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        plataforma = {
            "titulo_plataforma": "Entorno de Aprendizaje Python",
            "version": "2.0.26",
            "descripcion": "Un compendio interactivo y académico diseñado bajo el paradigma de Programación Orientada a Objetos."
        }

    return render_template('acerca_de.html', plataforma=plataforma)