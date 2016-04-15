# -*- coding: utf-8 -*-

print (u"El siguiente programa determina si un año ingresado por teclado es bisiesto o no")
print (" ")
print (" ")

ano = input("Ingrese ano: ")

if ano % 4 == 0:
	if ano % 400 == 0:
		if ano % 100 == 0:
			print (u"El ano %s NO es bisiesto" %(ano))
		else:
			print (u"El ano %s SI es bisiesto" %(ano))
	else:
		print (u"El ano %s SI es bisiesto" %(ano)) 
	
else:
	print (u"El ano %s NO es bisiesto" %(ano))
