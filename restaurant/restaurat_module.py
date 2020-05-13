class Al_Nazeer:
    menu={
      'chicken_changz':120,
      'Mutton_changz':320,
      'Beef':190,
      'Paya':190,
      'Soft_drink':85,
      'Water':30
    }
    def __init__(self,name):
    	self.name=name
    	self.total=0
    	self.items=[]
    	print('Bill for the ',self.name)
    def add_item(self,item):
    	self.total+=self.menu[item]
    	self.items.append(item)
    def generate_bill(self,tax,service):
    	for item in self.items:
    		print(f'{item:20} ${self.menu[item]}')
    	print(f'{"Total":20} {self.total+((tax/100)*self.total)+((service/100)*self.total)}')

           