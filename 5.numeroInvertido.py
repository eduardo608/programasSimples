#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

numero = input("Digite el numero")

numeroInvertido = []

for i in range (len(numero)):
    numeroInvertido.append(numero[-i-1])

print(' '.join(numeroInvertido))