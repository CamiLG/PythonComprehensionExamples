#p={ x, x ≡ N , x % 2 == 0 } definimos un conjunto acotado de numeros pares

pares = [x for x in range(0, 11) if x % 2 == 0]
print(len(pares))
#imprime la cantidad de pares que hay de 0 a 10
