presion = input("Introduzca valor de presion: ")
volumen = input("Introduzca valor de volumen: ")
temperatura = input("Introduzca valor de temperatura: ")

x = presion * volumen
y = 0.37 * (temperatura + 460)

masa = x / y

print (masa)