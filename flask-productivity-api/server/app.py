from flask import Flask
from .config import Config
from .extensions import db, migrate, bcrypt



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    
    from . import models
    from .routes.auth_routes import auth_bp
    from .routes.note_routes import note_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(note_bp, url_prefix="/notes")

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)