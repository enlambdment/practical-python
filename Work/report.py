import csv

# Exercise 2.16: Using the zip() function
def read_portfolio(filename):
	'''
	Opens a given portfolio file and 
	reads it into a list of dictionaries.
	'''
	portfolio = [] 

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		
		for row in rows:
			
			# don't hard-code the row indices containing the
			# values you need

			# d = {}
			# d['name'] = row[0]
			# d['shares'] = int(row[1])
			# d['price'] = float(row[2])

			record = dict(zip(headers, row))
			portfolio.append(record)

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

def portfolio_value_and_change(portfolio, prices):
	'''
	Compute current value of portfolio along with 
	gain / loss
	'''
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
		# (Following Ex. 2.16, we build dictionaries from each
		# row in the portfolio by zip'ing with header fields, so,
		# we don't try to prejudge which fields need conversion to
		# numerical type. This activity is deferred instead to the time
		# when fields are needed for calculations.)
		for d in portfolio:
			if d['name'] == s:
				s_shares += int(d['shares'])
				past_s_value += s_shares * float(d['price'])

		# calculate current value due to share: s
		current_s_value = s_shares * current_price

		total_current_value += current_s_value
		total_delta += current_s_value - past_s_value

	print(
		f"The total value of your portfolio is: \
		{total_current_value:0.2f}, \
		and your portfolio value has changed by: \
		{total_delta:0.2f}")

# portfolio_value_and_change(portfolio, prices)
# The total value of your portfolio is: 		28686.10, 		
# and your portfolio value has changed by: 		-32527.05

# Exercise 2.9 

def make_report(stock_list, price_list):
		'''
		Takes a list of stocks & a dictionary of prices as input;
		returns a list of tuples containing the rows for a table
		(without header or row / column delimiters)
		'''

		tuples = [
			# stock symbol
			(d['name'],
			# number of shares
			int(d['shares']),
			# current share price
			price_list[d['name']],
			# change in share price
			price_list[d['name']] - float(d['price'])) 
			for d in stock_list]

		return tuples

# Exercise 2.10

report = make_report(portfolio, prices)
# for r in report:
# 	print('%10s %10d %10.2f %10.2f' % r)

# Exercise 2.11  

def show_report(report):
	'''
	Print out the records making up the report table.
	'''
	headers = ('Name', 'Shares', 'Price', 'Change')
	header_words = ['%10s' % r for r in headers]
	header = ' '.join(header_words)
	print(header)

	separator_words = ['-' * 10 for _ in headers]
	separator = ' '.join(separator_words)
	print(separator)

	# Exercise 2.12 Formatting Challenge
	for r in report:
		print(f'{r[0]:>10s} {r[1]:>10d} ' +
			# nested f-strings! get the 
			# price part of r, r[2], as 
			# a float with 2 decimal places,
			# then place '$' on left &
			# right justify the resulting string
			# inside a field of 10 chars
				f'{ f"${r[2]:0.2f}" :>10s} ' + 
				   f'{r[3]:>10.2f}')

