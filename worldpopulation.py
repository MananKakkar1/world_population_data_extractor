import csv

def getLifeExpectancyData(filename):

    someDict = {}
    
    with open(filename, 'r') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            if line['country'] not in someDict:
                #Checks if the country is not in the list and creates keys for that country since it did not exist before
                someDict[line['country']] = {}
                someDict[line['country']]['Life Expectancy - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Iq'] = []
                someDict[line['country']]['Population Density - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Weight'] = []
                someDict[line['country']]['Life Expectancy - Weight'] = []
                
            #Creating a temporary tuple which stores male and female life expectancy
            tempTuple = (float(line['male_life_expectancy']), float(line['female_life_expectancy']))
            #Appending Life Expectancy Data to the list in the dictionary at its corresponding key
            someDict[line['country']]['Life Expectancy - Quality Of Life'].append(tempTuple)
            someDict[line['country']]['Life Expectancy - Weight'].append(tempTuple)

        return someDict
def getQualityOfLifeData(filename, someDict):

    with open(filename, 'r') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:
            #Creating a temporary tuple to store all of the quality of life data that the application could potentially use
            tempTuple = (int(line['stability']),
                        int(line['rights']),
                        int(line['health']),
                        int(line['safety']),
                        int(line['climate']),
                        int(line['costs']),
                        int(line['popularity']))

            if line['country'] not in someDict:
                #Checks if the country is not in the list and creates keys for that country since it did not exist before
                someDict[line['country']] = {}
                someDict[line['country']]['Life Expectancy - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Iq'] = []
                someDict[line['country']]['Population Density - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Weight'] = []
                someDict[line['country']]['Life Expectancy - Weight'] = []

            #Appending and adding Quality Of Life Data to its specific keys in a dictionary
            someDict[line['country']]['Quality Of Life - Iq'] = [tempTuple]
            someDict[line['country']]['Life Expectancy - Quality Of Life'].append(tempTuple)
            someDict[line['country']]['Population Density - Quality Of Life'].append(tempTuple)
            someDict[line['country']]['Quality Of Life - Weight'].append(tempTuple)
    
    
        return someDict

def getIqData(filename, someDict):
    
    with open(filename, 'r') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            if line['country'] not in someDict:
                #Checks if the country is not in the list and creates keys for that country since it did not exist before
                someDict[line['country']] = {}
                someDict[line['country']]['Life Expectancy - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Iq'] = []
                someDict[line['country']]['Population Density - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Weight'] = []
                someDict[line['country']]['Life Expectancy - Weight'] = []
            #Creating a temporary tuple which stores IQ data 
            tempTuple = (int(line['iq']), 0)
            #Appends IQ Data to the list in dictionary at its corresponding key
            someDict[line['country']]['Quality Of Life - Iq'].append(tempTuple)
            
        return someDict

def getPopulationDensityData(filename, someDict):
    
    with open(filename, 'r') as fileIn:

         reader = csv.DictReader(fileIn)

         for line in reader:

             if line['country'] not in someDict:
                #Checks if the country is not in the list and creates keys for that country since it did not exist before
                 someDict[line['country']] = {}
                 someDict[line['country']]['Life Expectancy - Quality Of Life'] = []
                 someDict[line['country']]['Quality Of Life - Iq'] = []
                 someDict[line['country']]['Population Density - Quality Of Life'] = []
                 someDict[line['country']]['Quality Of Life - Weight'] = []
                 someDict[line['country']]['Life Expectancy - Weight'] = []
            #Creating a temporary tuple which stores the population density data 
             tempTuple = (float(line['pop_per_km_sq']), 0)
            #Appends the population density data to the list in the dictionary at its corresponding key
             someDict[line['country']]['Population Density - Quality Of Life'].append(tempTuple)

         return someDict
def getHeightWeightData(filename, someDict):
    
    with open(filename, 'r') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:
            
            if line['country'] not in someDict:
                #Checks if the country is not in the list and creates keys for that country since it did not exist before
                someDict[line['country']] = {}
                someDict[line['country']]['Life Expectancy - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Iq'] = []
                someDict[line['country']]['Population Density - Quality Of Life'] = []
                someDict[line['country']]['Quality Of Life - Weight'] = []
                someDict[line['country']]['Life Expectancy - Weight'] = []
            #Creating a temporary tuple which stores male and female weight data 
            someTuple = (float(line['male_weight']), float(line['female_weight']))
            #Appending Weight Data for Quality of Life - Weight Graph to the list in the dictionary at its corresponding key
            someDict[line['country']]['Quality Of Life - Weight'].append(someTuple)
            #Appending Weight Data for Life Expectancy - Weight Graph to the list in the dictionary at its corresponding key
            someDict[line['country']]['Life Expectancy - Weight'].append(someTuple)

        return someDict    
def printFinalDict(someDict):
    #Function created to print dictionary to console in an organized manner.
    for k in someDict.keys():
        print(f'{k}')
        print(f'{someDict[k]}\n')
        

def main():
    #Calling all functions
    lifeExpectancyData = getLifeExpectancyData('life_expectancy.csv')

    qualityOfLifeData = getQualityOfLifeData('quality_of_life.csv', lifeExpectancyData)

    iqData = getIqData('iq.csv', qualityOfLifeData)

    populationDensityData = getPopulationDensityData('population_density.csv', iqData)

    finalDict = getHeightWeightData('height_weight_data.csv', populationDensityData)

    #print(finalDict)

    printFinalDict(finalDict)
main()


