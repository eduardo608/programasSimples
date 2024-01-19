#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

horaAct = int(input("Ingrese la hora actual\n"))
horaFut = int(input("ingrese la cantidad de horas a sumar\n"))

horafutura = (horaAct + horaFut) % 24 #mod porque al hacer la division entre horaactual + hora futura y dividirla por 24 que son las horas del reloj me va a dar como residuo un numero, el cual es la hora futura 

print(f"En {horaFut} horas, el reloj marcara las {horafutura}:00")