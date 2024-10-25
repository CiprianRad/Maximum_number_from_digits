def get_valid_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            if n >= 0:
                return n
            else:
                return abs(n)
        except ValueError:
            print("Please enter a valid integer: ")


def max_number(n):
    list_from_number = list(str(n))  # We declare a list with string values, each entry is the digit of a given number
    list_from_number.sort(reverse=True)  # We sort the list alphanumerically in descending order
    list_from_number = ''.join(list_from_number)  # We join the elements in the list together. They form the number
    return list_from_number


def main():

    n = get_valid_input()
    print("The greatest number that can be made using the digits of your number is: ", max_number(n))


main()
