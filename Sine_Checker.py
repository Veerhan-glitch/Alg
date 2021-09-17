def Sine_Checker(Num):
	if Num > 0:
		print(f"{Num} is grater than zero.")
		return 1
	elif Num == 0:
		print(f"{Num} is zero.")
		return 0
	else:
		print(f"{Num} is smaller than zero.")
		return -1
