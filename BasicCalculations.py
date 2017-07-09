from Parameters import Parameters

#Function to calculate the number of periods for the current selected number of analyzed weeks
def calculateNumberOfPeriods(numberOfWeeks):
    numberOfPeriods = 0
    if numberOfWeeks % Parameters.periodicity != 0:
        numberOfPeriods = int(numberOfWeeks / Parameters.periodicity) + 1
    else:
        numberOfPeriods = int(numberOfWeeks / Parameters.periodicity)
    return  numberOfPeriods