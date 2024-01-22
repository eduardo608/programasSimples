Algoritmo HoraFutura
	
	definir horaAct, horapfutura, horasum Como Real
	
	EScribir "Ingrese la hora actual"
	Leer horaAct
	EScribir "Ingrese la cantidad de horas a sumar"
	Leer horasum
	
	horapfutura = (horaAct + horasum) mod 24
	
	EScribir "En ", horaAct " horas, el reloj marcara las ", horapfutura ":00"
	
	
	
FinAlgoritmo
