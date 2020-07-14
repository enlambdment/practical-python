import csv
import sys 

def portfolio_cost(filename):
	'''
	Takes a filename as input, reads the portfolio data
	in that file, and returns the total cost of the portfolio
	as a float.
	'''
	with open(filename, 'rt') as f:
		# parse rows
		rows = csv.reader(f)
		# skip headers
		headers = next(rows)
		# now, start building up total portfolio value
		total_value = 0

		# Exercise 2.15: A practical enumerate() example
		for rowno, row in enumerate(rows, start=1):
			# Exercise 2.16: Using the zip() function
			# (make a dictionary out of 'headers' & current 'row')
			record = dict(zip(headers, row))
			try:
				nshares 		= int(record['shares'])
				price 			= float(record['price'])
				# (You want to include the attempted addition
				# to the running total portfolio value inside
				# this try-part of try-except block. That way,
				# if int() or float() conversions fail then
				# the entire row is set aside & no attempted
				# change to total_value)
				total_value += nshares * price
			except ValueError:
				print(f'Row {rowno}: Couldn\'t convert: {row}')

	# return total portfolio value
	return total_value

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
	
cost = portfolio_cost(filename)
print('Total cost: ', cost)


