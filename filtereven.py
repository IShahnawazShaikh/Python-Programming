number=[1,2,3,4,2,6,7,2,9,10]
filter_list=[]
def even_num(n):
	return n%2==0


print(list(filter(even_num,number)))

print([n for n in number if n%2==0])  



print(list(map(lambda a:a*a,number)))

def func():
	return lambda a,b:a*b
lamb=func()
print(lamb(3,4))