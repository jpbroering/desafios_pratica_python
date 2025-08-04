# Não pode usar .reverse() nem list[::-1]

lista = [1, 2, 3, 4]

answ = []

for n in range(len(lista)):
    answ.append(lista[len(lista)-(1+n)])
print(answ)