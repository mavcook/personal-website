from config import connect_to_database
db = connect_to_database('web')
cursor = db.cursor()


def getProjects(sort=None, tags=None):
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
	return cursor.fetchall()

def getProject(pid):
	pid = str(pid)
	cursor.execute('SELECT *, YEAR(date) as year FROM Project where project_id=%s', (pid,))
	return cursor.fetchone()

def getProjectMedia(pid):
	pid = str(pid)
	cursor.execute('SELECT directoryPath FROM Media WHERE project_id=%s', (pid,))
	return cursor.fetchall()

def getTags():
	cursor.execute('SELECT name as tag FROM PTags')
	return cursor.fetchall()