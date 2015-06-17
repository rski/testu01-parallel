def createResultsArray(testSuite):
    results = [None] * SUITE_SIZE[testSuite]
    return results

def extractTestResults(rawResults):
    #result = [ testName, testNumber, p_value, rawResult ]
    results = []
    for rawResult in rawResults:
        result = rawResult
        results.append(result)

    return results

def interpretResults(results):
    for result in results:
        resultList = result.split("\n")
        #do stuff with the lines

    return interpretedResults

def printResults(results):
    for result in results:
        print(result)
