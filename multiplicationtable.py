for row in range(1, 12):
	for column in range(1, 12):
		print(str(column * row).rjust(3) + " ", end="")
	print("\n", end="")

