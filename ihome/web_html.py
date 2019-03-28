from flask import Blueprint,current_app,make_response
from flask_wtf import csrf
html = Blueprint("web_html", __name__)


@html.route("/<re(r'.*'):filename>")
def get_html(filename):
    if not filename:
        filename = 'index.html'

    if filename != 'favicon.ico':
        filename = 'html/' + filename

    resp= make_response(current_app.send_static_file(filename))
    csrf_token = csrf.generate_csrf()
    resp.set_cookie("csrf_token", csrf_token)

    return resp