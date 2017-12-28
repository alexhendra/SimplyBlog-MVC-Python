import importlib

from flask import Flask, render_template

from web_app.models import db
from web_app.models.sites import Site
from web_app.routes.dashboard_controller import dashboard_controller
from web_app.routes.page_controller import page_controller


def create_app():
    app = Flask(__name__)

    # config diambil dari python file settings.py
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    app.register_blueprint(page_controller,  url_prefix="/page")
    app.register_blueprint(dashboard_controller,  url_prefix="/dashboard")

    plugs_ = importlib.import_module('pluggs.blogs.blog_app')
    plugs_.load_plugin(app)

    # https://stackoverflow.com/questions/19008260/pythonic-way-to-correctly-separate-model-from-application-using-sqlalchemy
    # Ini digunakan untuk membentuk current context ketika request pertama kali
    @app.before_first_request
    def initialize_database():
        db.create_all()

        # plugs_ = importlib.import_module('pluggs.blogs.blog_app')
        # plugs_.load_plugin(current_app)

    @app.route('/')
    def index():
        site_ = Site.query.filter_by(id=1).first()

        if site_ is not None:
            return render_template('base_layout.html', TITLE='Index Learning', CONTENT='''
                    <div class="starter-template">
                        <h1>Welcome to my page !!</h1>
                        <p class="lead">Learning by Doing !!!</p>
                    </div>
                ''', SITE=site_.name)
        else:
            return render_template('base_layout.html', TITLE='Index Learning', CONTENT='''
                    <div class="starter-template">
                        <h1>Welcome to my page !!</h1>
                        <p class="lead">Learning by Doing !!!</p>
                    </div>
                ''')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Index Learning')

    return app
