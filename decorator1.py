def greeting(func):
	def innerFunction(name):
		print('Good Morning')
		func(name)
		print('how are You')
	    
	return innerFunction;
  	
@greeting
def greet(name):
	print(name)
greet('Shahnawaz')

