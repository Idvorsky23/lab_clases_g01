"""
Requisitos:

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"
Hora máximo de envío: 8 pm

Correo a enviar solución: cerseuufisi@gmail.com
Asunto: participación 23 Mar - nombre apellido 

"""

# Solicitar datos del empleado
nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
distrito = input("Ingrese su distrito: ")
sueldo = float(input("Ingrese su sueldo mensual: "))

# Calcular el bono final del año
bono_final = (sueldo * 3) - (sueldo * 0.10)

# Mostrar los resultados
print("Empleado:{} {}" .format(nombre, apellido_paterno))
print("Distrito:{}" .format(distrito))
print("Sueldo mensual:{}" .format(sueldo))
print("Bono anual:{}" .format(bono_final))