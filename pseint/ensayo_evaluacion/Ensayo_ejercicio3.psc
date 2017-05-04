Proceso sin_titulo
	Definir ht, vt, cargas, sueldo_n, sueldo_prom, n_trabajadores, prom_h Como Real;
	Escribir "ingresar horas trabajo ";
	Leer ht;
	sueldo_prom = 0;
	n_trabajadores = 0;
	prom_h = 0;
	Mientras ht <> 0 Hacer
		Escribir "Ingresar valor horas de trabajo ";
		Leer vt;
		Escribir "Ingresar n cargas ";
		Leer cargas;
		sueldo_n = ht * vt;
		Si cargas > 3 Entonces
			sueldo_n = sueldo_n * 1.12;
		FinSi
		Si cargas = 1 o cargas = 2 Entonces
			sueldo_n = sueldo_n *1.07;
		FinSi
		sueldo_prom = sueldo_prom + sueldo_n;
		prom_h = prom_h + ht;
		Escribir "El sueldo es ", sueldo_n;
		n_trabajadores = n_trabajadores + 1;
		Escribir "ingresar horas trabajo ";
		Leer ht;
	FinMientras
	sueldo_prom = sueldo_prom / n_trabajadores;
	prom_h = prom_h / n_trabajadores;
	Escribir "El sueldo promedio de los trabajadores es ", sueldo_prom;
	Escribir "El promedio de horas trabajadas es ", prom_h;
FinProceso
