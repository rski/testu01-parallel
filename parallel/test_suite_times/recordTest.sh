
TEST=$1

echo "$TEST" > ${TEST}_output.txt 
date >> ${TEST}_output.txt
./run_${TEST}.out &>> ${TEST}_output.txt
echo ${TEST} >> ${TEST}_output.txt
date >> ${TEST}_output.txt


