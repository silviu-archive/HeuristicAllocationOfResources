#Contains all the information about a project
class projectClass():
	#Initialize project with project number
	def __init__ (self, project):
		self.project = project
	#Define project cluster assignment
	def clusterAssignment(self, cluster):
		self.cluster = cluster
	#Define project group assignment
	def groupAssignment(self, group):
		self.group = group
	#Define weeks in which project is running
	def weeklyTaskList(self, runningWeeks):
		self.runningWeeks = runningWeeks
	#Define project usage over runtime
	def weeklyUsageList(self, usage):
		self.usage = usage
	#Method to get usage in a particular week
	def getWeeklyUsage(self, week):
		try:
			specificWeek = self.runningWeeks.index(week)
			return self.usage[specificWeek]
		except ValueError:
			print('No usage in week '+str(week))
	#Calculate total project usage
	def totalUsage(self):
		self.total = 0
		if self.usage == ['No usage']:
			self.total = 0
		else:
			for i in self.usage:
				self.total += i
	#Calculate project horizon
	def projectHorizon(self):
		self.horizon = 0
		for i in self.runningWeeks:
			self.horizon += 1
	#Calculate project average usage over horizon
	def averageUsage(self):
		self.average = 0
		if self.usage == ['No usage']:
			self.total = 0
		else:
			for i in self.usage:
				self.average += i
		self.average = self.average / self.horizon
	#Define new project usage after normalization
	def normUsage(self, newUsage, week):
		self.usage[self.runningWeeks.index(week)] = newUsage
	#Reset project cluster
	def cleanup(self):
		self.cluster = -1

#Initializes a list of projects with information currently available
def projectClassInit(numberOfProjects, dfProjectMap, dfProjectForecast):

	#Initiates projects (from 1 to 169, but index in list starts from 0)
	projectList = [projectClass(i) for i in range(1, numberOfProjects+1)]
	#Assigns project's group
	for index, row in dfProjectMap.iterrows():
		projectList[index].groupAssignment(row[0])
	#Specify the weeks in which each project is running, and the relevant slot usage
	for name, group in dfProjectForecast.groupby('Project'):
		projectList[group['Project'].iloc[0]-1].weeklyTaskList(group['WeeksFromStart'].tolist())
		projectList[group['Project'].iloc[0]-1].weeklyUsageList(group['Slots'].tolist())
		print('x')
	for project in projectList:
		if not hasattr(project, 'runningWeeks'):
			project.runningWeeks = ['Not in planning']
		if not hasattr(project, 'usage'):
			project.usage = ['No usage']

	return projectList