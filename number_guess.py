#!usr/bin/python3

import random

random_number = random.randrange(1, 10)
input_count = 0

while input_count < 3:
    input_number = input("Enter number to guess: ")
    input_count += 1
    if  int(input_number) == random_number:
        print("You won!")
        break
else: #This else related to the while loop
    print("You failed.")

