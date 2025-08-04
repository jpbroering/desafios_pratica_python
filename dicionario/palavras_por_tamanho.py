entrada = "Hoje é um ótimo dia para programar"

caracteres_especiais = [",", ".", "!", "?", ":", ";", "'", "[", "]", "{", "}", "(", ")", '"']

entrada = entrada.lower()

for caracter in caracteres_especiais:
    entrada = entrada.replace(caracter,"")

saida = {}

entrada = entrada.split()

for palavra in entrada:
    num = len(palavra)
    if num in saida:
        saida[num].append(palavra)
    else:
        saida[num] = [palavra]

print(saida)

# Desafio bonus! Colocar em ordem

entrada = "Hoje é um ótimo dia para programar"

caracteres_especiais = [",", ".", "!", "?", ":", ";", "'", "[", "]", "{", "}", "(", ")", '"']

entrada = entrada.lower()

for caracter in caracteres_especiais:
    entrada = entrada.replace(caracter,"")

saida = {}

entrada = entrada.split()

for palavra in entrada:
    num = len(palavra)
    if num in saida:
        saida[num].append(palavra)
    else:
        saida[num] = [palavra]

saida = dict(sorted(saida.items()))

print(saida)
