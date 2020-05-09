class Student:
  course='Computer Science Engineering'
  def __init__(self,name,age):
	    self.name=name
	    self.age=age
  def func(self):
  	  print(f'Name of the Student is {self.name} of age {self.age} enrolled in course {self.course}')

s1=Student('shahnawaz',22)
s2=Student('Devendra',20)
s1.func()
s2.func()
print(s1.course)
print(Student.course)
# print(Student.name)   ------>  error beacuse name is instance attribute
