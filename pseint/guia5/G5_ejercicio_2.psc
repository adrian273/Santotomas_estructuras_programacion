Proceso G5_ejercicio_2
	Definir n_students, i, notes, prom, prom_g Como Real;
	Definir count Como Entero;;
	prom = 0;
	count =0;
	Escribir "Numero de estudiantes";
	Leer n_students;
	Para i = 1 Hasta n_students
		Escribir "Ingrese notas";
		Leer notes;
		Si notes < 4.0 Entonces
			count = count + 1;
		FinSi
		prom = notes + prom;
	FinPara
	count = count * 100 / n_students;
	prom_g = prom / n_students;
	Escribir "Promedio de notas ", prom_g;
	Escribir "El porcentaje de reprobados es %",count;
FinProceso
