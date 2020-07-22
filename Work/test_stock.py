# Exercise 8.1: Writing Unit Tests

import unittest
import stock

# Writing a set of unit tests for the Stock class
class TestStock(unittest.TestCase): 	# <- all test classes must inherit unittest.TestCase 
	def test_create(self): 				# <- all unit tests must start test_[...]
		s = stock.Stock('GOOG', 100, 490.1)
		self.assertEqual(s.name, 'GOOG')
		self.assertEqual(s.shares, 100)
		self.assertEqual(s.price, 490.1)

	def test_cost(self):
		s = stock.Stock('GOOG', 100, 490.1)
		self.assertEqual(s.cost, 49010.0)

	def test_sell(self):
		s = stock.Stock('GOOG', 100, 490.1)
		s.sell(12)
		self.assertEqual(s.shares, 100-12)

	def test_set_shares(self):
		s = stock.Stock('GOOG', 100, 490.1)
		with self.assertRaises(TypeError):
			s.shares = '100'

if __name__ == '__main__':
	unittest.main()