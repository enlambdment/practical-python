# bounce.py
#
# Exercise 1.5

height_0 = 100 	# starting height before 1st bounce, meters
factor = 3/5 	# upon j'th bounce, ball returns to height of
				# (factor ** j) * height_0

j = 0
height = height_0
while j < 10:
	# perform the next bounce
	j = j + 1
	# calculate the height reached upon next bounce
	height = height * factor
	# print row of table for next bounce
	print(j, round(height, ndigits=4))


