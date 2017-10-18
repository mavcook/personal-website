from flask import *
from sql import *
import os

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route('/contact', methods=['POST', 'GET'])
def main_route():
	
	return render_template("contact.html")