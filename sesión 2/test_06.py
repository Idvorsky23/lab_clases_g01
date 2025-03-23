"""
Requisitos
 1. Crear las variables para los valores de nombre, profesión y ciudad
 2. Crear 2 variables para remuneración de enero y febrero
 3. Crear 1 variable donde se sumará el ingreso de  los meses de enero  febrero
 4. Mostar en pantalla el mensaje de:
    "Hola soy 'nombre' mi profesión 'profesión' y mi remuneración acumulable es de 'remuneración total"
"""

nombre = "Cesar"
profesion = "Ing. Electrónica"
ciudad = "Lima"

enero = 3000
febrero = 3000
suma= enero + febrero

print("Hola, soy {}, mi profesión {}, y mi remuneración acumulable es de: {} " .format(nombre, profesion, suma))