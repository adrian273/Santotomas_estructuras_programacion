Proceso ejercicio_1
	Definir number, result, i Como Entero;
	Escribir "Ingrese un numero";
	Leer number;
	result = number MOD 2;
	Si result = 0 Entonces
		number <- number -1;
	fin si
		Para i = 1 Hasta  100
			number = number + 2;
			Si number < 100 Entonces
				Escribir number;
			FinSi
		FinPara
FinProceso
