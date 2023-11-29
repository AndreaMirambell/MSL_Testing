def writefile():

	#Escribir
	f = open ('ejemplo.txt', 'w')
	f.write('Andrea Mirambell')
	f.close()

def readfile():

	#Leer
	f = open ('ejemplo.txt', 'r')
	leer = f.read()
	print(leer)
	f.close()


#Automatización
def automatizacion():
	print ("Hola")
if __name__ == '__main__':
	writefile()
	readfile()



