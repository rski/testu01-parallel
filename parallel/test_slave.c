#include <TestU01.h>
#include <ulcg.h>
#include <unif01.h>
#include <bbattery.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void checkArguments(int argc, char *argv[]);
//void startSingleTest(int testNumber);

int main(int argc, char **argv){

  //find out which test from which suite to run
  int testNumber, testSuite;
  checkArguments(argc, argv);
  testNumber = atoi(argv[1]);
  testSuite = atoi(argv[2]);

  //start up a generator and get a test running on it
  unif01_Gen *gen;
  gen = ulcg_CreateLCG (2147483647, 16807, 0, 12345);
  //start the test & suite that was passed 
  startSingleTest(gen, testNumber, testSuite);
  ulcg_DeleteGen (gen);
  return 0;
}

void checkArguments(
    int argc, 
    char * argv[]
    ){

  if (argc != 3){
    fprintf(stderr, "Number of test to run & test suite were not passed, process exiting");
    exit(EXIT_FAILURE);
  }
}
