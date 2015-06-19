from subprocess import Popen, PIPE
import multiprocessing as mp
from multiprocessing import Queue
from time import sleep
from test_definitions import TEST_SLAVE_EXECUTABLE, TEST_SUITES, TEST_ORDER_DIR,SUITE_SIZE
from results import createResultsArray
from order import *



def forkTest(test, results):
    testNumber = int(test[1])
    print(test)
    #sleep (10)
    #stdout=subprocess.PIPE, stderr=subprocess.PIPE
    #get the output with stdout, stderr = testProcess.communicate()
    #otherwise a deadlock might occurr
    return Popen(test, stdout = PIPE )#results[testNumber-1])


def pollTests(processes):

    for process in processes:
        if process.poll():
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
#this function is horribly broken
def forkNewTests(processes, testGen, results):
    while(True):
        nextTest = next(testGen)
        #no tests left to run
        if not nextTest:
            break
        for process in processes:
            #is this precedence correct?
            #process.poll is not correct either
            if not process.poll() and nextTest:
                process = forkTest(nextTest, results)
                nextTest = next(testGen)
        sleep(1)


def startTests(testGen, processes, results):
    testProcesses = []
    for process in processes:
        test = next(testGen)
        process = forkTest(test, results)
        testProcesses.append(process)
        print(process)
    processes = testProcesses
    print(processes)
    return processes


if __name__=='__main__':
    testSuite = "smallCrush"
    numberOfCores = mp.cpu_count()
    #wholeSuiteInParallel actually might not be needed
    processes, wholeSuiteInParallel = createProcessArray()
    results = createResultsArray(testSuite)
    testGen = testGenerator(testSuite)

    processes = startTests(testGen, processes, results)
    print(processes)

    if not wholeSuiteInParallel:
        forkNewTests(processes, testGen, results)

    waitForTests(processes)
