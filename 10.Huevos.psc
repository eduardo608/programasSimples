Algoritmo Huevos
	
	Definir TH, TE, M, P, C, K, dividendo, resultado, resultado2, segundoss, minutoss Como Real
	
	Escribir "Temperatura original"
	Leer TH

	TE = 100
	M = 47
	P = 1.038
	C = 3.7
	K = 0.0054
	
	dividendo = M^(2/3)*(C*(P^(1/3)))
	divisor = K*(PI^2)*(((4*PI)/3)^(2/3))
	resultado = dividendo / divisor
	resultado2 = ln(0.76)*(TH - TE) / (70-TE)
	segundoss = resultado * resultado2
	minutoss = TRUNC(segundoss/60)
	
	EScribir "En segundos es: ", segundoss " s"
	Escribir "En minutos es: ", minutoss " min"
	
	
	
	
	
	
FinAlgoritmo
