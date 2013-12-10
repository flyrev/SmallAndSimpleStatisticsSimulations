import random

TRIALS = 1000000
success = 0

SUM = 10

DICE = 2

for i in xrange(TRIALS):
	sumOfDice = 0
	for s in xrange(DICE):
		sumOfDice += random.randint(1,6)
		
	if sumOfDice == SUM:
		success+=1

print float(success)/TRIALS