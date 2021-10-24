def Factor(Num, Factor_of):
    if (Factor_of % Num) == 0:
        return 'is a'  # Factor
    else:
        return 'is not a'  # Not a factor


def main():
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

        status = Factor(Num, Factor_of)
        print(f"{Num} {status} factor of {Factor_of}.")

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
