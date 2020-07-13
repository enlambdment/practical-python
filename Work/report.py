import csv

def read_portfolio(filename):
	'''
	Opens a given portfolio file and 
	reads it into a list of tuples.
	'''
	portfolio = [] 

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			d = {}
			d['name'] = row[0]
			d['shares'] = int(row[1])
			d['price'] = float(row[2])
			portfolio.append(d)

	return portfolio

def read_prices(filename):
	'''
	Reads a list of symbols paired with prices
	& returns a dictionary of stock prices.
	'''
	prices = {}

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		for row in rows:
			# try:
			# 	prices[row[0]] = float(row[1])
			# except IndexError:
			# 	print("Couldn't parse:\t", row)

			# alternatively, guard against bad data
			# using an if-statement:
			if len(row) == 2:
				prices[row[0]] = float(row[1])

	return prices

# Exercise 2.7

# Take list of stocks from 'Data/portfolio.csv'
portfolio_fname = 'Data/portfolio.csv'
portfolio = read_portfolio(portfolio_fname)

# Take dictionary of prices from 'Data/prices.csv'
prices_fname = 'Data/prices.csv'
prices = read_prices(prices_fname)

# Compute current value of portfolio along with 
# gain / loss
total_current_value = 0.0
total_delta = 0.0
# get set of unique symbols in portfolio
portfolio_syms = set(
	[ d['name'] for d in portfolio ])
# start working on total current value / total delta
for s in portfolio_syms:
	# get current price
	current_price = prices[s]
	# get # of s shares in portfolio
	s_shares = 0
	past_s_value = 0.0

	# calculate past value due to share: s
	for d in portfolio:
		if d['name'] == s:
			s_shares += d['shares']
			past_s_value += d['shares'] * d['price']

	# calculate current value due to share: s
	current_s_value = s_shares * current_price

	total_current_value += current_s_value
	total_delta += current_s_value - past_s_value

print(
	f"The total value of your portfolio is: \
	{total_current_value:0.2f}, \
	and your portfolio value has changed by: \
	{total_delta:0.2f}")
