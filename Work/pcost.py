# pcost.py
#
# Exercise 1.27

# >>> import os
# >>> os.getcwd()
# will give '/Users/jaimepiedra/Desktop/practical-python/Work'

filename = 'Data/portfolio.csv'

with open(filename, 'rt') as f:
	# skip header row
	headers = next(f).split(',')
	# now, start building up total portfolio value
	total_value = 0
	for line in f:
		row = line.split(',')
		row_shares 		= int(row[1])
		row_share_price = float(row[2])
		row_value 		= row_shares * row_share_price
		total_value		= total_value + row_value
	# report total value
	print(f'Total cost {total_value:0.2f}')



