import re
from werkzeug.security import generate_password_hash, check_password_hash

# Simulación de ORM ligero o estructuras de datos con SQLite. 
# Para asegurar que corra directo, usaremos sqlite3 nativo de Python.
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database.db')

def inicializar_base_datos():
    """Crea las tablas de usuarios y progreso si no existen."""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    # Tabla de Usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Tabla de Progreso (Relaciona usuario con bloques completados)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progreso (
            usuario_id INTEGER,
            bloque_id TEXT,
            PRIMARY KEY (usuario_id, bloque_id)
        )
    ''')
    conexion.commit()
    conexion.close()


class ValidadorRegistro:
    @staticmethod
    def validar_nombre_apellido(texto):
        # Solo letras (incluyendo eñes y acentos) y espacios
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        return bool(re.match(patron, texto))

    @staticmethod
    def validar_email(email):
        # Debe estar en minúsculas completo
        if email != email.lower():
            return False
        # Validar un solo arroba y al menos un punto después del arroba
        if email.count('@') != 1:
            return False
        
        usuario, dominio = email.split('@')
        if dominio.count('.') < 1:
            return False
            
        # Validación estándar de estructura
        patron = r'^[\w\.-]+@[\w\.-]+\.[\w]+$'
        return bool(re.match(patron, email))

    @staticmethod
    def validar_password(password):
        # Mínimo 7 caracteres, una mayúscula, una minúscula, un número y un carácter especial (ej. _)
        if len(password) < 7:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "_-!@#$%^&*(),.?\":{}|<>" for c in password):
            return False
        return True

    @classmethod
    def evaluar_registro(cls, nombre, apellido, email, password):
        """Devuelve un mensaje de error específico si algo falla, o None si es válido."""
        if not cls.validar_nombre_apellido(nombre):
            return "nombre invalido"
        if not cls.validar_nombre_apellido(apellido):
            return "apellido invalido"
        if not cls.validar_email(email):
            return "email invalido"
        if not cls.validar_password(password):
            return "contraseña invalida"
        return None