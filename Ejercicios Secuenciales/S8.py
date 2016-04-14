#Matematica
examenMat = input("Exame de Matematica: ")
tareaMat1 = input("Nota primer tarea: ")
tareaMat2 = input("Nota segunda tarea: ")
tareaMat3 = input("Nota tercer tarea: ")
cantTareasMat = 3
promTareasMat = (tareaMat1 + tareaMat2 + tareaMat3) / cantTareasMat
print(" ")
promedioMat = examenMat * 0.9 + promTareasMat * 0.1
print "Nota promedio de Matematica: ",promedioMat
print(" ")
print(" ")

#Fisica
examenFis = input("Examen de Fisica: ")
tareaFis1 = input("Nota primer tarea:")
tareaFis2 = input("Nota segunda tarea:")
cantTareasFis = 2
promTareasFis = (tareaFis1 + tareaFis2) / cantTareasFis
print(" ")
promedioFis = examenFis * 0.8 + promTareasFis * 0.2
print "Nota promedio de Fisica",promedioFis
print(" ")
print(" ")

#Quimica
examenQuim = input("Examen de Quimica: ")
tareaQuim1 = input("Nota primer tarea: ")
tareaQuim2 = input("Nota segunda tarea:")
tareaQuim3 = input("Nota tercer tarea: ")
cantTareasQuim = 3
promTareasQuim = (tareaQuim1 + tareaQuim2 + tareaQuim3) / cantTareasQuim
print(" ")
promedioQuim = examenQuim * 0.85 + promTareasQuim * 0.15
print "Nota promedio de Quimica",promedioQuim
print(" ")
print(" ")


promedioGral = (promedioMat + promedioFis + promedioQuim) / 3
round(promedioGral,2)

print "Promedio general",round(promedioGral,2)