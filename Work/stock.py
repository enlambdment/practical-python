class Stock:
	'''
	A class where an instance represents a single holding of stock.
	'''
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

	def __repr__(self):
		return (f'Stock({self.name}, {self.shares}, {self.price})')

	def cost(self):
		'''
		Return cost of the stock holding.
		'''
		return self.shares * self.price

	def sell(self, n_shares):
		'''
		Update the holding after n_shares shares are sold.
		'''
		self.shares -= n_shares

# 4.2 Inheritance - example
# "class MyStock extends Stock"
class MyStock(Stock):
	# __init__ and inheritance:
	# If '__init__' is redefined for a subclass, 
	# it is essential to initialize the parent:
	def __init__(self, name, shares, price, factor):
		# check the call to 'super' and '__init__'
		super().__init__(name, shares, price)
		self.factor = factor

	# defining a new method
	def panic(self):
		self.sell(self.shares)

	# redefining an existing method
	def cost(self):
		# return 1.25 * self.shares * self.price
		# (Leveraging the superclass'es original
		# implementation for the relevant method)
		actual_cost = super().cost()
		return 1.25 * actual_cost


