def sumfile(numberfile):
	sum = 0
	with open(numberfile) as nf:
		for line in nf:
			sum += int(line.strip())
	return sum

numberfile='numbers.txt'
print("Sum of " + numberfile + " is " + str(sumfile(numberfile)))
