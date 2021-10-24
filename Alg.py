# importing self made modules
import Calculator as C
import Factor as F
import LCM_HCF as L_H
import Multipal as M
import Odd_Even as O_E
import Sine_Checker as S_C


while True:
    while True:
        print(
            '''Welcome to Alg a tool with multipal algebraic centered features!
		It can currently:
			1) Act as a Calculator
			2) Check if a number is a factor of another
			3) Find LCM or HCF of two numbers
			4) Check if a number is a multipal of another
			5) Check if a number is odd or even
			6) Check the sine of a number (+ve/0/-ve)
			ENTER exit/quit TO QUIT''')

        feature = input(
            "So, which feature do you wanna use (enter the number)? ").lower()
        if feature in ['1', '2', '3', '4', '5', '6', 'exit', 'quit']:
            break
        print("Invalid input please try again!")

    # Calculator
    if feature == '1':
        C.main()

    # Factor
    elif feature == '2':
        F.main()

    # LCM/HCF
    elif feature == '3':
        L_H.main()

    # Multipal
    elif feature == '4':
        M.main()

    # Odd/Even
    elif feature == '5':
        O_E.main()

    # Sine_Checker
    elif feature == '6':
        S_C.main()

    else:
        exit()

    # Program looping
    while True:
        try:
            Again = input(
                "Do you want to run the program again (y/n)? ").lower()
            if Again in ['y', 'n']:
                break
            else:
                raise Exception("Invalid input")
                # ⬆ To raise an error so that except gets triggered
        except Exception:
            print("Invalid input please try again!")
    if Again == 'y':
        continue
    else:
        break
