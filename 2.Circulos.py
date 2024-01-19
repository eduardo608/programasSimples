#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

radio = float(input("Escriba el radio\n "))

area = 3.14 * radio **2
perimetro = 2 * 3.14 *radio
print(f"el area del circulo es {area}")
print(f"el perimetro del circulo es {perimetro}")