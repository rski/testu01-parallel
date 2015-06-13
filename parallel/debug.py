__all__ = ["dummyTest"]

from random import randint
from time import time,sleep


#dummy test which sleeps for a random time
def dummyTest(testNumber):
    testRunTime = randint(1,10)
    testStartTime = int(time())
    print("Starting dummy test " + str(testNumber) + " at " + str(testStartTime) + " for " + str(testRunTime) +"s")
    sleep(testRunTime)
    testEndTime = int(time())
    Dt = testEndTime - testStartTime - testRunTime
    print("Finished dummy test " + str(testNumber) + " at " + str(testEndTime) + ". Dt = " + str(Dt) +"s")


if __name__ == "__main__":
    dummyTest(1)
