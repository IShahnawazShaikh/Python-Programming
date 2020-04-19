def printName(*argument):
	for var in argument:
	 print(var)
printName('a','b','c','d',7,8)

# Lambda Function

sum=lambda a,b: a+b

print(sum())