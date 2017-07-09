import pandas as pd
import numpy as np

from Parameters import Parameters

def readInput():

    #GROUP TO CLUSTER MAPPING
    dfProjectMap = pd.read_csv(Parameters.projectMap)
    #Transform group string into integer
    dfProjectMap['group'] = dfProjectMap['group'].map(lambda x: int(x[6:]))
    #Transform project string into integer
    dfProjectMap['project'] = dfProjectMap['project'].map(lambda x: int(x[8:]))
    #Sort dataframe by project and reset index
    dfProjectMap.sort_values(by='project', inplace=True)
    dfProjectMap = dfProjectMap.reset_index(drop=True)
    dfProjectMap.columns = ['Group', 'Project']

    #PROJECT USAGE FORECAST
    dfProjectForecast = pd.read_csv(Parameters.projectForecast)
    #Transform strings into integers
    dfProjectForecast['week'] = dfProjectForecast['week'].map(lambda x: int(x[1:]))
    dfProjectForecast['year'] = dfProjectForecast['year'].map(lambda x: int(x[1:]))
    dfProjectForecast['project'] = dfProjectForecast['project'].map(lambda x: int(x[8:]))
    dfProjectForecast['slots'] = dfProjectForecast['slots'].astype(np.int64)
    #Calculate week distance from week t = 0 (week 1 year 1 = 1)
    dfProjectForecast['WeeksFromStart'] = dfProjectForecast['week'] + (dfProjectForecast['year'] - 1) * 52
    dfProjectForecast['WeeksFromStart'] = dfProjectForecast['WeeksFromStart'].map(lambda x: int(x))
    #Remove week and year columns
    dfProjectForecast.drop('week', axis=1, inplace=True)
    dfProjectForecast.drop('year', axis=1, inplace=True)
    #Caclculate number of projects
    numberOfProjects = len(dfProjectForecast['project'].unique())
    #Remove project-weeks not in planning horizon
    dfProjectForecast = dfProjectForecast.loc[dfProjectForecast['WeeksFromStart'] <= Parameters.planningHorizon]
    dfProjectForecast.reset_index(inplace=True, drop=True)
    dfProjectForecast.columns = ['Project', 'Slots', 'WeeksFromStart']

    #GROUP MAXIMUM CAPACITIES
    dfGroupCapacities = pd.read_csv(Parameters.groupCapacities)
    #Transform strings into integers
    dfGroupCapacities['group'] = dfGroupCapacities['group'].map(lambda x: int(x[6:]))
    dfGroupCapacities['cap'] = dfGroupCapacities['cap'].map(lambda x: int(x))
    #Group capacities ordered array
    dfGroupCapacities.sort_values(by='group', inplace=True)
    groupCapacityList = dfGroupCapacities['cap'].tolist()

    return dfProjectMap, dfProjectForecast, dfGroupCapacities, numberOfProjects, groupCapacityList
