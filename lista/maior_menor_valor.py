entrada = [-7, -2, -9, -4, -1]

maior = menor = entrada[0]

for num in entrada:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(maior, menor)