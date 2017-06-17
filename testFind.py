# testFind.py
#
# A program to test findConnections()
#
# Ian Marx, June 2017

from findConnections import findConnections

print("\nfindConnections() testing")

# Test 1: Two groups (East and West Coasts) joined by a link (Detroit)
testMap1 = {}
testMap1["New York City"] = ["Boston", "Detroit"]
testMap1["Los Angeles"] = ["San Francisco", "Detroit"]
testMap1["Boston"] = ["New York City"]
testMap1["Detroit"] = ["New York City", "Los Angeles"]
testMap1["San Francisco"] = ["Los Angeles"]

origin = "New York City"
visitedCities = []
connectedCities = findConnections(origin, visitedCities, testMap1)

print("\nTest 1: One network")
print("Should contain: New York City, Los Angeles, Boston, Detroit, San Francisco")
print("Actual list: " + str(connectedCities))
print("\n")

# Test 2: Test a map of two separate networks of cities
testMap2 = {}

# West Coast network
testMap2["Los Angeles"] = ["San Francisco", "San Jose", "Las Vegas"]
testMap2["San Francisco"] = ["Sacramento", "Los Angeles"]
testMap2["Sacramento"] = ["San Francisco"]
testMap2["San Jose"] = ["Los Angeles"]
testMap2["Las Vegas"] = ["Los Angeles", "Salt Lake City"]
testMap2["Salt Lake City"] = ["Las Vegas", "Boise"]
testMap2["Boise"] = ["Salt Lake City"]

# East Coast network
testMap2["New York City"] = ["Boston", "Philadelphia", "Newark"]
testMap2["Boston"] = ["New York City", "Concord", "Providence"]
testMap2["Philadelphia"] = ["New York City", "Newark"]
testMap2["Newark"] = ["New York City", "Philadelphia"]
testMap2["Concord"] = ["Boston"]
testMap2["Providence"] = ["Boston"]

# test West Coast network from 3 different starting points
origin = "Los Angeles"
visitedCities = []
connectedWestCities1 = findConnections(origin, visitedCities, testMap2)

origin = "Sacramento"
visitedCities = []
connectedWestCities2 = findConnections(origin, visitedCities, testMap2)

origin = "Boise"
visitedCities = []
connectedWestCities3 = findConnections(origin, visitedCities, testMap2)

# test East Coast network from 3 different starting points
origin = "New York City"
visitedCities = []
connectedEastCities1 = findConnections(origin, visitedCities, testMap2)

origin = "Concord"
visitedCities = []
connectedEastCities2 = findConnections(origin, visitedCities, testMap2)

origin = "Newark"
visitedCities = []
connectedEastCities3 = findConnections(origin, visitedCities, testMap2)

print("Test 2: Two separate networks")
print("West Coast network should contain:")
print("Los Angeles, San Francisco, Sacramento, San Jose, Las Vegas, Salt Lake City, Boise")
print("West Coast network starting from Los Angeles: " + str(connectedWestCities1))
print("West Coast network starting from Sacramento: " + str(connectedWestCities2))
print("West Coast network starting from Boise: " + str(connectedWestCities3))
print("\n")
print("East Coast network should contain:")
print("New York City, Boston, Philadelphia, Newark, Concord, Providence")
print("East Coast network starting from New York City: " + str(connectedEastCities1))
print("East Coast network starting from Concord: " + str(connectedEastCities2))
print("East Coast network starting from Newark: " + str(connectedEastCities3))
print("\n")
