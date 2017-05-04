Proceso Ensayo_ejercicio2
	Definir nota, alumnos, nota_roja, nota_azul, sum_nota Como Real;
	Definir num_alumno Como Entero;
	nota_azul = 0;
	nota_roja = 0;
	sum_nota = 0;
	num_alumno = 2;
	Para alumnos = 1 Hasta num_alumno
		escribir "nota alumno:";
		leer nota;
		si nota < 4.0 Entonces
			nota_roja = nota_roja + 1;
		Sino
			nota_azul = nota_azul + 1;
		FinSi
		si nota > 3.5 y nota < 4.0 Entonces
			sum_nota = sum_nota + 1;
		FinSi
	FinPara
	nota_azul = nota_azul * 100 / num_alumno;
	nota_roja = nota_roja * 100 / num_alumno;
	Escribir "nota rojas: ",nota_roja,"%";
	Escribir "nota azul: ", nota_azul, "%";
	Escribir "El numero de notas entre 3.5 y 4.0 es : ", sum_nota;
FinProceso