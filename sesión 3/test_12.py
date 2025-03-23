"""Requisitos:
-Crear dos lista de personas vacías
-Agregar los datos de nombre, edad y profesión para ambas listas
-Obtener y mostrar la suma de las edad // por indica
-Sumar ambas listas y mostrar el resultado en la terminal
-Mostrar de manera inversa la suma de ambas listas
-Actualizar la nueva lista eliminando las edades de ambas personas
-Mostrar la lista vacia de la segunda persona aplicando el método respectivo"""

"""Programa que trabaja con listas en Python"""
# Crear dos listas de personas vacías
persona_1 = []
persona_2 = []
# Agregar datos a ambas listas (nombre, edad, profesión)
persona_1.append(["Cesar", 25, "Ingeniero Electrónica"])
persona_2.append(["Karen", 24, "Abogada"])
# Obtener y mostrar la suma de las edades usando el índice
suma_edades = persona_1[0][1] + persona_2[0][1]
print("Suma de las edades:", suma_edades)
# Sumar ambas listas
lista_unida = persona_1 + persona_2
print("Lista combinada:", lista_unida)
# Mostrar la lista combinada en orden inverso
lista_inversa = lista_unida[::-1]
print("Lista en orden inverso:", lista_inversa)
# Eliminar las edades de ambas personas usando el índice
persona_1[0].pop(1)  # Elimina la edad de la primera persona
persona_2[0].pop(1)  # Elimina la edad de la segunda persona
# Actualizar la lista combinada sin edades
lista_unida = persona_1 + persona_2
print("Lista sin edades:", lista_unida)
# Vaciar la segunda lista aplicando el método correspondiente
persona_2.clear()
print("Segunda lista vacía:", persona_2)