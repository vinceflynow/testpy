def rotate(l, pos=1):
	if len(l) == 0:
		return l
	pos = -pos % len(l) #flip rotation direction
	return l[pos:] + l[:pos]

numbers = [1, 2, 3, 4, 5, 6]
print(rotate(numbers))
