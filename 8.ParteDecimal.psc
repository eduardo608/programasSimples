Algoritmo ParteDecimal
	
	definir numeroReal, numeroDec Como Real
	
	EScribir "Ingrese el numero real: "
	Leer  numeroReal
	
	numeroDec = numeroReal - TRUNC(numeroReal)
	
	Escribir ,numeroDec
	
	
FinAlgoritmo
