# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


# Define the WSGI application object
app = Flask(__name__)

login_manager = LoginManager()

# Configurations
app.config.from_object('config')
login_manager.init_app(app)
from flask import redirect


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


app.config['DEBUG'] = True
# Importing of variable necessary for creating blueprint
from views.main_view import main
from views.historico_view import historico
from views.login_view import login
from views.logout_view import logout
from views.tags_view import tags

# Creating blueprint for recipe route
app.register_blueprint(main)
app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(historico)
app.register_blueprint(historico, url_prefix='/historico')
app.register_blueprint(login)
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(logout)
app.register_blueprint(logout, url_prefix='/logout')
app.register_blueprint(tags)
app.register_blueprint(tags, url_prefix='/tags')
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()

