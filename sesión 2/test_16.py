"""
Requisitos:

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)
3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //
6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia
"""
#DESARROLLO

entero1 = 10
entero2 = 5
flotante1 = 3.5
flotante2 = 2.7
variable_string = "Hola"
string_numerico = "20"
booleano = True

suma_entero_string = entero1 + int(string_numerico)
print("Suma de entero y string numérico:", suma_entero_string)

suma_total = entero1 + entero2 + int(string_numerico ) + flotante1
print("Suma total:", suma_total)

modulo_enteros = entero1 % entero2
print("Módulo de los enteros:", modulo_enteros)

division_entera = entero1 // entero2
print("Parte entera de la división:", division_entera)

potencia = flotante1 ** entero1
print("Potencia:", potencia)
