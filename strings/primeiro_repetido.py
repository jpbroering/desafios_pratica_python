entrada = "Abacaxi"
entrada = entrada.lower().replace(" ","")

repetidos = []

for letra in entrada:
    if letra in repetidos:
        print(letra)
        break
    else:
        repetidos.append(letra)