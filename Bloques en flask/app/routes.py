import os
import json
import sqlite3
from functools import wraps
from flask import Blueprint, render_template, current_app, session, redirect, url_for, flash
from app.models_auth import DB_PATH

main_bp = Blueprint('main', __name__)


def login_required(f):
    """Decorador que protege rutas: redirige al login si no hay sesión activa."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            flash("Debes iniciar sesión para acceder a esa página.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


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
@login_required
def inicio():
    progreso_porcentaje = obtener_porcentaje_progreso()
    return render_template('inicio.html', progreso=progreso_porcentaje)


@main_bp.route('/ejercicios')
@login_required
def lista_ejercicios_global():
    progreso_porcentaje = obtener_porcentaje_progreso()

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT bloque_id FROM progreso WHERE usuario_id = ?', (session['usuario_id'],))
    bloques_hechos = [fila[0] for fila in cursor.fetchall()]
    conexion.close()

    return render_template(
        'ejercicios.html',
        progreso=progreso_porcentaje,
        bloques_hechos=bloques_hechos
    )


@main_bp.route('/acerca-de')
@login_required
def acerca_de():
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
