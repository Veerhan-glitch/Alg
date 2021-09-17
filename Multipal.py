def Multipal_of(Num, Multipal_of):
	if (Num % Multipal_of) == 0:
		print(f"{Num} is a Multipal of {Multipal_of}.")
		return 1
	else:
		print(f"{Num} is not a Multipal of {Multipal_of}.")
		return 0
