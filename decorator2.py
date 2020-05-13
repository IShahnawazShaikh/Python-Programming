# If inner functio retun value
def sum_number(func):
	def inner1(a,b):
		func(a,b)
		return a*b
	return inner1
	def inner2(a,b):
		func(a,b)
		return a**b
	return inner2

@sum_number
def sum(a,b):
	print('From Sum= ',a+b)
print("From inner 1= ",sum(2,3))   #Call inner 1
print("From inner 2= ",sum(2,2))   #Call inner 2

