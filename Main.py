


from Parameters import Parameters
from ReadData import readInput
from BasicCalculations import calculateNumberOfPeriods
from ProjectClass import projectClassInit
from GroupClass import groupClassInit


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


    print('x')










if __name__ == '__main__':
    main()