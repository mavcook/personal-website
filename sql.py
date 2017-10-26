from config import connect_to_database


def sqlQuery(queryFunc):

	def openClose(*args):
		db = connect_to_database('web')
		cursor = db.cursor()
		args = args + (cursor,)

		results = queryFunc(*args)

		cursor.close()
		db.close()
		return results

	return openClose

@sqlQuery
def getProjects(cursor, sort=None, tags=None):

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
	return results

@sqlQuery
def getProject(pid, cursor):
	pid = str(pid)
	cursor.execute('SELECT *, YEAR(date) as year FROM Project WHERE project_id=%s LIMIT 1', (pid,))
	results = cursor.fetchone()
	return results

@sqlQuery
def getProjectMedia(pid, cursor):
	pid = str(pid)
	cursor.execute('SELECT directoryPath FROM Media WHERE project_id=%s', (pid,))
	results = cursor.fetchall()
	return results

@sqlQuery
def getTags(cursor):
	cursor.execute('SELECT name as tag FROM PTags')
	results = cursor.fetchall()
	return results
