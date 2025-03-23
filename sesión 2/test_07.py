"""Reconocimiento de tipos de datos: type()"""
from sqlparse.utils import LINE_MATCH

"""Creación varaibles"""

nombre = "Luis"
ciudad = "Lima"
saldo = 5000
empresa = False
correo = "Luis@gmail.com"
empleado = [nombre, saldo, empresa, ciudad]
empleado_d = {'nomb': nombre, 'ciud': ciudad, 'sald': saldo, 'empre': empresa, 'cor': correo}

print("Tipo de dato de mi variable 'nombre' es: {}" .format(type(nombre)))
print("Tipo de dato de mi variable 'ciudad' es: {}" .format(type(ciudad)))
print("Tipo de dato de mi variable 'saldo' es: {}" .format(type(saldo)))
print("Tipo de dato de mi variable 'empresa' es: {}" .format(type(empresa)))
print("Tipo de dato de mi variable 'correo' es: {}" .format(type(correo)))
print("Tipo de dato de mi variable 'empleado' es: {}" .format(type(empleado)))
print("Tipo de dato de mi variable 'empleado_d' es: {}" .format(type(empleado_d)))
print("el tipo de dato es: ",type(nombre))