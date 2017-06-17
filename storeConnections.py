# storeConnections.py
#
# A program to generate a unique list of city networks
#
# Parameters:
# neighborMap: a map of each city name to its list of neighbors. type: {String, [String]}
#
# Ian Marx, June 2017

from collections import Counter
from findConnections import findConnections

# citation in README.md
def compare(list1, list2):
    return Counter(list1) == Counter(list2)

# generate a list of unique city networks
def storeConnections(neighborMap):
    connectionsList = []

    for currentCity in neighborMap:
        visitedCities = []
        currentNetwork = findConnections(currentCity, visitedCities, neighborMap)

        connectionsList.append(currentNetwork)

    uniqueList = []
    for network in connectionsList:
        if len(uniqueList) == 0:
            uniqueList.append(network)
        else:
            counter = 0
            for item in uniqueList:
                if compare(network, item) == True:
                    counter += 1

            if counter == 0:
                uniqueList.append(network)

    return uniqueList
