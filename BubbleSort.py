def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]

lista_ejemplo = [58, 52, 5, 12, 69, 87, 12]

bubble_sort(lista_ejemplo)

print ("Lista ordenada:")
for i in lista_ejemplo:
	print (str(i))
