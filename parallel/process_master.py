from subprocess import Popen
import multiprocessing as mp
from multiprocessing import Queue
from time import sleep
from test_definitions import TEST_SLAVE_EXECUTABLE, TEST_SUITES, TEST_ORDER_DIR,SUITE_SIZE


def getNextTest(testSuite):
    testNumber = 1
    testNumber = testNumber + 1
    testNumber = str(testNumber)
    yield ["./" + TEST_SLAVE_EXECUTABLE, testNumber, TEST_SUITES[testSuite]]


def forkTest(test, results):
    testNumber = int(test[1])
    return Popen(test, stdout = results[testNumber-1])


def waitForTests(processes):
    for process in processes:
        if process.poll():
            process.wait()


def pollTests(processes):
    for process in processes:
        pass


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
        testsStillRunning = False
        for process in processes:
            if process.poll():
                testsStillRunning = True



#forks new tests to replace all the finished processes
def forkNewTests(processes,testSuite):
    while(True):
        nextTest = getNextTest(testSuite)
        #no tests left to run
        if not nextTest:
            break
        for process in processes:
            #is this precedence correct?
            #process.poll is not correct either
            if not process.poll() and nextTest:
                process = forkTests(nextTest)
                nextTest = getNextTest(testSuite)
            sleep(1)




if __name__=='__main__':
    testSuite = "smallCrush"
    numberOfCores = mp.cpu_count()
    #wholeSuiteInParallel actually might not be needed
    processes, wholeSuiteInParallel = createProcessArray()

    startTests(processes)

    if not wholeSuiteInParallel:
        forkNewTests(processes)

    waitForLastTests(processes)
