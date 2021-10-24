# importing modules
import math


def HCF(Num_1, Num_2):  # HCF
    return math.gcd(Num_1, Num_2)

def LCM(Num_1, Num_2):  # LCM
    return math.lcm(Num_1, Num_2)


def main():
    while True:
        print("LCM/HCF Finder")

        while True:
            L_or_H = input("Enter L for LCM and H for HCF: ").upper()
            if L_or_H in ['H', 'L']:
                break

        # HCF
        if L_or_H == 'H':
            print("HCF Finder")

            while True:
                Num_1 = input("Enter first the number: ")
                try:
                    Num_1 = int(Num_1)
                    break
                except:
                    print("Invalid input please try again!")

            while True:
                Num_2 = input("Enter second the number: ")
                try:
                    Num_2 = int(Num_2)
                    break
                except:
                    print("Invalid input please try again!")

            HCF(Num_1, Num_2)
            print(f"HCF of {Num_1} and {Num_2} is {math.gcd(Num_1,Num_2)}.")

        # LCM
        else:
            print("LCM Finder")

            while True:
                Num_1 = input("Enter first the number: ")
                try:
                    Num_1 = int(Num_1)
                    break
                except:
                    print("Invalid input please try again!")

            while True:
                Num_2 = input("Enter second the number: ")
                try:
                    Num_2 = int(Num_2)
                    break
                except:
                    print("Invalid input please try again!")

            LCM(Num_1, Num_2)
            print(f"LCM of {Num_1} and {Num_2} is {math.lcm(Num_1,Num_2)}.")

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
