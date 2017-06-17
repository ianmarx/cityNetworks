# findConnections.py
#
# A recursive function to build a list of connected cities (see README.md)
#
# Parameters:
# currentCity: a city name. type: String
# visitedCities: an array of visited city names. type: [String]
# neighborMap: a map of each city name to its list of neighbors. type: {String, [String]}
#
# Ian Marx, June 2017

def findConnections(currentCity, visitedCities, neighborMap):

    # base case: return if the city has been visited
    if currentCity in visitedCities:
        return

    # recursive case: otherwise, keep adding cities
    else:
        visitedCities.append(currentCity)

        # recurse through all neighbors of the current city
        for neighbor in neighborMap[currentCity]:
            findConnections(neighbor, visitedCities, neighborMap)

    return visitedCities
