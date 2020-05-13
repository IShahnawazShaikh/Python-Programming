import urllib.request

def download(url,filepath,filename):
	full_path=filepath+filename+'.jpg'
	urllib.request.urlretrieve(url,full_path)



url=input('enter url of the image: ')
filaname=input('Enter Filaname to save as: ')
download(url,'images/',filaname)
