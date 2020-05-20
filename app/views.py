from flask import render_template, Blueprint

views = Blueprint('views', __name__)

# route every path to Vue's SPA
@views.route('/', defaults={'path': ''})
@views.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
