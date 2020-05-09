class Student:
  def __init__(self,name,age):
	    self.name=name
	    self.age=age
  def func(self):
  	  print(f'Name of the Student is {self.name} of age {self.age}')

s1=Student('shahnawaz',22)
s2=Student('Devendra',20)
s1.func()
s2.func()
