class Base:
	def displayCourse(self):
		return self.course
	def displayName(self):
		return self.name
	def __init__(self,name,course):
           self.name=name
           self.course=course
           
def call():
	print('call')
# base=Base("shahnawaz","CSE")
# print(base.displayName())
# print(base.displayCourse())
           