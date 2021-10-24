def Multiple(Num, Multiple_of):
    if (Num % Multiple_of) == 0:
        print(f"{Num} is a Multiple of {Multiple_of}.")
        return 'is a'  # Multiple
    else:
        print(f"{Num} is not a Multiple of {Multiple_of}.")
        return 'is not a'  # Not a Multiple


def main():
    while True:
        print("Multiple Checker")

        while True:
            Num = input("Enter the number: ")
            try:
                Num = float(Num)
                break
            except:
                print("Invalid input please try again!")

        while True:
            Multiple_of = input(
                "Enter another the number (which could be the Multiple of previous one): ")
            try:
                Multiple_of = float(Multiple_of)
                break
            except:
                print("Invalid input please try again!")

        status = Multiple(Num, Multiple_of)
        print(f"{Num} {status} Multiple of {Multiple_of}.")

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
