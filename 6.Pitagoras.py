#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2. 

catetoA = float(input("Ingrese cateto a "))
catetoB = float(input("Ingrese cateto b "))

hipo = (catetoA**2 + catetoB**2)**0.5 #elevar a la 0.5 equivale a la raiz cuadrada
print(f"la hipotenusa es {hipo}")