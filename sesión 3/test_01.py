"""Listas en Python"""

"""Listas -> pop(): Quita un elemento de una posición dada"""
#Índices:    0        1         2          3         4
paises = ["Perú", "Canadá", "Argentina", "México", "España"]

print("Mi lista inicial: {}".format(paises))

paises.pop() #En este caso elimina el último elemento.
print("Mi lista actualizada es: {}".format(paises))

print("paises[2]: {}".format(paises[2]))
paises.pop(1)
print("Mi lista actualizada es: {}".format(paises))

paises.pop(2)
print("Mi lista actualizada es: {}".format(paises))


