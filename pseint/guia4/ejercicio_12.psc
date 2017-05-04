Proceso ejercicio_12
	Definir n1, n2, result Como Real;
	Escribir "Ingrese dos numeros";
	Leer n1, n2;
	Si (n1 > n2) Entonces
		result = n1 * n2;
		Escribir "El resultado es ", result;
	FinSi
	Si (n2 > n1 y n2 != 0 ) Entonces
		result = n1 / n2;
		Escribir "El resultado es ", result;
	FinSi
	Si (n2 = 0) Entonces
		Escribir "No se puede calcular";
	FinSi
	
FinProceso
