entrada = [1, 2, 3, 4, 5]

impar = [num for num in entrada if num%2 != 0]

answ = 0
if impar != []:
    answ = sum(impar) / len(impar)
    print(answ)
else:
    print("Lista vazia")