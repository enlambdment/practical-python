# Exericse 7.8: Simplifying Function Calls

String = 	lambda val: typedproperty(val, str)
Integer = 	lambda val: typedproperty(val, int)
Float = 	lambda val:	typedproperty(val, float) 

# Exercise 7.7: Using Closures to Avoid Repetition

def typedproperty(name, expected_type):
	private_name = '_' + name 
	@property 
	def prop(self):
		return getattr(self, private_name)

	@prop.setter
	def prop(self, value):
		if not isinstance(value, expected_type):
			raise TypeError(f'Expected {expected_type}')
		setattr(self, private_name, value)

	return prop 