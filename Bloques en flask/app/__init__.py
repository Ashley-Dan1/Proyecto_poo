import os
from flask import Flask, render_template
from app.models_auth import inicializar_base_datos

def crear_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SECRET_KEY'] = 'clave_secreta_para_sesiones_curso'

    inicializar_base_datos()

    from app.routes_auth import auth_bp
    app.register_blueprint(auth_bp)
    
    # ---------------------------------------------------------------------
    # REGISTRO DEL BLUEPRINT DE RUTAS ESTÁTICAS Y GLOBALES (routes.py)
    # ---------------------------------------------------------------------
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # ---------------------------------------------------------------------
    # REGISTRO MASIVO DE LOS 20 BLUEPRINTS (BLOQUES 0 A 19)
    # ---------------------------------------------------------------------
    from app.blueprints.bloque00.controller import b00_bp
    from app.blueprints.bloque01.controller import b01_bp
    from app.blueprints.bloque02.controller import b02_bp
    from app.blueprints.bloque03.controller import b03_bp
    from app.blueprints.bloque04.controller import b04_bp
    from app.blueprints.bloque05.controller import b05_bp
    from app.blueprints.bloque06.controller import b06_bp
    from app.blueprints.bloque07.controller import b07_bp
    from app.blueprints.bloque08.controller import b08_bp
    from app.blueprints.bloque09.controller import b09_bp
    from app.blueprints.bloque10.controller import b10_bp
    from app.blueprints.bloque11.controller import b11_bp
    from app.blueprints.bloque12.controller import b12_bp
    from app.blueprints.bloque13.controller import b13_bp
    from app.blueprints.bloque14.controller import b14_bp
    from app.blueprints.bloque15.controller import b15_bp
    from app.blueprints.bloque16.controller import b16_bp
    from app.blueprints.bloque17.controller import b17_bp
    from app.blueprints.bloque18.controller import b18_bp
    from app.blueprints.bloque19.controller import b19_bp

    app.register_blueprint(b00_bp, url_prefix='/curso/bloque00')
    app.register_blueprint(b01_bp, url_prefix='/curso/bloque01')
    app.register_blueprint(b02_bp, url_prefix='/curso/bloque02')
    app.register_blueprint(b03_bp, url_prefix='/curso/bloque03')
    app.register_blueprint(b04_bp, url_prefix='/curso/bloque04')
    app.register_blueprint(b05_bp, url_prefix='/curso/bloque05')
    app.register_blueprint(b06_bp, url_prefix='/curso/bloque06')
    app.register_blueprint(b07_bp, url_prefix='/curso/bloque07')
    app.register_blueprint(b08_bp, url_prefix='/curso/bloque08')
    app.register_blueprint(b09_bp, url_prefix='/curso/bloque09')
    app.register_blueprint(b10_bp, url_prefix='/curso/bloque10')
    app.register_blueprint(b11_bp, url_prefix='/curso/bloque11')
    app.register_blueprint(b12_bp, url_prefix='/curso/bloque12')
    app.register_blueprint(b13_bp, url_prefix='/curso/bloque13')
    app.register_blueprint(b14_bp, url_prefix='/curso/bloque14')
    app.register_blueprint(b15_bp, url_prefix='/curso/bloque15')
    app.register_blueprint(b16_bp, url_prefix='/curso/bloque16')
    app.register_blueprint(b17_bp, url_prefix='/curso/bloque17')
    app.register_blueprint(b18_bp, url_prefix='/curso/bloque18')
    app.register_blueprint(b19_bp, url_prefix='/curso/bloque19')

    return app