from flask import Flask
from . import routes
from .utils import compile_markdown

def create_app():
    app = Flask(__name__)
    
    # Compile markdown files
    compile_markdown()
    
    app.register_blueprint(routes.bp)
    
    return app