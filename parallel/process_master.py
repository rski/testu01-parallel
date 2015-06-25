from subprocess import Popen, PIPE
import multiprocessing as mp
from time import sleep
from test_definitions import TEST_SLAVE_EXECUTABLE, TEST_SUITES, TEST_ORDER_DIR,SUITE_SIZE
from results import createResultsArray, handleResults
from order import *
import logging

logging.basicConfig(filename='/tmp/testu01_parallel.log', filemode='w', level=logging.DEBUG)
logging.debug("\n\n\n")



def forkTest(test):
    testNumber = int(test[1])
    #sleep (10)
    #stdout=subprocess.PIPE, stderr=subprocess.PIPE
    #get the output with stdout, stderr = testProcess.communicate()
    #otherwise a deadlock might occurr
    logging.debug("forking test {0}".format(test))
    return Popen(test, stdout = PIPE )#results[testNumber-1])


def pollTests(processes):

    for process in processes:
        if process[0].poll():
            return True

    return False


def createProcessArray():
    if SUITE_SIZE[testSuite] <= numberOfCores:
        processes = [None] * SUITE_SIZE[testSuite]
        wholeSuiteInParallel = True
    else:
        processes =  [None] * numberOfCores
        wholeSuiteInParallel = False
    return (processes, wholeSuiteInParallel)


def waitForTests(processes):
    testsStillRunning = True
    while (testsStillRunning):
        testsStillRunning = pollTests(processes)
        sleep(1)


#forks new tests to replace all the finished processes
def forkNewTests(processes, testGen, results):
    numOfProcesses = len(processes)
    nextTest = next(testGen)
    testNumber = int(nextTest[1])

    while(True):
        #no tests left to run
        if not nextTest:
            break
        for i in range(0, numOfProcesses):
            #is this precedence correct?
            #process.poll is not correct either
            if (processes[i] is None or processes[i][0].poll() is not None) and nextTest:
                testNumber = int(nextTest[1])
                #get the results of the test to be replaced
                if processes[i] is not None:
                    results[processes[i][1]-1],_ = processes[i][0].communicate()
                processes[i] = (forkTest(nextTest), testNumber)
                nextTest = next(testGen)
        sleep(1)
    return results, processes


def getLastResults(processes, results):
    logging.debug("This is getlastResults")
    for process in processes:
        logging.debug("Putting results of process {0} in {1}".format(process[1],process[1]-1))
        results[process[1]-1],_ = process[0].communicate()
    return results


if __name__=='__main__':
    testSuite = "smallCrush"
    numberOfCores = mp.cpu_count()
    #wholeSuiteInParallel actually might not be needed
    processes, wholeSuiteInParallel = createProcessArray()
    results = createResultsArray(testSuite)
    testGen = testGenerator(testSuite)

    results, processes = forkNewTests(processes, testGen, results)

    waitForTests(processes)
    results = getLastResults(processes, results)
    handleResults(results)
