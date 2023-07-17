#!/usr/bin/env python3
"""
Author: Precious Jacob
Description: This module contains solution to the 
assigment moon-weight.py
"""

# Use constants where appropriate
MOON_CONSTANT = 16.5 / 100
BASE = 0    # Note: This is a personal convention.

def main():
    """
    Calculates and returns the weight of a human on the moon.
    """
    earth_weight = float(input("Enter your weight: "))
    if earth_weight < BASE:
        print("Sorry, you can't have a negative weight.")
    elif earth_weight == BASE:
        print("Human weights can't be zero.")
    else:
        moon_weight = MOON_CONSTANT * earth_weight
        print("Your weight on the moon is: {}".format(moon_weight))


if __name__ == '__main__':
    main()