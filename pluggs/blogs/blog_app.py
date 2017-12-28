from pluggs.blogs import load_custom_jinja2_env
from pluggs.blogs.routes.blogs_home_controller import bloghome_controller


def load_plugin(app):
    print('**** Load Plugin Section ****')
    print('App Root Path:', app.root_path)
    app.register_blueprint(bloghome_controller, url_prefix="/dashboard/blog")
    load_custom_jinja2_env(app, bloghome_controller.name)

