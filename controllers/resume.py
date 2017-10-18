from flask import *
from sql import *
import hashlib
import os

resume = Blueprint('resume', __name__, template_folder='templates')



@resume.route('/resume')
def main_route():
	return render_template("resume.html")
