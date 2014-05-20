def isprime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for x in range(3, int(n**0.5) + 1, 2):
		if n % x == 0:
			return False
	return True

for i in range(1, 100):
	print(str(i) + " " + str(isprime(i)))