# Prints mean of the numbers given as arguments.
import sys

# Error checking for case of zero arguments
if len(sys.argv)==1:
	print 'Error: No arguments given.'
	sys.exit()

sum = 0
n = 0

#Takes sum of all inputted numbers and finds length
for line in open(sys.argv[1]):
	sum+= float(line)
	n+=1

#Calculates and prints the average
print sum / n