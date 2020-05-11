class Area:
	def areaCircle(self):
		return (self.side*self.side)
	def areaSquare(self):
		return (self.side*self.side*3.14)
	def __init__(self,side):
          self.side=side
