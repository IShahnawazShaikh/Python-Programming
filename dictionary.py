def display_player(myDic):
  for key,val in myDic.items():
	  print(f'I am {key} with {val} belt color')
def belt_count(myDic):
  belts=list(myDic.values())
  print(set(belts))
  for belt in set(belts):
    count=belts.count(belt)
    print(f'{count} {belt} belt') 

myDic={} 
while True:
	key=input("enter name of the ninja: ")
	val=input("enter belt color: ")
	status=input('add another ninja ? Y/N: ')
	myDic[key]=val
	if status=='Y':
	 continue
	else:
	 break
display_player(myDic)
belt_count(myDic);