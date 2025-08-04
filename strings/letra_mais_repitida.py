entrada = "Abacaxi"
entrada = entrada.lower().replace(" ","")
ordem = set(entrada)

print(ordem)
mais_repitida = [None,0]
for letra in ordem:
    if entrada.count(letra) > mais_repitida[1]:
        mais_repitida = [letra,entrada.count(letra)]

print(mais_repitida)