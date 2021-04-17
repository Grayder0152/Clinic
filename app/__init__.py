from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)


@app.template_filter('formatdate')
def format_datetime(value, format="%d-%m-%Y"):
    """Фільтер для дат в шаблонах"""
    if value is None:
        return ""
    return value.strftime(format)
