#!/usr/bin/env python3

import sys

numbers = []
numbersSum = 0
numbersLow = None
numbersHigh = None

while True:
    try:
        line = input("Enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        numbersSum += number
        if numbersLow is None or numbersLow > number:
            numbersLow = number
        if numbersHigh is None or numbersHigh <number:
            numbersHigh = number
    except ValueError as err:
        print(err)

print("Numbers input: ",numbers)
if numbers:
    print("Count = ", len(numbers), "Sum = ", numbersSum,
          "Lowest = ",numbersLow, "Highest = ", numbersHigh,
          "Mean = ", numbersSum/len(numbers))
    
