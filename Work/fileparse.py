import csv
from typing import List, Dict

# Exercise 3.3: Reading CSV Files
# Exercise 3.4: Building a Column Selector
# Exercise 3.5: Performing Type Conversion
# Exercise 3.6: Working without Headers
# Exercise 3.7: Picking a different column delimiter

# Does 'typing' have a duck type 
# for functions that I can use?
def parse_csv(filename: str, select :List[str] = None
						   , types = None
						   , has_headers = False
						   , delimiter=',') -> List[Dict[str, str]]:
	'''
	Parse a CSV file into a list of records
	'''
	with open(filename) as f:
		rows = csv.reader(f, delimiter=delimiter)

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
		for row in rows:
				if not row:		# skip rows with no data
					continue
				# If has_headers = True, then every record is a dict.
				if has_headers:
					# apply type casting & other functions, if provided.
					if types:
						record = dict(
							[(col, fn(val)) for col, fn, val in zip(
									[headers[j] for j in indices],
									types,
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

	return records