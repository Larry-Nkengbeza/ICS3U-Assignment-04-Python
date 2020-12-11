# assignment/usr/bin/env python3
# This was created by Larry Nkengbeza
# This program was created on December 2020
# This program calculates the largest number

def main():
    # Input
    print("Enter in three numbers")
    number1_str = input("Enter in Number 1: ")
    number2_str = input("Enter in Number 2: ")
    number3_str = input("Enter in Number 3: ")

    # Process and Output
    try:
        number1 = int(number1_str)
        number2 = int(number2_str)
        number3 = int(number3_str)

        if number1 > number2 and number3:
            print("{0} is the largest number."
                  .format(number3_str))
        elif number2 > number1 and number3:
            print("{0} is the largest number."
                  .format(number2_str))
        elif number3 > number1 and number2:
            print("{0} is the largest number."
                  .format(number3_str))
        else:
            print("The numbers are all even.")
    except Exception:
        print("There was atleast one number which was not an integer.")
    finally:
        print("Thanks for inputting number")


if __name__ == "__main__":
    main()
