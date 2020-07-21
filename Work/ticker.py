# Exercise 6.10: Making more pipeline components

from follow import follow
from report import read_portfolio
import csv
import tableformat

def select_columns(rows, indices):
	for row in rows:
		yield [row[index] for index in indices]

def convert_types(rows, types):
	for row in rows:
		yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
	for row in rows:
		yield dict(zip(headers, row))

# Exercise 6.11: Filtering data
def filter_symbols(rows, names):
	for row in rows:
		if row['name'] in names:
			yield row

def parse_stock_data(lines):
	rows = csv.reader(lines)
	rows = select_columns(rows, [0, 1, 4])
	rows = convert_types(rows, [str, float, float])
	rows = make_dicts(rows, ['name', 'price', 'change'])
	return rows

# Exercise 6.12: Putting it all together
def ticker(portfile, logfile, fmt):
	# read the portfolio into a Portfolio instance
	portfolio = read_portfolio(portfile)
	# read rows from logfile, as they are produced
	rows = parse_stock_data(follow(logfile))
	# intermediate processing
	rows = filter_symbols(rows, portfolio)
	# 'rows' is now a list of dicts, filtered on 
	# whether 'stock' for the row is in 'portfolio'.
	# We need a formatter, for formatting the output:
	formatter = tableformat.create_formatter(fmt)
	# print the table. 
	tableformat.print_table(rows, ['name', 'price', 'change'], formatter)

# Exercise 6.15: Code simplification.
# Generator expressions are often a useful 
# replacement for small generator functions: 
# e.g. the following alternative ticker function
# Exercise 6.12: Putting it all together
def ticker_new(portfile, logfile, fmt):
	# read the portfolio into a Portfolio instance
	portfolio = read_portfolio(portfile)
	# read rows from logfile, as they are produced
	rows = parse_stock_data(follow(logfile))
	# intermediate processing
	rows = (row for row in rows if row['name'] in portfolio)
	# 'rows' is now a list of dicts, filtered on 
	# whether 'stock' for the row is in 'portfolio'.
	# We need a formatter, for formatting the output:
	formatter = tableformat.create_formatter(fmt)
	# print the table. 
	tableformat.print_table(rows, ['name', 'price', 'change'], formatter)

if __name__ == '__main__':
	portfolio = read_portfolio('Data/portfolio.csv')
	rows = parse_stock_data(follow('Data/stocklog.csv'))
	rows = filter_symbols(rows, portfolio)
	for row in rows:
		print(row)