


class Parameters():


    projectMap = 'J:\Source\Datasets\HeuristicAllocationOfResources\ProjectMap.csv'
    projectForecast = 'J:\Source\Datasets\HeuristicAllocationOfResources\ProjectForecast.csv'
    groupCapacities = 'J:\Source\Datasets\HeuristicAllocationOfResources\GroupCaps.csv'

    #Number of weeks for which to plan the allocation
    planningHorizon = 312




    #Placeholders from old usage
    # Input by user
    planningHorizon = 312
    periodicity = 52
    numberOfClusters = 3
    clusterCapacity = [2100, 2100, 2100]
    numberOfObjectives = 3
    inputMethod = 'RS'  # [RS, EA, ...]
    calculationMethod = 'EA'  # [EA, RS, ...]
    algorithmIterations = 4
    freshRuns = 3
    populationSize = 8
    hyperVolumeInterval = 1
    setReferencePoint = [1872, 1872, 338]
    objective2Normalization = 2100
    tempProjects = 169
