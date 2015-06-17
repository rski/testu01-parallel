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

  unif01_Gen *gen;
  gen = ulcg_CreateLCG (2147483647, 16807, 0, 12345);
  bbattery_BigCrush (gen);
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
