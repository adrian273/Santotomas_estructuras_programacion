Proceso ejercicio_14
	Definir number_one, result_mod Como Real;
	Escribir "Ingrese un numero";
	Leer number_one;
	result_mod = number_one % 2;
	Si result_mod = 0 Entonces
		result_mod = number_one + 1;
		Escribir "El impar siguiente es: ", result_mod;
	Sino
		result_mod = number_one + 2;
		Escribir "El impar siguiente es: ", result_mod;
	FinSi
FinProceso
