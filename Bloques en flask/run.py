from app import crear_app

app = crear_app()

if __name__ == '__main__':
    # Lanzamos el servidor en modo de depuración para desarrollo local
    app.run(debug=True, port=5000)