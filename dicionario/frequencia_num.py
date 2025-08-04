entrada = [1, 2, 2, 3, 3, 3,4,4,4,4,5,6,5,5,6,6]

answ = {}

for num in set(entrada):
    answ[num] = entrada.count(num)

print(answ)