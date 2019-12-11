#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program turns integer into line of numbers


def seperateNumbers(number):
    numbers = []
    # Insert the digits into the "Number" list
    for digits_as_string in number:
        digits_as_int = int(digits_as_string)
        # Returnign converted digits to the list to be seperated
        numbers.append(digits_as_int)
    return numbers


def main():
    number_as_string = input("Enter your number: ")
    try:
        list_of_numbers = seperateNumbers(number_as_string)
        print(list_of_numbers)
    except ValueError:
        print("Invalid Input")


if __name__ == "__main__":
    main()
