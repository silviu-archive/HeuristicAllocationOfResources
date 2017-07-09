from Parameters import Parameters

#Function to calculate the number of periods for the current selected number of analyzed weeks
def calculateNumberOfPeriods(numberOfWeeks):
    numberOfPeriods = 0
    if numberOfWeeks % Parameters.periodicity != 0:
        numberOfPeriods = int(numberOfWeeks / Parameters.periodicity) + 1
    else:
        numberOfPeriods = int(numberOfWeeks / Parameters.periodicity)
    return  numberOfPeriods

def groupNormalization(groupList, projectList):
    # Normalize group requests
    for group in groupList:
        for week in group.weeks:
            if group.getGroupWeeklyUsage(week) > group.capacity:
                for project in projectList:
                    if project.group == group.group and week in project.runningWeeks:
                        project.normUsage(int(project.getWeeklyUsage(week) /
                                              (group.getGroupWeeklyUsage(week) / group.capacity)),
                                          week)

    return projectList