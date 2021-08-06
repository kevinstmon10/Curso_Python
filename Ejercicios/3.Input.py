#valor = input("Escribe un valor: ")
# print(type(int(valor)))

# Solucion 1
a = 5
b = 2
print("valor de inicial de a: " + str(a))
print("valor de inicial de b: " + str(b))

a, b = b, a

print("valor de final de a: " + str(a))
print("valor de final de b: " + str(b))
