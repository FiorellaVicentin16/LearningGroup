#Este programa calcula el sueldo final de un trabajador en base a la asistencia  y la cantidad de horas extra.


sueldo =input("Introduzca sueldo: ")

asistencia = int(input("El empleado asistio todo el mes?. Pulse 1 para SI o 0 para NO: "))

horasExtra = int(input("Introduzca cantidad de horas adicionales trabajadas por el empleado: "))

if asistencia == 1:
	if horasExtra >= 3 and horasExtra <= 5:
		sueldo = sueldo * 1.03

	elif asistencia == 1 and horasExtra >= 6 and horasExtra <= 10:
		sueldo = sueldo * 1.10

elif asistencia == 0:
	if horasExtra >= 3 and horasExtra <= 10:
		sueldo = sueldo * 1.02

else:
	print"Opcion ingresada NO valida"


print ("Sueldo final del empleado: ",sueldo)# Colocado con parentesisi para permitir la ejecucion en la version 3.5

