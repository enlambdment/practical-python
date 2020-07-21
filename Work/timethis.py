# Exercise 7.10: A decorator for timing
import time

def timethis(func):
	'''
	Decorator function to wrap input function with 
	extra logic that prints out how long it takes
	for the function to execute.
	'''
	def wrapper(*args, **kwargs):
		start = time.time()
		r = func(*args, **kwargs)
		end = time.time()
		print('%s.%s: %f' % (func.__module__, func.__name__, end-start))

	return wrapper