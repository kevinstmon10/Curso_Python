numeros = input("Escribe los numeros de la loteria: ")
lista = numeros.split(',')  # Separamos el input por ,
num = []  # declaramos un array vacio para su conversion
for element in lista:
    num.append(int(element))  # llenamos el array con el numero como entero
num.sort()  # Ordernamos la lista
print(num)
