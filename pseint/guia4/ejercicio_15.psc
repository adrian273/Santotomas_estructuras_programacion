Proceso ejercicio_15
	Definir n1, n2, n3 Como Real;
	Escribir "Ingrese numero 1";
	Leer n1;
	Escribir "Ingrese numero 2";
	Leer n2;
	Escribir "Ingrese numero 3";
	Leer n3;
	Si (n1 > n2 y n1 < n3 o n1 > n3 y n1 < n2) Entonces
		Escribir "El valor intermedio es ", n1;
	FinSi
	Si (n2 > n3 y n2 < n1 o n2 > n1 y n2 < n3) Entonces
		Escribir "El valor intermedio es ", n2;
	FinSi
	Si (n3 > n2 y n3 < n1 o n3 < n2 y n3 > n1) Entonces
		Escribir "El valor intermedio es ", n3;
	FinSi
FinProceso
