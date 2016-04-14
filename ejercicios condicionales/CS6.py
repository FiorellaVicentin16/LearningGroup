#-*- coding: utf-8 -*-

print("				ANSES")
print ("	Clasificacion de jubilados")
print ("")
print ("")

edad = input ("Ingresa edad: ")
antiguedad = input ("Ingrese antigüedad: ")


if edad >= 60 and antiguedad < 25:
	print ("La persona esta adscripta a la jubilacion por edad")

elif edad < 60 and antiguedad >= 25:
	print ("La persona esta adscripta por jubilacion joven")

elif edad >= 60 and antiguedad >= 25:
	print (u"La persona esta adscripta por antigüedad adulta")

