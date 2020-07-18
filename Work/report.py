#!/usr/bin/env python3
# report.py

import csv
import fileparse
import stock
import tableformat
from typing import List

# Exercise 3.12: Using your library module
# Modify the report.py program so that all of the input
# file procecssing is done using functions in fileparse module.

# Exercise 4.4: Using your class (from stock.py)

# Exercise 2.16: Using the zip() function
def read_portfolio(filename):
	'''
	Opens a given portfolio file and 
	reads it into a list of Stock instances.
	'''
	with open(filename, 'rt') as f:
		portdicts = fileparse.parse_csv(f,
			select = ['name',	'shares',	'price'],
			types =  [str,		int,		float],
			has_headers = True)

	portlist = [
		stock.Stock(d['name'], d['shares'], d['price'])
		for d in portdicts ]

	return portlist

def read_prices(filename):
	'''
	Reads a list of symbols paired with prices
	& returns a dictionary of stock prices.
	'''
	with open(filename, 'rt') as f:
		pricelist = fileparse.parse_csv(f,
			types = [str, float],
			has_headers = False)

		prices = dict(pricelist)

	return prices

def portfolio_value_and_change(portfolio, prices):
	'''
	Compute current value of portfolio along with 
	gain / loss
	'''
	total_current_value = 0.0
	total_delta = 0.0
	# get set of unique symbols in portfolio
	portfolio_syms = set(
		[ s.name for s in portfolio ])
	# start working on total current value / total delta
	for s in portfolio_syms:
		# get current price
		current_price = prices[s]
		# get # of s shares in portfolio
		s_shares = 0
		past_s_value = 0.0

		# calculate past value due to share: s
		# (Following Ex. 2.16, we build dictionaries from each
		# row in the portfolio by zip'ing with header fields, so,
		# we don't try to prejudge which fields need conversion to
		# numerical type. This activity is deferred instead to the time
		# when fields are needed for calculations.)
		for t in portfolio:
			if t.name == s:
				s_shares += t.shares
				past_s_value += t.cost()

		# calculate current value due to share: s
		current_s_value = s_shares * current_price

		total_current_value += current_s_value
		total_delta += current_s_value - past_s_value

	print(
		f"The total value of your portfolio is: \
		{total_current_value:0.2f}, \
		and your portfolio value has changed by: \
		{total_delta:0.2f}")

# Exercise 2.9 

def make_report(stock_list, price_list):
		'''
		Takes a list of stocks & a dictionary of prices as input;
		returns a list of tuples containing the rows for a table
		(without header or row / column delimiters)
		'''

		tuples = [
			# stock symbol
			(s.name,
			# number of shares
			s.shares,
			# current share price
			price_list[s.name],
			# change in share price
			price_list[s.name] - s.price) 
			for s in stock_list]

		return tuples

# Exercise 2.11  

# Exercise 4.5: An Extensibility Problem
# Modify the print_report() function so that it accepts
# a TableFormatter object as input, and invokes methods on it
# to produce the output.

def print_report(report, formatter):
	'''
	Print out the (name, shares, price, change) tuples 
	making up 'report', in the format specified by 'formatter'
	'''
	# headers = ('Name', 'Shares', 'Price', 'Change')
	# header_words = ['%10s' % r for r in headers]
	# header = ' '.join(header_words)
	# print(header)
	formatter.headings(['Name', 'Shares', 'Price', 'Change'])

	# separator_words = ['-' * 10 for _ in headers]
	# separator = ' '.join(separator_words)
	# print(separator)

	# Exercise 2.12 Formatting Challenge
	# for r in report:
	# 	print(f'{r[0]:>10s} {r[1]:>10d} ' +
	# 		# nested f-strings! get the 
	# 		# price part of r, r[2], as 
	# 		# a float with 2 decimal places,
	# 		# then place '$' on left &
	# 		# right justify the resulting string
	# 		# inside a field of 10 chars
	# 			f'{ f"${r[2]:0.2f}" :>10s} ' + 
	# 			   f'{r[3]:>10.2f}')
	for name, shares, price, change in report:
		rowdata = [ name, str(shares), f"${price:0.2f}", f'{change:0.2f}' ]
		formatter.row(rowdata)

# Since you added an argument to print_report(), you're going to need to
# modify the portfolio_report() function as well. Change it so that it 
# creates a TableFormatter like this:

def portfolio_report(portfolio_fname, prices_fname, fmt='txt'):
	'''
	Make a stock report, given portfolio and price data files.
	'''
	# Read data files
	portfolio = read_portfolio(portfolio_fname)
	prices = read_prices(prices_fname)

	# Create the report data
	report = make_report(portfolio, prices)

	# Print it out
	formatter = tableformat.create_formatter(fmt)
	print_report(report, formatter)

# Exercise 3.15: main() functions
# Exercise 4.8: Putting it all together
def main(args: List[str]):
	'''
	Accepts a list of command line options.
	Produces the portfolio_report output due to them.
	'''
	py_fname 		= args[0]
	portfolio_arg 	= args[1]
	prices_arg 		= args[2]
	# The 3rd argument, specifying the output format, is optional
	fmt_arg 		= args[3] if len(args) == 4 else 'txt'

	if py_fname == 'report.py':
		portfolio_report(portfolio_arg, prices_arg, fmt_arg)

if __name__ == '__main__':
	import sys
	main(sys.argv)
