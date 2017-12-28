import jinja2
import os


# https://stackoverflow.com/questions/2180247/does-the-jinja2-templating-language-have-the-concept-of-here-current-director
# https://stackoverflow.com/questions/13598363/how-to-dynamically-select-template-directory-to-be-used-in-flask
def load_custom_jinja2_env(app, controller_name):
    # print('os.path.dirname(__file__):', os.path.dirname(__file__))
    # print('os.path.join(app.root_path, "templates")', os.path.join(app.root_path, 'templates'))
    # print('os.path.join(os.path.dirname(__file__), "views")', os.path.join(os.path.dirname(__file__), 'views'))

    if controller_name is not None:
        blueprint = app.blueprints[controller_name]
        print('blueprint.template_folder:', blueprint.template_folder)

        loader = jinja2.FileSystemLoader(
            [os.path.join(app.root_path, 'templates'),
             blueprint.template_folder])
    else:
        loader = jinja2.FileSystemLoader(os.path.join(app.root_path, 'templates'))

    jinja2.Environment(loader)
