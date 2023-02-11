git-website: https://github.com/kingsleylow0327/island_counter
# island_counter
This program allow user to count groups of '1's in a map full of '0'.\
eg:\
0000\
0110\
0100\
1000

The output of the program with above eg input is 2 (Diagonal '1's is not grouped).\
The output format is in form of json.\
eg:\
{"status":"Ok","message":"2"} represents 2 groups of '1's as result\
{"status":"Error","message":"Map shape of is not x*y"} represents Error due to input shape\

There are 2 ways to run this program, following shows the steps to run main program and unit test for each ways

## sh Method:

Pre-requisite to run sh command:
- Install Docker

Steps:
1. Indicate an .txt file with only '0' and '1's
2. Run this command 'sh ./run.sh <.txt file in step 1>.txt'
3. Wait and see the result

Unit Test:
1. Run this command 'sh ./run_unittest.sh'
2. Wait and see the result


## Python Method:

Pre-requisite to run using python command:
- Install Python 3.x

Steps:
1. Create an .txt file with only '0' and '1's with name 'input.txt' at root dir of project
2. Run this command 'python3 main.py'
3. Wait and see the result

Unit Test:
1. Go to unit_test folder
2. Run this command 'python3 unit_test_island_count.py'
3. Wait and see the result
2. Run this command 'python3 unit_test_map_validator.py'
3. Wait and see the result