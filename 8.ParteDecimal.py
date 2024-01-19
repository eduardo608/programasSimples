#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numeroReal = float(input("Ingrese el numero real: "))

numeroDec = numeroReal - int(numeroReal) #Resta el entero del numero real

print(f"{numeroDec}")
