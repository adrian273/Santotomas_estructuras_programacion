Proceso G5_ejercicio_6
	Definir time, number_person, prom_time, time_less, time_higher Como Real;
	number_person = 0;
	prom_time = 0;
	time_less = 1000000;
	time_higher = 0;
	Escribir "Ingrese Tiempo en llegar";
	Leer time;
	Mientras time > 0 Hacer
		number_person = number_person + 1;
		prom_time = time + prom_time;
		Si time_less > time Entonces
			time_less = time;
		FinSi
		Si time_higher < time Entonces
			time_higher = time;
		FinSi
		Escribir "Ingrese Tiempo en llegar";
		Leer time;
	FinMientras
	prom_time = prom_time / number_person;
	Escribir "El numero de personas que llegaron son ", number_person;
	Escribir "El tiempo promedio de la maraton es:", prom_time;
	Escribir "El tiempo menor es ", time_less;
	Escribir "El tiempo mayor es ", time_higher;
FinProceso

