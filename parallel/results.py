from test_definitions import SUITE_SIZE
import re
import logging

logging.basicConfig(filename='/tmp/testu01_results.log', filemode='w', level=logging.DEBUG)

def handleResults(results, testSuite, totalTime):
    results = binToString(results)
    header, results = stripHeaders(results)
    summaries, results = stripSummaries(results)
    logSummaries(summaries)
    printHeader(header)
    printResults(results)
    failedTests = getStatistics(summaries)
    printSummary(testSuite, failedTests, totalTime)


def logSummaries(summaries):
    for summary in summaries:
        for line in summary:
            logging.debug(line)


def getStatistics(summaries):
    allFailedTests = []
    for summary in summaries:
        failedTests = getFailedTests(summary)
        if failedTests is not None:
            allFailedTests = allFailedTests + failedTests
    return allFailedTests


def printSummary(testSuite, failedTests, totalTime):
    print("\n" * 3)
    print("========= Summary results of {0} =========".format(testSuite))
    print("Total time: {0}s".format(totalTime))
    if failedTests is not None:
        print("The following tests gave p-values outside [0.001, 0.9990]:")
        print("(eps  means a value < 1.0e-300):")
        print("(eps1 means a value < 1.0e-15):")
        #ugly but matches the eps values under it
        print("\tTest\t\t\t      p-value")
        print(" ----------------------------------------------")
        for test in failedTests:
            print(test)
        print(" ----------------------------------------------")


def createResultsArray(testSuite):
    results = [None] * SUITE_SIZE[testSuite]
    return results


def getFailedTests(summary):
    testFailureRe = re.compile('\s*\d+\s+\w+..+', re.IGNORECASE)
    failedTests = []
    for line in summary:
        match = testFailureRe.match(line)
        if match is not None:
            failedTests.append(match.group())
    if failedTests:
        return failedTests
    else:
        return None


def printResults(results):
    for result in results:
        for line in result:
            print(line)


def printHeader(header):
    for line in header:
        print(line)


def binToString(results):
    stringResults = []
    for result in results:
        stringResults.append(result.decode('utf-8'))
    return stringResults


def stripHeaders(results):
    newResults = []
    headersize = 12
    for result in results:
        tempResult = result.split("\n")
        newResults.append(tempResult[headersize-1:])
    header = tempResult[0:headersize-1]

    return header, newResults


def stripSummaries(results):
    newResults = []
    summaries = []
    for result in results:
        startOfSummary = getStartOfSummary(result)
        newResults.append(result[0:startOfSummary])
        summary = result[startOfSummary:len(result)]
        summaries.append(summary)
    return summaries, newResults


def getStartOfSummary(result):
    startOfSummary = [i for i,x in enumerate(result) if x == "Generator state:"]
    #print(startOfSummary)
    startOfSummary = startOfSummary[-1]+2
    return startOfSummary
