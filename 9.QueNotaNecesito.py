N1 = float(input('Ingrese nota del examen 1:'))
N2 = float(input('Ingrese nota del examen 2:'))
Nlab = float(input('Ingrese nota del laboratorio:'))

Nc = (10*60-3*Nlab)/7
N3 = 3*Nc-N1-N2

print(f'Necesita nota {N3} en el examen 3')