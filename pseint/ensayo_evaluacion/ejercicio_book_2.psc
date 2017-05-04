Proceso Bucle
	Definir value, desc, r, i Como Real;
	Para i = 1 Hasta 10 Hacer
		Escribir "ingrese valor";
		Leer value;
		Si value > 100000 Entonces
			desc = value * 0.1;
			r = value - desc;
			Escribir "El valor total es $", r;
		Sino
			Si value > 50000 y value < 100000 Entonces
				desc = value * 0.05;
				r = value - desc;
				Escribir "El valor total es $", r;
			Sino
				Si value > 10000 y value < 50000 Entonces
					desc = value * 0.03;
					r = value - desc;
					Escribir "El valor total es $", r;
				FinSi
			FinSi
		FinSi
	FinPara
FinProceso
