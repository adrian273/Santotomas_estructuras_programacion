
# ___Sistema de gestión de pagos___

La empresa NovaVisio actualmente se encuentra realizando gestión de pagos de sueldos y cotizaciones con un proceso informático implementado  mediante una planilla Excel. Cada mes se debe calcular por trabajador su sueldo, incluyendo horas extras, bonos,  monto a descontar por pago de cotizaciones de AFP e Isapre.
El problema surge cuando muchos datos deben ser modificados, y aunque hay funciones y macros implementadas, la planilla crece de manera exponencial, haciéndose inmanejable en algunos casos. 
Para satisfacer la necesidad  dentro de estos procesos, se le ha solicitado a Usted como desarrollador en Python crear una plataforma de gestión de pagos, siguiendo las especificaciones que se explicitan a continuación:

***
__En la empresa existe la siguiente categoría de empleados:__ 
1. Novato 
2. Experto 
3. Supervisor 
4. Administrativo
***
__Control de Autentificación:__
1. El sistema debe contar con un control de autentificación. Es decir, al empezar el programa, deberá pedir Usuario y Contraseña. 
2. El usuario administrador inicial y contraseña los puede definir a su criterio.
***
__Menú de opciones: Cuando el usuario accede al sistema, dispondrá de las siguientes opciones:__
1. Ingresar datos
2. Calcular sueldo
3. Listar Empleados
4. Listar Liquidaciones
***
__Ingresar datos: Para generar una liquidación de sueldo, se deben considerar los siguientes datos:__
1. Datos a Ingresar:
    1. Mes
    2. Año
    3. Rut del trabajador
    4. Nombre del trabajador
    5. Categoría.
    6. Días ausencia
    7. AFP
    8. Sistema salud, que puede ser A, B o C.
    9. Monto sueldo bruto
***
__Calcular sueldo:__
1. Después de realizar el ingreso de la información solicitada en el punto anterior, se debe calcular el monto de pago de sueldo líquido e imprimir la liquidación con todos los datos, incluido el monto a pagar
2. Reglas a considerar:
    1. Los campos no deben estar vacíos.
    2. El monto del sueldo bruto no puede ser negativo
    3. La cantidad de días de ausencia no puede ser negativo o mayor a 30
    4. En caso no haber faltado al trabajo debe tener un bono de $50.000 extra.
    5. Si Categoría es Experto el bono se paga doble
    6. El porcentaje de descuento por AFP es el 10% del sueldo bruto
    7. El porcentaje de descuento por Sistema de salud es el siguiente:
        1. Si Sistema de salud es A corresponde un 5,7%
        2. Si Sistema de salud es B corresponde un 6,1%
        3. Si Sistema de salud es C corresponde un 6,5%
***
__Listar Empleados:__ 
1. El usuario autentificado, podrá listar todos los empleados registrados
***
__Listar Liquidaciones:__ 
1. el usuario autentificado, podrá listar todas las liquidaciones de sueldo según las siguientes opciones:
    1. Por mes y año
    2. Por rut
