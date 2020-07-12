# pcost.py
#
# Exercise 1.27
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. 
# Write a program called pcost.py that opens this file, reads all lines, and 
# calculates how much it cost to purchase all of the shares in the portfolio.
import sys

def portfolio_cost(filename):
    # open and read the file
    purchase_price = 0.0 
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            try:
                purchase_price = purchase_price + float(row[1]) * float(row[2])
            except ValueError:
                print("Check for missing values")
    return purchase_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: ${cost}')
