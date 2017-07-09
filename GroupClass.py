from Parameters import Parameters

#Contains all information about a group
class groupClass():
	#Initialize group with group number
	def __init__(self, group, planningHorizon):
		self.group = group
		self.usage = [0] * planningHorizon
		self.projects = []
		self.clusterAllocation = []
	#Define the weeks for the group
	def groupWeeks(self, weeks):
		self.weeks = weeks
	#Define group weekly usage
	def groupWeeklyUsage(self, usageInWeek, week):
		if not isinstance(usageInWeek, str):
			self.usage[week - 1] += usageInWeek
	#Method to get group weekly usage
	def getGroupWeeklyUsage(self, week):
		try:
			specificWeek = self.weeks.index(week)
			return self.usage[specificWeek]
		except ValueError:
			print('No usage in week ' + str(week))
	#Define group capacity
	def groupCapacity(self, capacity):
		self.capacity = capacity
	#Define projects in group
	def projectsInGroup(self, newProject):
		self.projects.append(newProject)
	#Define cluster allocation
	def projectCluster(self, cluster):
		self.clusterAllocation.append(cluster)


#Initializes a list of groups with information currently available
def groupClassInit(numberOfGroups, projectList, groupCapacities):
	#Initiate groups (from 1 to 5, but index in list starts from 0)
	groupList = [groupClass(i, Parameters.planningHorizon) for i in range(1, numberOfGroups+1)]
	#Initiate group capacities and running weeks
	for group in groupList:
		group.groupCapacity(groupCapacities[group.group-1])
		group.groupWeeks(list(range(1, Parameters.planningHorizon+1)))
	#Caclulate group weekly usage
	for project in projectList:
		#Get a project's running weeks
		projectWeeks = project.runningWeeks
		#Iterate over running weeks
		for i in projectWeeks:
			#Get project usage in a particular week
			projectUsage = project.getWeeklyUsage(i)
			#Add project usage to the relevant group
			groupList[project.group-1].groupWeeklyUsage(projectUsage, i)

	return groupList