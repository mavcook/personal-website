from flask import *
import sql
import os

view = Blueprint('view', __name__, template_folder='templates')

SORT_OPTIONS = ['newest', 'oldest']
mediaEls = {
	'video': { 
		'ext': ['.mp4', 'ocg'], 
		'pre_html': Markup('<video controls width="100%" height="100%" src="'),
		'post_html': Markup('"/>')
	},
	'pic': { 
		'ext': ['.png', '.jpg', '.gif'], 
		'pre_html': Markup('<div class="center wAuto"><img src="'),
		'post_html': Markup('"/></div>')
	},
	'html': { 'ext': '.html'}
}

def getProjectMedia(pid, split=False, url=False):
	mediaDirs = sql.getProjectMedia(pid)
	final = []

	for x in mediaDirs:
		filepath = os.path.join('static', x['directoryPath'])
		files = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
		files.sort()
		files = [os.path.join(x['directoryPath'], f) for f in files]
		if url is True:
			files = [url_for('static', filename=i) for i in files]
		if split is True:
			final.append(files)
		else:
			final += files

	# TODO: have caption file associated with each media
	return final
import itertools


def gallery(project):

	pid = project['project_id']
	# should be two entries for media directories in a gallery
	media, thumbnails = getProjectMedia(pid, url=True, split=True)

	# convert to list of tuples (media[n], thumb[n])
	mediaPkg = list(itertools.zip_longest(media, thumbnails))
	
	data = {
		'mediaEls': mediaEls,
		'media': mediaPkg,
		'title': project['title'],
		'year': project['year'],
		'description': project['description'],
		'requesterURL': request.referrer
	}
	
	return data

@view.route('/portfolio/view/<name>', methods=['GET'])
# name is just for identifying links that will be broken if pid changes
def main_route(name):

	kwargs = {}

	if request.method == 'GET':
		if 'p' in request.args:
			pid = request.args['p']
			try:
				pid = int(pid)
			except:
				abort(404)
			project = sql.getProject(pid)
			if project == None:
				abort(404)
	else:
		abort(404)

	if project['type'] == 'GAL':
		data = gallery(project)
		return render_template("gallery.html", **data)
		
	
	data = {
		'mediaEls': mediaEls,
		'media': getProjectMedia(pid),
		'title': project['title'],
		'year': project['year'],
		'description': project['description'],
		'requesterURL': request.referrer
	}
	
	return render_template("projectView.html", **data)