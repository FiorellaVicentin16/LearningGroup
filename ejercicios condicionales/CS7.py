#-*- coding: utf-8 -*-

print ("El siguiente programa determina si un año ingresado por teclado es bisiesto o no")
print (" ")
print (" ")

año = input("Ingrese año: ")

if año % 4 == 0:
	if año % 400 == 0:
		if año % 100 == 0:
			print ("El año %s NO es bisiesto" %(año))
		else:
			print ("El año %s SI es bisiesto" %(año))
	else:
		print ("El año %s SI es bisiesto" %(año)) 
	
else:
	print ("El año %s NO es bisiesto" %(año))
