from flask import Blueprint, render_template, current_app

# from web_app import render
from pluggs.blogs.models.MBlog import Blog
from web_app.models.pages import Page

bloghome_controller = Blueprint('bloghome_controller', __name__, template_folder='../views')


@bloghome_controller.route('/')
def index_blog():
    print('**** Access bloghome_controller ****')
    print('bloghome_controller Root Path:', bloghome_controller.root_path)
    print('current_app template path:', current_app.template_folder)
    blog_obj = Blog.query.get(1)
    title = 'Index Learning'
    blog2 = Blog()
    pages_ = blog2.page

    if pages_ is None:
        pages_ = Page.query.all()
        blog2.page = pages_

    if blog_obj is not None:
        title = blog_obj.title

    return render_template('input_layout.html', TITLE=title, CONTENT='Test aja', PARENT_VIEW=current_app.template_folder + '/dashboard/dashboard_layout.html')
