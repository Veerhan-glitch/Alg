def Factor_of(Num, Factor_of):
	if (Factor_of % Num) == 0:
		print(f"{Num} is a Factor of {Factor_of}.")
		return 1
	else:
		print(f"{Num} is not a Factor of {Factor_of}.")
		return 0
