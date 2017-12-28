from flask import Blueprint, render_template, abort

from web_app.models.authorizt import Authorizt
from web_app.models.users import User

page_controller = Blueprint('page_controller', __name__, template_folder='templates')


@page_controller.route('/')
def index_page():
    auth_ = Authorizt.query.filter_by(id=1).first()
    user_ = User.query.filter_by(email='alex').first()
    #if user_ is not None and auth_ is not None:
    return render_template('/page/page_layout.html', TITLE='Index Learning', CONTENT='')
    #else:
    #    abort(404)
