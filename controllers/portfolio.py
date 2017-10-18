from flask import *
import sql
import urllib

portfolio = Blueprint('portfolio', __name__, template_folder='templates')
SORT_OPTIONS = ['newest', 'oldest']


# returns basic data about a project
def getProjectCard(sortBy=None, tags=None):
	kwargs = {}
	if sortBy and sortBy in SORT_OPTIONS:
		if sortBy == 'newest':
			kwargs['sort'] = 'DESC'
		else:
			kwargs['sort'] = 'ASC'
	if tags:
		kwargs['tags'] = [urllib.parse.unquote_plus(t) for t in tags]

	projects = sql.getProjects(**kwargs)

	# get abs urls
	for i in range(len(projects)):
		tn = projects[i]['thumbnail']
		projects[i]['thumbnail'] = url_for('static', filename=tn) #TODO:
	return projects

@portfolio.route('/portfolio', methods=['GET', 'POST'])
def main_route():

	kwargs = {}

	if request.method == 'GET':
		if 'tags' in request.args:
			tags = request.args['tags']
			kwargs['tags'] = tags.split(':')
		if 'sort' in request.args:
			kwargs['sortBy'] = request.args['sort']
			# sanitize
		#if 'access' in request.args:

	projects = getProjectCard(**kwargs)
	availableTags = sql.getTags() # returns all tags
	requestedTags = kwargs.get('tags', [])

	data = {
		'projects' : projects,
		'availableTags' : availableTags,
		'requestedTags' : requestedTags
	}
	return render_template("portfolio.html", **data)