def Dif(Num_1, Num_2):  # Difference
    return Num_1-Num_2

def Div(Num_1, Num_2):  # Division
    return Num_1/Num_2

def Expo(Num_1, Num_2):  # Exponential
    return Num_1**Num_2

def Floor_Div(Num_1, Num_2):  # Floor division
    return Num_1//Num_2

def Modulus(Num_1, Num_2):  # Modulus
    return Num_1 % Num_2

def Multi(Num_1, Num_2):  # Multiplication
    return Num_1*Num_2

def Sum(Num_1, Num_2):  # Summation
    return Num_1+Num_2


def main():
    while True:
        print("Calculator")

        while True:
            print('''For:
				Division press /
				Exponent press **
				Integral Division press //
				Multiplication press *
				Modulus (Remainder) press %
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
            Num_2 = input("Enter second the number: ")
            try:
                Num_2 = float(Num_2)
                break
            except:
                print("Invalid input please try again!")

        # Difference
        if operation == '-':
            Dif(Num_1, Num_2)
            print(f"Difference of {Num_1} and {Num_2} is {Num_1-Num_2}.")

        # Division
        elif operation == '/':
            Div(Num_1, Num_2)
            print(f"Division of {Num_1} and {Num_2} is {Num_1/Num_2}.")

        # Exponential
        elif operation == '**':
            Expo(Num_1, Num_2)
            print(f"{Num_1} to the power {Num_2} is {Num_1**Num_2}.")

        # Floor division
        elif operation == '//':
            Floor_Div(Num_1, Num_2)
            print(f"Floor division of {Num_1} and {Num_2} is {Num_1//Num_2}.")

        # Modulus
        elif operation == '%':
            Modulus(Num_1, Num_2)
            print(
                f"Modulus (Remainder) of {Num_1} and {Num_2} is {Num_1%Num_2}.")

        # Multiplication
        elif operation == '*':
            Multi(Num_1, Num_2)
            print(f"Multiplication of {Num_1} and {Num_2} is {Num_1*Num_2}.")

        # Summation
        else:
            Sum(Num_1, Num_2)
            print(f"Sum of {Num_1} and {Num_2} is {Num_1+Num_2}.")

        # Program looping
        while True:
            try:
                Again = input(
                    "Do you want to run this feature again (y/n)? ").lower()
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


if __name__ == '__main__':
    main()
