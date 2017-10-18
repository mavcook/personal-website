from flask import *
from sql import *


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def main_route():
	return render_template("index.html")

@main.route('/faq')
def faq_route():
	return render_template("faq.html")

@main.route('/', subdomain='junkyard')
def junkyard_route():
	return render_template("junkyard.html")
