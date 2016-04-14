#-*- coding: utf-8 -*-
#Esto es para que te tome la ñ supuestamente. Puede ser que igual no salga la ñ, sino un simbolo raro. 

nacimiento = input("Ingrese año de nacimiento: ")
actual = input(u"Ingrese año actual: ")		#La u inicial es por unicode, todavia no tengo bien en claro porque se pone ahi, lo puse porque asi pasaron en el grupo del Inf.

edadFutura = actual + 1 - nacimiento
print(edadFutura)