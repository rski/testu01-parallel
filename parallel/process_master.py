import subprocess
import multiprocessing as mp

TEST_SLAVE_EXECUTABLE = "test_slave.out"
TEST_SUITES = {"smallCrush":"0",
                "Crush":"1",
                "bigCrush":"2",
                "debug":"3"}
TEST_SUITE_TIMES_DIR = "test_suite_times"


def getAvailableTest(testSuite):
    testNumber = 1
    testNumber = str(testNumber)
    return ["./" + TEST_SLAVE_EXECUTABLE, testNumber, TEST_SUITES[testSuite]]

def startNewTest(testSuite):
    test = getAvailableTest(testSuite)
    print(test)
    subprocess.call(test)
    #exec(test)

if __name__=='__main__':
    numberOfCores = mp.cpu_count()
    #for core in range(0, numberOfCores-1):
    #    startNewTest(core)
    #pool = mp.Pool(processes=4)
    #results = [pool.apply(startNewTest, args=(x,)) for x in range(0,3)]
    #processes =  [mp.Process(target=startNewTest, args=(x, )) for x in range(0,3)]
    processes =  [mp.Process(target=startNewTest, args=('smallCrush', ))]
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("###################\n###################\nAfter the join")

    #print(results)
