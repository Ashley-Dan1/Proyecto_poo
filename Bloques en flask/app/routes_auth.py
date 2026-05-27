from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from app.models_auth import ValidadorRegistro, DB_PATH

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    # Si ya está logueado, no tiene sentido registrarse
    if 'usuario_id' in session:
        return redirect(url_for('main.inicio'))

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        apellido = request.form.get('apellido', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        error = ValidadorRegistro.evaluar_registro(nombre, apellido, email, password)
        if error:
            flash(error, "danger")
            return render_template('auth/registro.html', nombre=nombre, apellido=apellido, email=email)

        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        try:
            password_encriptada = generate_password_hash(password)
            cursor.execute('INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)',
                           (nombre, apellido, email, password_encriptada))
            conexion.commit()
            flash("¡Registro exitoso! Ya puedes iniciar sesión.", "success")
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError:
            flash("El email ya se encuentra registrado.", "danger")
        finally:
            conexion.close()

    return render_template('auth/registro.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si ya está logueado, redirigir directo al inicio
    if 'usuario_id' in session:
        return redirect(url_for('main.inicio'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute('SELECT id, nombre, password FROM usuarios WHERE email = ?', (email,))
        usuario = cursor.fetchone()
        conexion.close()

        if usuario and check_password_hash(usuario[2], password):
            session['usuario_id'] = usuario[0]
            session['usuario_nombre'] = usuario[1]
            flash(f"¡Bienvenido de vuelta, {usuario[1]}!", "success")
            return redirect(url_for('main.inicio'))
        else:
            flash("Credenciales incorrectas. Verifica tu email y contraseña.", "danger")

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "info")
    return redirect(url_for('auth.login'))


@auth_bp.route('/completar-bloque/<string:bloque_id>', methods=['POST'])
def completar_bloque(bloque_id):
    """Permite al usuario marcar un bloque como completado para guardar su progreso."""
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario_id = session['usuario_id']
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT OR IGNORE INTO progreso (usuario_id, bloque_id) VALUES (?, ?)', (usuario_id, bloque_id))
        conexion.commit()
    except Exception:
        pass
    finally:
        conexion.close()

    return redirect(url_for('main.lista_ejercicios_global'))
