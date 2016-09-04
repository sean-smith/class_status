import requests

class person:
	def __init__(self, name, email, cell):
		self.name = name
		self.email = email
		self.cell = cell

class class_attr:
	def __init__(self, year, semester, school, dept, num):
		self.year = year
		self.semester = semester
		self.school = school
		self.dept = dept
		self.num = num

	def id(self):
		return '%d%s%s%s%d' % (self.year, self.semester.upper(), self.school.upper(), self.dept.upper(), self.num)

ENDPOINT = "https://www.bu.edu/phpbin/summer/rpc/openseats.php"

# poll based on a list of classes
def poll(classes):

	data = {}

	index = 0
	params = ''
	for class_attr in classes:
		params += 'sections[%d]=%s' % (index, class_attr.id())
		index += 1

	print params

	r = requests.get('%s?%s' % (ENDPOINT, params))

	print r.url
	print r.json()
	



# Send a notification with class info
def notify(person, class_attr):
	return 1



class1 = class_attr(2016, "fall", "cas", "cs", 410)

poll([class1])
