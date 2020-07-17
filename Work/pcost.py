#!/usr/bin/env python3
# pcost.py

from report import read_portfolio
from typing import List

def portfolio_cost(filename):
	'''
	Takes a filename as input, reads the portfolio data
	in that file, and returns the total cost of the portfolio
	as a float.
	'''
	# Exercise 3.14: Using more library imports
	# Modify the pcost.py file so that it uses the 
	# report.read_portfolio() function.
	# So, instead of iterating over the csv.reader(f),
	# use report.read_portfolio() to get the dictionary
	# of stock prices from 'Data/portfolio.csv'

	portfolio = read_portfolio(filename)

	total_value = 0
	for row in portfolio:
		total_value += row['shares'] * row['price']

	# return total portfolio value
	return total_value

# if len(sys.argv) == 2:
# 	filename = sys.argv[1]
# else:
# 	filename = 'Data/portfolio.csv'

# Exercise 3.15: main() fuctions

def main(args: List[str]):
	'''
	Accepts a list of command line options.
	Produces the pcost output due to them.
	'''
	py_fname	= args[0]
	portf_fname = args[1]

	if py_fname == 'pcost.py':
		cost = portfolio_cost(portf_fname)
		print('Total cost: ', cost)

if __name__ == '__main__':
	import sys
	main(sys.argv)


