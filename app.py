from flask import Flask, render_template, url_for, g, request
import extensions
import controllers
import config
import os

#TODO:
# get rid of or fix js image optomization (cookies)
# animation reminder for logo (bounce click me)
# animation for logo when hard scroll to top
# change bg image every page reload until cookie is set
# change logo color
# new decsriptions for each media piece in project view
# sortBy button
# resume icons are cut off
# padding for html pv
# cleanup other bad code
# minifyer (css, js, combines into one file to save http req?)
# profile js, flask

app = Flask(__name__, template_folder='templates', static_folder='static')


# Register the controllers
app.register_blueprint(controllers.contact)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.portfolio)
app.register_blueprint(controllers.resume)
app.register_blueprint(controllers.view)

# Key for sessions (very secure)
app.secret_key = 'Barnburner Lullaby'


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.template_global()
# TODO: cleanup, super hacky
# adds and removes tags for limiting portfolio projects
def addGETTag(newtag):
	delim = ':'
	args = request.args.copy()

	if 'tags' not in args:
		args['tags'] = newtag
	elif newtag not in args['tags'].split(delim):
		args['tags'] = args['tags'] + delim + newtag
	else: # remove tag
		if len(args['tags'].split(delim)) == 1:
			return url_for('portfolio.main_route')
		else:
			rep = delim + newtag
			if args['tags'].split(delim)[0] == newtag:
				rep = newtag + delim
			args['tags'] = args['tags'].replace(rep, '')

	return url_for('portfolio.main_route', **args)


@app.template_global()
def getExt(filename):
	filename, ext = os.path.splitext(filename)
	return ext


@app.template_global()
def rawME(filename):
	with open(filename, 'r') as f:
		return f.read()



@app.before_request
def getCurrent():
	global hImgs
	global PAGES

	hImgs = [
		{
			'active': 'active',
			'src': url_for('static', filename='media/bg/00_small.jpg'),
			'alt': 'Cloud Steps by Maverick Cook'
		},
		{
			'active': '',
			'src': url_for('static', filename='media/bg/01_small.jpg'),
			'alt': 'Mushrooms by Maverick Cook'
		},
		{
			'active': '',
			'src': url_for('static', filename='media/bg/02_small.jpg'),
			'alt': 'Macro Guitar Strings by Maverick Cook'
		},
		{
			'active': '',
			'src': url_for('static', filename='media/bg/03_small.jpg'),
			'alt': 'Traverse City Stars by Maverick Cook'
		},
		{
			'active': '',
			'src': url_for('static', filename='media/bg/04_small.jpg'),
			'alt': 'Macro Tree Stump by Maverick Cook'
		}
	]

	PAGES = {
		'index': ('Home', url_for('main.main_route')),
		'pf': ('Portfolio', url_for('portfolio.main_route')),
		'res': ('Resume', url_for('resume.main_route')),
		'contact': ('Contact', url_for('contact.main_route')),
		'faq': ('FAQ', url_for('main.faq_route')),
		'jy': ('The Junkyard', url_for('main.junkyard_route'))
	}


	if 'hImg' not in request.cookies:
		hImgs[0]['active'] = 'active'
	else:
		for i in range(len(hImgs)):
			if 'i' + str(i) == request.cookies['hImg']:
				hImgs[i]['active'] = 'active'
			else:
				hImgs[i]['active'] = ''
	g.hImgs = hImgs


# Globals needed for base.html
@app.context_processor
def inject_user():

	navPages = [
		PAGES['index'],
		PAGES['pf'],
		PAGES['res'],
		PAGES['contact']
	]

	evenMore = [
		PAGES['faq'],
		PAGES['jy']
	]

	URLS = {
		'logo': url_for('static', filename='media/metram_logo_solid_highres.png'),
		'logoWM' : url_for('static', filename='media/metram_watermark_solid_highres.png'),
		'favicon': url_for('static', filename='media/favicon.png'),

	}

	return dict(navPages=navPages, evenMore=evenMore, URLS=URLS)

# Listen on external IPs
if __name__ == '__main__':
	if len(sys.argv) > 1: # only arguments will be pased to development
		app.run(host=config.webEnv['host'], port=config.webEnv['port'], debug=True)
	else:
		app.run()
	
