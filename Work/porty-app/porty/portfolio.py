# Exercise 7.11: Class Methods in Practice 
# IDEA: If a Portfolio instance is supposed
# to contain a list of Stock instances, then
# maybe you should change the class to be 
# a bit more explicit about the fact. (a)
# And if you want to read a portfolio from a 
# CSV file, then maybe you should make a 
# class method for it. (b)

from . import stock
from . import fileparse

class Portfolio:
	def __init__(self):
		self.holdings = []

	def append(self, holding):
		if not isinstance(holding, stock.Stock): # (a)
			raise TypeError('Expected a Stock instance')
		self.holdings.append(holding)

	@classmethod
	def from_csv(cls, lines, **opts):
		self = cls()
		portdicts = fileparse.parse_csv(lines,
										select=['name','shares','price'],
										types=[str,int,float],
										**opts)

		# dict unpacking, via '**kwargs' syntax
		for d in portdicts:
			self.append(stock.Stock(**d))

		return self

	# Exercise 6.2: Supporting iteration
	def __iter__(self):
		return self.holdings.__iter__()

	# Exercise 6.3: Making a more proper container
	def __len__(self):
		return len(self.holdings)

	def __getitem__(self, index):
		return self.holdings[index]

	def __contains__(self, name):
		'''
		Indicates whether 'name' is the name of the stock for any
		holding present in the portfolio.
		'''
		# Exercise 6.14: Generator Expressions in Function Arguments
		return any(s.name == name for s in self.holdings)

	@property
	def total_cost(self):
		return sum(s.cost for s in self.holdings)

	def tabulate_shares(self):
		from collections import Counter
		total_shares = Counter()
		for s in self.holdings:
			total_shares[s.name] += s.shares 
		return total_shares