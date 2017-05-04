Proceso G5_ejercicio_3
	Definir total, salary, n_cargo, value_hours, hours_work, i Como Real;
	total = 0;
	Para i = 1 Hasta  50
		Escribir "Ingresa horas de trabajo";
		Leer hours_work;
		Escribir "Ingresa valor hora";
		Leer value_hours;
		Escribir "Ingrese numero de cargas";
		Leer n_cargo;
		salary = hours_work * value_hours;
		Escribir salary;
		Si n_cargo >= 3 Entonces
			salary = salary * 1.1;
		Sino
			Si n_cargo = 1 o n_cargo = 2 Entonces
				salary = salary * 1.05;
			FinSi
		FinSi
		total = salary + total; 
		Escribir "El salario es ", salary;
	FinPara
	Escribir "El total a pagar es de : $", total;
FinProceso
