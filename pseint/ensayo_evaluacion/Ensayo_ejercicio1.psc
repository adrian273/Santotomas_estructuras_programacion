Proceso Ensayo_ejercicio1
	definir tiempo,estatura, num_person, prom_maraton, prom_estatura, prom_edad, tiempo_mayor, edad_menor, num_fem Como Real;
	definir edad Como Entero;
	Definir genero Como Caracter;
	num_person = 0;
	prom_maraton = 0;
	prom_estatura = 0;
	prom_edad = 0;
	tiempo_mayor = 0;
	edad_menor = 15500500;
	num_fem = 0;
	Escribir "Ingresar estatura";
	Leer estatura;
	Mientras estatura <> 0 Hacer
		Escribir "tiempo";
		Leer tiempo;
		prom_maraton = prom_maraton + tiempo;
		prom_estatura = prom_estatura + estatura;
		Escribir "Ingresar edad";
		Leer edad;
		prom_edad = prom_edad + edad;
		num_person = num_person + 1;
		Escribir "Genero";
		Leer genero;
		Si genero = "femenino" Entonces
			num_fem = num_fem + 1;
		FinSi
		Si tiempo_mayor < tiempo Entonces
			tiempo_mayor = tiempo;
		FinSi
		Si edad_menor > edad Entonces
			edad_menor = edad;
		FinSi
		Escribir "Ingrese estatura";
		Leer estatura;
	FinMientras
	num_fem = num_fem * 100 / num_person;
	prom_maraton = prom_maraton / num_person;
	prom_estatura = prom_estatura / num_person;
	prom_edad = prom_edad / num_person;
	Escribir "El numero que llegaron es ", num_person;
	Escribir "El promedio de la maraton es ", prom_maraton;
	Escribir "El promedio de la estatua es ", prom_estatura; 
	Escribir "El promedio de la edad es ", prom_edad;
	Escribir "El numero mayor ", tiempo_mayor;
	Escribir "La edad menor es ", edad_menor;
	Escribir "El porcentaje de mujeres es ", num_fem,"%";
FinProceso 
