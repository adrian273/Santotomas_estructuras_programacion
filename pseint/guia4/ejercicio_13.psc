Proceso ejercicio_13
	Definir number_cargo, salary Como Real;
	Escribir "Ingresar sueldo";
	Leer salary;
	Escribir "Ingrese numero de cargas";
	Leer number_cargo;
	Si (number_cargo >= 2) Entonces
		salary = salary * 1.2;
		Escribir "El salario es: ", salary;
	FinSi
	Si (number_cargo = 1) Entonces
		salary = salary * 1.1;
		Escribir "El salario es: ", salary;
	FinSi
	Si (number_cargo = 0) Entonces
		salary = salary * 1.05;
		Escribir "El salario es: ", salary;
	FinSi
FinProceso
