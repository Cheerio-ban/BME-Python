#!/usr/bin/env python3


"""
Author: Precious Jacob
Description: This module contains solution to the 
assigment compute-interest.py
"""

# Use constants where appropriate
def main():
    """
    Compute Interest
    """
    initial_balance = float(input("Initial Balance: "))
    start_year = int(input("Start year: "))
    start_month = int(input("Start month: "))
    end_year = int(input("End year: "))
    end_month = int(input("End month: "))
    interest_rate = 5

    if (end_year < start_year) or (end_year == start_year and end_month <= start_month):
        print("Starting date needs to be before the ending date.")

    tmp_initial_balance = initial_balance
    tmp_start_year = start_year
    tmp_start_month = start_month
    tmp_end_year = end_year
    tmp_end_month = end_month

    while interest_rate != 0:
        interest_rate = float(input("Interest rate (0 to quit): "))
        if interest_rate == 0:
            break

        # while start_year != end_year and start_month != end_month:
        while start_year <= end_year:
            print("Year {}, month {} balance: {}".format(start_year, start_month, initial_balance))
            interest = initial_balance * interest_rate
            initial_balance += interest

            if start_year == end_year and start_month == end_month:
                break

            if start_month == 12:
                start_month = 1
                start_year += 1
            else:
                start_month += 1

        initial_balance = tmp_initial_balance
        start_year = tmp_start_year
        start_month = tmp_start_month
        end_year = tmp_end_year
        end_month = tmp_end_month

        






if __name__ == '__main__':
    main()