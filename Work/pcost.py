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
		for row in rows:
			try:
				row_shares 		= int(row[1])
				row_share_price = float(row[2])
			except ValueError:
				print("Couldn't parse number(s) from: ", row)
			row_value 		= row_shares * row_share_price
			total_value		= total_value + row_value

	# return total portfolio value
	return total_value

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
	
cost = portfolio_cost(filename)
print('Total cost: ', cost)


