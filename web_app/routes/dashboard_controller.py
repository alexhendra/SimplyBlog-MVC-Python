from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from web_app.models.pages import Page
from web_app.models.pluggins import Pluggine
from web_app.models.sites import Site

dashboard_controller = Blueprint('dashboard_controller', __name__, template_folder='templates')


@dashboard_controller.route('/')
def index_dashboard():
    plugins = Pluggine.query.filter_by(id=1).first()
    return render_template('/dashboard/dashboard_layout.html', TITLE='Index Learning', CONTENT='')


@dashboard_controller.route('/sites')
def get_sites_dashboard():
    return render_template('/dashboard/dashboard_sites_layout.html', Title='Sites Data')


@dashboard_controller.route('/sites', methods=['POST'])
def post_sites_dashboard():
    name_ = request.form['Name']
    post_ = Site(name=name_, createdby='Alex', createddate=datetime.now())
    post_.insert()

    return redirect(url_for('dashboard_controller.get_sites_dashboard'))


@dashboard_controller.route('/pages')
def get_pages_dashboard():
    page_ = Page.query.all()
    site_ = Site.query.all()
    return render_template('/dashboard/dashboard_pages_layout.html', Title='Pages Data', Pages=page_, Sites=site_)


@dashboard_controller.route('/pages', methods=['POST'])
def post_pages_dashboard():
    name_ = request.form['Name']
    siteId = request.form['Site']
    page_ = Page(name=name_, site_id=siteId, createdby='Alex', createddate=datetime.now())
    page_.insert()

    return redirect(url_for('dashboard_controller.get_pages_dashboard'))
