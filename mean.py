# Prints mean of the numbers given as arguments.
import sys

# Error checking for case of zero arguments
if len(sys.argv)==1:
	print 'Error: No arguments given.'
	sys.exit()

sum = 0

#Takes sum of all inputted numbers
for num in sys.argv[1:]:
	sum+= float(num)

#Calculates and prints the average
print sum / (len(sys.argv)-1