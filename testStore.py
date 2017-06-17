# testStore.py
#
# A program to test storeConnections()
#
# Ian Marx, June 2017

from findConnections import findConnections
from storeConnections import storeConnections

print("\nstoreConnections() testing")

# Test 1: Generate a list of one city network
testMap1 = {}
testMap1["New York City"] = ["Boston", "Detroit"]
testMap1["Los Angeles"] = ["San Francisco", "Detroit"]
testMap1["Boston"] = ["New York City"]
testMap1["Detroit"] = ["New York City", "Los Angeles"]
testMap1["San Francisco"] = ["Los Angeles"]

connections = storeConnections(testMap1)
print("\nTest 1: Should contain one city network")
print(connections)

# Test 2: Generate a list containing two city networks
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

connections = storeConnections(testMap2)
print("\nTest 2: Should contain two city networks (west/east) in any order")
print(connections)

# Test 3: Add a third network to the map from test 2
testMap2["Detroit"] = ["Milwaukee", "Indianapolis", "Columbus"]
testMap2["Milwaukee"] = ["Chicago", "Detroit"]
testMap2["Chicago"] = ["Milwaukee", "Indianapolis"]
testMap2["Indianapolis"] = ["Chicago", "Detroit", "St. Louis"]
testMap2["St. Louis"] = ["Indianapolis"]
testMap2["Columbus"] = ["Detroit", "Pittsburgh", "Louisville"]
testMap2["Louisville"] = ["Columbus"]
testMap2["Pittsburgh"] = ["Columbus"]

connections = storeConnections(testMap2)
print("\nTest 3: Should contain three city networks (west/midwest/east) in any order")
print(connections)
print("\n")
