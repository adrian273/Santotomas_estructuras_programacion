//Praticano para la prueba
Proceso Ejercicio_1_test
	Definir number, result_mod, i Como Real;
	Escribir "Ingrese un numero";
	Leer number;
	result_mod = number MOD 2;
	Si result_mod = 0 Entonces
		number = number - 1;
	FinSi
	Para i = 0 Hasta 100 
		number = number + 2;
		Si number < 100 Entonces
			Escribir  "Los numeros impares ", number;
		FinSi
	FinPara
FinProceso
