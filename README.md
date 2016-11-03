# Adder-LF-2D

## How To Generate BC File
1. run `$ python BC-CNF/testwriteadder32.py` to generate `32Adder.bc`
2. run `$ python BC-CNF/testwriteKSA32.py` to generate 'KSA32.bc'
3. generate cnf file using bc2cnf tools, one of them available [here](http://users.ics.aalto.fi/tjunttil/circuits/)
4. identify the 2 output ids you want to compare, add the line `d1 id2 0 -id1 -id2 0` at the bottom of the generated cnf file
5. run in a SAT Solver and it should give UNSAT as the answer

Our [SATSolver](https://github.com/amish995/Term4-2D)
