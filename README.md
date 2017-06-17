# Finding City Networks

This is a group of Python programs written to find networks in a data set of cities.
The function `storeConnections()` from `storeConnections.py` will take a map of cities to a list of their neighbors (within some predetermined radius), and generate an array containing all unique networks of cities in the data set.

## Usage
```
from storeConnections import storeConnections

neighborMap = {}
# populate the map with {String, [String]} pairs of cities to their neighbors
# ex: neighborMap["San Francisco"] = ["Palo Alto", "Sunnyvale", "Redwood Shores", "Oakland"]

networkList = storeConnections(neighborMap)
# now use the list of networks for your purposes

```

## Testing
Run `bash test.sh` to display the results of both test programs.

## Citations
The `compare()` method in `storeConnections.py` is used to check if two unordered arrays contain the same contents. It comes from [this StackOverflow discussion](https://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets-in-python).


-Ian Marx, June 2017
