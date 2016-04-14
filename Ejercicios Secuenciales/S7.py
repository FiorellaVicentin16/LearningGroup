print "Calculo del porcentaje de inversion de empresarios con respecto a la cantidad total invertida"
print (" ")
print (" ")

inversion1 = input("Ingrese cantidad invertida por el primer empresario: ")
inversion2 = input("Ingrese cantidad invertida por el segundo empresario: ")
inversion3 = input("Ingrese cantidad invertida por el tercer empresario: ")

total = float(inversion1 + inversion2 + inversion3)

porc1 = (100 * inversion1)/ total
porc2 = (100 * inversion2)/ total
porc3 = (100 * inversion3)/ total

print "Con respecto al total, la inversion del primer empresario fue de un: ",round(porc1,2), "%"
print "Con respecto al total, la inversion del segund empresario fue de un: ",round(porc2,2), "%"
print "Con respecto al total, la inversion del tercer empresario fue de un: ",round(porc3,2), "%"

