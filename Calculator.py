def main():
    while True:
        print("Calculator")
        print('''For:
            Division press /
            Exponent press **
            Integral Division press //
            Multiplication press *
            Modulus (Remainder) press %
            Subtraction press -
            Addition press +''')

        operation = input("Your response: ")
        while operation not in ['/', '**', '//', '*', '%', '-', '+']:
            print("Invalid input please try again!")
            operation = input("Your response: ")

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
            print(f"Difference of {Num_1} and {Num_2} is {Num_1-Num_2}.")

        # Division
        elif operation == '/':
            print(f"Division of {Num_1} and {Num_2} is {Num_1/Num_2}.")

        # Exponential
        elif operation == '**':
            print(f"{Num_1} to the power {Num_2} is {Num_1**Num_2}.")

        # Floor division
        elif operation == '//':
            print(f"Floor division of {Num_1} and {Num_2} is {Num_1//Num_2}.")

        # Modulus
        elif operation == '%':
            print(
                f"Modulus (Remainder) of {Num_1} and {Num_2} is {Num_1%Num_2}.")

        # Multiplication
        elif operation == '*':
            print(f"Multiplication of {Num_1} and {Num_2} is {Num_1*Num_2}.")

        # Summation
        elif operation == "+":
            print(f"Sum of {Num_1} and {Num_2} is {Num_1+Num_2}.")

        # Program looping
        Again = None
        while Again not in ['y', 'n']:
            Again = input(
                "Do you want to run this feature again (y/n)? ").lower()
        if Again != 'y':
            break


if __name__ == '__main__':
    main()
