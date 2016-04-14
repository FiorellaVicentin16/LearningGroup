print ("				AFIP				")
print("		Sistema de Facturacion Electronica para Consumidor Final")

print(" ")
print(" ")

importeTotal = input ("Ingrese valor de importe total: ")
print(" ")

impuestos = input ("Ingrese impuestos: ")
print(" ")

importeNeto = importeTotal - impuestos

if importeNeto > 0:
	if importeTotal > 5000:
		print("Monto Superado para Consumidor Final")

elif importeNeto == 0:
	print ("Error. El monto de importe neto es nulo")

else:
	print("Error. Los impuestos ingresados son mayores que el importe total")

	