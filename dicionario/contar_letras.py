entrada = "Casa Grande!"

caracteres_especiais = [",", ".", "!", "?", ":", ";", "'", "[", "]", "{", "}", "(", ")", '"'," "]

entrada = entrada.lower()

for caracter in caracteres_especiais:
    entrada = entrada.replace(caracter,"")

repitidos = {}

for letra in entrada:
    if letra in repitidos:
        repitidos[letra] += 1
    else:
        repitidos[letra] = 1

print(repitidos)