# mortgage.py
#
# Exercise 1.7

principal 	= 500000.0
rate 		= 0.05
payment 	= 2684.11
total_paid	= 0.0

# # Exercise 1.8
# payment_num = 0

# Exercise 1.9
get_start_month = input('Please provide extra payment start month: ')
extra_payment_start_month = int(get_start_month)

get_end_month = input('Please provide extra payment end month: ')
extra_payment_end_month = int(get_end_month)

get_extra_payment = input('Please provide extra payment amount: ')
extra_payment = float(get_extra_payment)

current_month = 1

while round(principal, ndigits=2) > 0.00:
	# Exercise 1.11
	# For any given month, you should never pay more
	# than the remaining principal; so, always pay down
	# the lesser of principal, payment (+ extra_payment)
	if (current_month >= extra_payment_start_month and 
		current_month <= extra_payment_end_month):
		paid_down = round(
			min(principal, payment + extra_payment), ndigits=2)
	else:
		paid_down = round(
			min(principal, payment), ndigits=2)

	principal = round(
		(principal * (1+rate/12)) - paid_down, ndigits=2)

	total_paid = total_paid + paid_down

	# Exercise 1.10
	# print current status
	print(f'Month {current_month} of payment:\t ${total_paid:0.2f} paid in total,\t ${principal:0.2f} principal remaining')

	current_month = current_month + 1

print('Total paid', total_paid, '\n',
	  'over', current_month - 1, 'months')