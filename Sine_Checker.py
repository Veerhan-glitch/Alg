def Sine_Checker(Num):
    if Num > 0:  # +ve
        return 'positive'
    elif Num == 0:  # 0
        return 'zero'
    else:  # -ve
        return 'negative'


def main():
    while True:
        print("Sine Checker")

        while True:
            Num = input("Enter the number: ")
            try:
                Num = float(Num)
                break
            except:
                print("Invalid input please try again!")

        status = Sine_Checker(Num)
        print(f"{Num} is {status}.")

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
