Algoritmo QueNotaNecesito
	
	Definir n1, n2, nlab, nc, n3 Como Real
	
	Escribir "Ingrese nota del examen 1: "
	Leer n1
	Escribir "Ingrese nota del examen 2: "
	Leer n2
	Escribir "Ingrese nota del laboratorio: "
	Leer nlab
	
	nc = (10*60) -3 *nlab / 7
	n3 = 3*nc-n1-n2
	
	EScribir "Necesita nota ",n3 " en el examen 3"
	
FinAlgoritmo
