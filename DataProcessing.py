


from Parameters import Parameters
from ReadData import readInput
from BasicCalculations import calculateNumberOfPeriods, groupNormalization
from ProjectClass import projectClassInit
from GroupClass import groupClassInit, groupClassNormalized


def processProjects():

    #Read and transform project data into pandas dataframes
    dfProjectMap, dfProjectForecast, dfGroupCapacities = readInput()

    #Basic information about the data
    Parameters.numberOfProjects = len(dfProjectMap['Project'].unique())
    Parameters.numberOfGroups = len(dfGroupCapacities['Group'].unique())
    Parameters.numberOfWeeks = len(dfProjectForecast['WeeksFromStart'].unique())
    Parameters.groupCapacitiesArray = dfGroupCapacities['Capacity'].tolist()
    Parameters.numberOfPeriods = calculateNumberOfPeriods(Parameters.numberOfWeeks)

    #Initiate Project class
    projectList = projectClassInit(Parameters.numberOfProjects, dfProjectMap, dfProjectForecast)
    #Initiate Group class (non-normalized)
    groupList = groupClassInit(Parameters.numberOfGroups, projectList, Parameters.groupCapacitiesArray)
    #Normalize Group requests
    projectList = groupNormalization(groupList, projectList)
    #Create new Group class (normalized)
    newGroupList = groupClassNormalized(Parameters.numberOfGroups, Parameters.groupCapacitiesArray, projectList)

    return projectList, newGroupList


