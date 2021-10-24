def Odd_Even(Num):
    if (Num % 2) == 0:
        return 'even'  # Even number
    else:
        return 'odd'  # Odd number


def main():
    while True:
        print("Odd/Even Checker")

        while True:
            Num = input("Enter the number: ")
            try:
                Num = float(Num)
                break
            except:
                print("Invalid input please try again!")

        status = Odd_Even(Num)
        print(f"{Num} is an {status} number.")

        # Program looping
        while True:
            try:
                Again = input(
                    "Do you want to run this feature again(y/n)? ").lower()
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
