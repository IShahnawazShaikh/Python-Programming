from restaurat_module import Al_Nazeer
customer1=Al_Nazeer('Shahnawaz')
customer1.add_item('chicken_changz')
customer1.add_item('Mutton_changz')
customer1.add_item('Water')
customer1.generate_bill(10,10)

customer2=Al_Nazeer('Pasha')
customer2.add_item('chicken_changz')
customer2.add_item('Paya')
customer2.add_item('Soft_drink')
customer2.generate_bill(10,10)