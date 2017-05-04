Proceso ejercicio_7
	Definir time_work, value_time, number_cargo, salary, salary_bono Como Real;
	Escribir "Ingrese Horas de trabajo";
	Leer time_work;
	Escribir "Ingrese valor hora";
	Leer value_time;
	Escribir "Ingrese numero de carga";
	Leer number_cargo;
	salary = time_work * value_time;
	Si number_cargo >= 3 Entonces
		salary_bono = salary * 1.1;
		Escribir "El salario final es $", salary_bono;
	Sino
		Si number_cargo = 2 Entonces
			salary_bono = salary * 1.05;
			Escribir  "El salario final es $", salary_bono;
		Sino
			salary_bono = salary * 1.03;
			Escribir "El salario final es $", salary_bono;
		FinSi
	FinSi
FinProceso
