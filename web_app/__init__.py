import os

import jinja2


# http://matthiaseisen.com/pp/patterns/p0198/
def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    print('path:', path)
    print('filename:', filename)
    print('current directory:', os.getcwd())

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('/web_app/web_app/templates/dashboard' or './')
    ).get_template(filename).render(context)
