notas = []
n = int(input("Ingrese la cantidad de notas"))
for i in range(n):
       notas.append(float(input(f"ingrese la nota {i+1}:")))
  
suma = 0

for i in range(len(notas)):
    suma += notas[i]
print(f"las notas{notas}")
print(f"El promedio es: {suma/len(notas)}")