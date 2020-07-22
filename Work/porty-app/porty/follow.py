import os
import time

f = open('Data/stocklog.csv')
f.seek(0, os.SEEK_END) 	# Move file pointer 0 bytes from end of file

# Exercise 6.6: Using a generator to produce data
# The data production code responsible for file reading
# & producing lines of data will be moved into a generator
# function, 'follow(filename)'

def follow(filename):
	with open(filename) as f:
		f.seek(0, os.SEEK_END)
		while True:
			line = f.readline()
			if line == '':
				time.sleep(0.1)
				continue
			yield line 			

if __name__ == '__main__':
	# Exercise 6.7: Watching your portfolio
	import report

	portfolio = report.read_portfolio('Data/portfolio.csv')

	for line in follow('Data/stocklog.csv'):
		fields = line.split(',')
		name = fields[0].strip('"')
		price = float(fields[1])
		change = float(fields[4])
		if name in portfolio:
			print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')