import Calculator as C
import Factor as F
import LCM_HCF as L_H
import Multipal as M
import Odd_Even as O_E
import Sine_Checker as S_C
while True:

	Num = None
	Num_1 = None
	Num_2 = None
	Factor_of = None
	L_or_H = None
	Multipal_of = None
	Again = None
	Again_fea = None
	feature = None
	operation = None
	invalid = None

	while True:
		print('''Welcome to Alg a tole with multipal algebraic centered features!
		It can currently:
			1) Act as a Calculator
			2) Check if a number is a factor of another
			3) Find LCM or HCF of two numbers
			4) Check if a number is a multipal of another
			5) Check if a number is odd or even
			6) Check the sine of a number (+ve/0/-ve)
			ENTER exit TO QUIT''')
		feature = input("So, which feature do you wanna use (enter the number)? ").lower()
		if feature in ['1', '2', '3', '4', '5', '6', 'exit']:
			break
		print("Invalid input please try again!")

	#* Calculator
	if feature == '1':
		while True:
			while True:
				print('''Calculator
				For:
					Division press /
					Exponent press **
					Integral Division press //
					Multiplication press *
					Remander press %
					Subtraction press -
					Addition press +''')
				operation = input("Your responce: ")
				if operation in ['/', '**', '//', '*', '%', '-', '+']:
					break
				print("Invalid input please try again!")
			while True:
				Num_1 = input("Enter first the number: ")
				try: 
					Num_1 = float(Num_1)
					break
				except:
					print("Invalid input please try again!")
			while True:
				Num_2=input("Enter second the number: ")
				try:
					Num_2 = float(Num_2)
					break
				except:
					print("Invalid input please try again!")
			if operation == '/':
				C.Div(Num_1, Num_2)
			elif operation == '**':
				C.Expo(Num_1, Num_2)
			elif operation == '//':
				C.Int_Div(Num_1, Num_2)
			elif operation == '*':
				C.Multi(Num_1, Num_2)
			elif operation == '%':
				C.Remain(Num_1, Num_2)
			elif operation == '-':
				C.Sub(Num_1, Num_2)
			else:
				C.Sum(Num_1, Num_2)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break
		
	#* Factor
	elif feature == '2':
		while True:
			print("Factor Checker")
			while True:
				Num = input("Enter the number: ")
				try:
					Num = float(Num)
					break
				except:
					print("Invalid input please try again!")
			while True:
				Factor_of = input(
					"Enter another the number (which could be the factor of previous one): ")
				try:
					Factor_of = float(Factor_of)
					break
				except:
					print("Invalid input please try again!")
			F.Factor_of(Num, Factor_of)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break

	#* LCM/HCF
	elif feature == '3':
		while True:
			print("LCM/HCF Finder")
			while True:
				L_or_H = input("Enter L for LCM and H for HCF: ").upper()
				if L_or_H in ['H', 'L']:
					break
			while True:
				Num_1 = input("Enter first the number: ")
				try:
					Num_1 = float(Num_1)
					break
				except:
					print("Invalid input please try again!")
			while True:
				Num_2 = input("Enter second the number: ")
				try:
					Num_2 = float(Num_2)
					break
				except:
					print("Invalid input please try again!")
			if L_or_H == 'H':
				print("HCF Finder")
				L_H.HCF(Num_1, Num_2)
			else:
				print("LCM Finder")
				L_H.LCM(Num_1, Num_2)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break

	#* Multipal
	elif feature == '4':
		while True:
			print("Multipal Checker")
			while True:
				Num = input("Enter the number: ")
				try:
					Num = float(Num)
					break
				except:
					print("Invalid input please try again!")
			while True:
				Multipal_of = input("Enter another the number (which could be the multipal of previous one): ")
				try:
					Multipal_of = float(Multipal_of)
					break
				except:
					print("Invalid input please try again!")
			M.Multipal_of(Num, Multipal_of)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break

	#* Odd/Even
	elif feature == '5':
		while True:
			print("Odd/Even Checker")
			while True:
				Num = input("Enter the number: ")
				try:
					Num = float(Num)
					break
				except:
					print("Invalid input please try again!")
			O_E.Odd_Even(Num)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break

	#* Sine_Checker
	elif feature == '6':
		while True:
			print("Sine Checker")
			while True:
				Num = input("Enter the number: ")
				try:
					Num = float(Num)
					break
				except:
					print("Invalid input please try again!")
			S_C.Sine_Checker(Num)
			while True:
				try:
					Again_fea = input("Do you want to run this feature again(y/n)? ").lower()
					if Again_fea == 'y' or Again_fea == 'n':
						break 
					else:
						again_fea = int('w')
				except:
					print("Invalid input please try again!")
			if Again_fea == 'y':
				continue
			else:
				break

	else:
		exit()

	while True:
		try:
			Again = input("Do you want to run the program again (y/n)? ").lower()
			if Again == 'y' or Again == 'n':
				break
			else:
				again = int('w')
		except:
			print("Invalid input please try again!")
	if Again == 'y':
		continue
	else:
		break
