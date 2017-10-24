from config import connect_to_database
db = connect_to_database('web')


def getProjects(sort=None, tags=None):
	cursor = db.cursor()
	
	baseQ = 'SELECT *, YEAR(date) as year FROM Project'
	args = None

	if tags:
		tagQuery = """
		WHERE Project.project_id in (
			SELECT TagsToProject.project_id
			FROM TagsToProject
			INNER JOIN PTags on TagsToProject.ptag_id = PTags.ptag_id
			WHERE PTags.name in ({})
			GROUP BY TagsToProject.project_id
			HAVING COUNT(DISTINCT PTags.name) = {}
		)
		"""
		tagFormat = '%s, ' * (len(tags) - 1) + '%s'
		baseQ += tagQuery.format(tagFormat, len(tags))

		args = tuple(tags)
	if sort:
		baseQ += ' ORDER BY Project.date ' + sort
		args = ()
	if sort and tags:
		args = tuple(tags)
	
	if args == None:
		baseQ += ' ORDER BY project_seq ASC'

	cursor.execute(baseQ, args)
	results = cursor.fetchall()
	cursor.close()
	return results

def getProject(pid):
	cursor = db.cursor()
	pid = str(pid)
	cursor.execute('SELECT *, YEAR(date) as year FROM Project WHERE project_id=%s LIMIT 1', (pid,))
	results = cursor.fetchone()
	cursor.close()
	return results

def getProjectMedia(pid):
	cursor = db.cursor()
	pid = str(pid)
	cursor.execute('SELECT directoryPath FROM Media WHERE project_id=%s', (pid,))
	results = cursor.fetchall()
	cursor.close()
	return results

def getTags():
	cursor = db.cursor()
	cursor.execute('SELECT name as tag FROM PTags')
	results = cursor.fetchall()
	cursor.close()
	return results