cond = int(input("Seleccione que Area desea dibujar 0->Circulo 1->Triangulo "))
print("")
pi = 3.14

if cond == 1:
	base = input("Ingrese la base del Triangulo a dibujar: ")
	altura = input("Ingrese la altura del Triangulo a dibujar: ")
	print ""
	print "El Area del Triangulo es: ", (base*altura)/2
elif cond == 0:
	radio = input("Ingrese Radio del Circulo a dibujar: ")
	print ""
	print "El Area del Circulo es: ",pi*(radio**2)

else:
	print("Opcion Ingresada NO VALIDA")		