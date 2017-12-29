from datetime import datetime
import importlib
from flask import Flask, render_template, request, flash, redirect, url_for
from web_app.models import db
from web_app.models.sites import Site
from web_app.models.users import User
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
        print('initialize_database execute!!')
        db.create_all()

        # plugs_ = importlib.import_module('pluggs.blogs.blog_app')
        # plugs_.load_plugin(current_app)

    @app.route('/')
    def index():
        site_ = Site.query.filter_by(id=1).first()

        if site_ is not None:
            return render_template('base_layout.html', Title='Index Learning', Content='''
                    <div class="starter-template">
                        <h1>Welcome to my page !!</h1>
                        <p class="lead">Learning by Doing !!!</p>
                    </div>
                ''', SITE=site_.name)
        else:
            return render_template('base_layout.html', Title='Index Learning', Content='''
                    <div class="starter-template">
                        <h1>Welcome to my page !!</h1>
                        <p class="lead">Learning by Doing !!!</p>
                    </div>
                ''')

    @app.route('/about')
    def about():
        return render_template('about.html', Title='Index Learning')

    @app.route('/login')
    def login_user():
        return render_template('login_layout.html', Title='Login Form')

    @app.route('/register')
    def get_register_user():
        return render_template('register_layout.html', Title='Register Form')

    @app.route('/register', methods=['POST'])
    def post_register_user():
        userid_ = request.form['registerUserid']
        username_ = request.form['registerUsername']
        useremail_ = request.form['registerEmail']
        userpass_ = request.form['registerPassword']
        userconfirmpass_ = request.form['registerConfirmpassword']
        useragreelicense_ = request.form['agreelicense']

        if userpass_ != userconfirmpass_:
            flash('Password not match with Confirm Password', 'danger')
            return redirect(url_for('get_register_user'))

        users = User(userid=userid_, email=useremail_, name=username_, createdby=userid_, createddate=datetime.now())
        users.insert()

        sites_ = Site(name=username_ + ' Site', createdby=userid_, createddate=datetime.now())
        sites_.insert()

        print('Register success!')

        flash('Register successfully.', 'success')
        return redirect(url_for('get_register_user'))

    return app
