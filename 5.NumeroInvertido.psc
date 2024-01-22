Algoritmo NumeroInvertido
	Definir n, numerooInvertido Como Real
	numerooInvertido <- 0
	Escribir 'Digite el numero'
	Leer n
	Mientras n>0 Hacer
		numerooInvertido <- numerooInvertido*10
		numerooInvertido <- numerooInvertido+n MOD 10
		n <- TRUNC(n/10)
	FinMientras
	Escribir numerooInvertido
FinAlgoritmo
