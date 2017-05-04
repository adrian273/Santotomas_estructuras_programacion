Proceso Ejercicio_5
	Definir number, result, mod_result Como Real;
	Escribir "ingrese un numero";
	Leer number;
	result = number % 2;
	Si result = 0 Entonces
		mod_result = number - 1;
		Escribir "El antecesor de ", number, " es ", mod_result;
	Sino
		mod_result = number + 1;
		Escribir "El sucesor de ", number, " es ", mod_result;
	FinSi
FinProceso
