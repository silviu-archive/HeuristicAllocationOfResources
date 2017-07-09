


from Parameters import Parameters
from ReadData import readInput
from BasicCalculations import calculateNumberOfPeriods, groupNormalization
from ProjectClass import projectClassInit
from GroupClass import groupClassInit, groupClassNormalized


def main():


    #Read and transform project data into pandas dataframes
    dfProjectMap, dfProjectForecast, dfGroupCapacities = readInput()

    #Basic information about the data
    numberOfProjects = len(dfProjectMap['Project'].unique())
    numberOfGroups = len(dfGroupCapacities['Group'].unique())
    numberOfWeeks = len(dfProjectForecast['WeeksFromStart'].unique())
    groupCapacities = dfGroupCapacities['Capacity'].tolist()
    numberOfPeriods = calculateNumberOfPeriods(numberOfWeeks)

    #Initiate Project class
    projectList = projectClassInit(numberOfProjects, dfProjectMap, dfProjectForecast)
    #Initiate Group class (non-normalized)
    groupList = groupClassInit(numberOfGroups, projectList, groupCapacities)
    #Normalize Group requests
    projectList = groupNormalization(groupList, projectList)
    #Create new Group class (normalized)
    newGroupList = groupClassNormalized(numberOfGroups, groupCapacities, projectList)


    print('x')










if __name__ == '__main__':
    main()