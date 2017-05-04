Proceso ejercicio_4
	Definir prom, ex, end Como Real;
	Escribir "Ingrese promedio";
	Leer prom;
	Escribir "Ingrese examen";
	Leer ex;
	end = (prom * 0.7) + (ex * 0.3);
	Si end >= 4 Entonces
		Escribir "El alumno aprobo";
	Sino
		Escribir "El alumno reprobo";
	FinSi
FinProceso
