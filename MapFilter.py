number=[1,2,3,4,2,6,2,2,9,10]
def even_num(n):
	return n!=2
print(list(filter(even_num,number))