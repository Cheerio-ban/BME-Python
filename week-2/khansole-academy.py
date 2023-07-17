#!/usr/bin/env python3
"""
Author: Precious Jacob
Description: This module contains solution to the 
assigment khansole-academy.py
"""

import random

# Use constants where appropriate
MILESTONE = 3
BASE = 0    

def main():
    """
    Calculates and returns the weight of a human on the moon.
    """
    print("Khansole Academy")
    counter = 0

    while counter < MILESTONE:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        answer = num1 + num2

        print("What is {} + {}?".format(num1, num2))
        user_input = int(input("Your answer: "))

        if user_input != answer:
            counter = 0
            print("Incorrect. The expected answer is {}".format(answer))
        elif user_input == answer:
            counter += 1
            print("Correct! You've gotten {} correct in a row.".format(counter))
        
    print("Congratulations! You mastered addition.")




if __name__ == '__main__':
    main()