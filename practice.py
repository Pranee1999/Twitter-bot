def myfunc(**kwargs):
	if "fruit" in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print("I did not find any fruit here")

myfunc(fruit="apple",veggie="lettuce")