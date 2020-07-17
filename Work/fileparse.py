import csv
from typing import List, Dict, Iterable

# Exercise 3.3: Reading CSV Files
# Exercise 3.4: Building a Column Selector
# Exercise 3.5: Performing Type Conversion
# Exercise 3.6: Working without Headers
# Exercise 3.7: Picking a different column delimiter

# Exercise 3.8: Raising exceptions
# Modify the code so that an exception gets raised
# if 'select' argument is provided with a value but
# has_headers = False

# Remark. 
# Whenever 'select' includes col. names that do not
# exist in 'headers', then they are simply skipped over
# when trying to select from 'headers' / 'row'.
# But since the 'select', 'types' inputs are supposed to be
# 'co-indexed', this can lead to unanticipated pairing of
# 'row' elements with 'types' functions, typecasting / formatting
# the data in unwanted ways.

# Does 'typing' have a duck type 
# for functions that I can use?

# Exercise 3.17: From filenames to file-like objects
# Modify parse_csv() so that, instead of taking a filename
# to read using the csv library, it directly accepts *any* 
# iterable of comma-separated values

def parse_csv(lines: Iterable[str], select: List[str] = None
						   		  , types = None
						   		  , has_headers = False
						   		  , delimiter = ','
						   		  , silence_errors = False) -> List[Dict[str, str]]:
	'''
	Parse an iterable of comma-separated values into a list of records
	'''

	# Raise exception if a subset of header columns
	# is specified by a 'select' value, but has_headers=False
	if isinstance(select, list) and not has_headers:
		raise RuntimeError("select argument requires column headers") 

	# Raise exception if 'select', 'types' values of
	# unequal length are provided
	if isinstance(select, list) and isinstance(types, list):
		if len(select) != len(types):
			raise RuntimeError("select, types arguments of unequal length")

	# 'rows' is an iterable based upon 'lines'.
	# Split up every line in 'lines', into items, using delimiter
	rows = csv.reader(lines, delimiter=delimiter)

	# read the file headers, if applicable
	if has_headers:
		headers = next(rows)

	# If a list representing a selection of columns from
	# the headers was provided, then take just the 
	# headers / row elements at the appropriate indices.
	# Otherwise, take all elements.
	# Not applicable if has_headers = False
	if has_headers:
		if select:
			indices = [headers.index(col) for col in select 
										  if col in headers]
		else:
			indices = range(len(headers))

	# build up result list.
	records = []
	for row_no, row in enumerate(rows, start=1):
			if not row:		# skip rows with no data
				continue

			# All case logic on 'has_headers', 'types', 'select'
			# below goes in a try-except block, in case of any
			# ValueErrors arising from the attempt to construct
			# and add the record.

			try:
				# If has_headers = True, then every record is a dict.
				if has_headers:
					# apply type casting & other functions, if provided.
					if types:
						record = dict(
							[(col, fn(val)) for col, fn, val in zip(
									[headers[j] for j in indices],
									# (see Remark, above)
									[types[select.index(headers[j])] 	
												for j in indices]
										if 		isinstance(select, list)
										else 	types,
									[row[j] 	for j in indices])])
					else:
						record = dict(zip(
							[headers[j] for j in indices], 
							[row[j] 	for j in indices]))
				# If has_headers = False, then every record is a tuple.
				else:
					# apply type casting & other functions, if provided.
					if types:
						record = tuple([fn(val) for fn, val in zip(types, row)])
					else:
						record = tuple(row)
				records.append(record)
			except ValueError as e:
				# Exercise 3.10: Silencing Errors
				if not silence_errors:
					print(f"Row {row_no}: Couldn't convert {row}")
					print(f"Row {row_no}: Reason - {e}")


	return records

# ln. 71
# With this change, 'select' / 'types' arguments will work properly
# even if not all col_names in 'select' exist in the file header e.g.

'''
>>> portfolio3 = parse_csv(
...     'Data/portfolio.csv',
...     select=['shares','change','volume','fullname','name'],
...     types =[int,     float,   int,     str,       str   ],
...     has_headers=True)
'''

# , so long as 'select' / 'type' entries are paired appropriately