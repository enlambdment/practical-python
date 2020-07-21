class TableFormatter:
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		raise NotImplementedError()

# Exercise 4.6: Using Inheritance to Produce Different Output

class TextTableFormatter(TableFormatter):
	'''
	Emit a table in plain-text format
	'''
	def headings(self, headers):
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(('-'*10 + ' ')*len(headers))

	def row(self, rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()

class CSVTableFormatter(TableFormatter):
	'''
	Output portfolio data in CSV format.
	'''
	def headings(self, headers):
		print(','.join(headers))

	def row(self, rowdata):
		print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
	'''
	Output portfolio data in HTML format.
	'''
	def headings(self, headers):
		print('<tr>' + 
			"".join(['<th>' + h + '</th>' for h in headers]) + 
			'</tr>')

	def row(self, rowdata):
		print('<tr>' + 
			"".join(['<td>' + x + '</td>' for x in rowdata]) +
			'</tr>')

# Exercise 4.11: Defining a custom exception
class FormatError(Exception):
	pass

def create_formatter(name):
	'''
	Allows a user to create a formatter, given an output-format
	name such as 'txt', 'csv', or 'html'.
	'''
	if name == 'txt':
		return TextTableFormatter()
	elif name == 'csv':
		return CSVTableFormatter()
	elif name == 'html':
		return HTMLTableFormatter()
	else:
		raise FormatError('Unknown table format %s' % name)

def print_table(objs, attrs, formatter):
	'''
	Prints a table showing user-specified attributes, 'attrs',
	of a list of arbitrary objects, 'objs', in format according
	to the TableFormatter instance 'formatter'
	'''
	# Emit table headings, according to 'attrs' specified
	formatter.headings(attrs)

	# Emit a row of table data, for each obj in 'objs'
	for obj in objs:
		# Not all objects are dictionaries in their underlying representation
		# (e.g. instances of a class with '__slots__' defined), but this is still
		# more appropriate than 'getattr(obj, attr)' - onus should be on code
		# leveraging tableformat to take care of casting objects into dicts, not on
		# 'print_table' to handle dict- vs. non-dict-based objects agnostically
		obj_row = [str(obj[attr]) for attr in attrs]
		formatter.row(obj_row)

