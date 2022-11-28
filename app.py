# Importar
from main import create_app
import os
from main import db

# Inicializar
app = create_app()
app.app_context().push()

if __name__ == '__main__':
    # Crear tablas
    db.create_all()
    # Iniciar servidor
    app.run(debug = True, port = os.getenv("PORT"))