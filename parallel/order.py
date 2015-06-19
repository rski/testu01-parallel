__all__ = ["testGenerator"]

from test_definitions import TEST_ORDER_DIR, TEST_SUITES, TEST_SLAVE_EXECUTABLE
import os


def testOrderFromFile(testSuite):
    testOrder = []
    testOrderFileName = os.path.join(TEST_ORDER_DIR, "{0}_order.txt".format(testSuite))
    print(testOrderFileName)
    with open(testOrderFileName) as testOrderFile:
        for line in testOrderFile:
            testOrder.append(line)

    return testOrder

def testGenerator(testSuite):
    testOrder = testOrderFromFile(testSuite)
    for testNumber in testOrder:
        test = ["./" + TEST_SLAVE_EXECUTABLE, testNumber, TEST_SUITES[testSuite]]
        yield test

    while True:
        yield None


