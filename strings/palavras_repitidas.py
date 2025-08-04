entrada = "Hoje é um bom dia, um dia claro e bom!"

caracteres_especiais = [",",".","!","?",":",";","'","[","]","{","}","(",")",'"']

entrada = entrada.lower()

for caracter in caracteres_especiais:
    entrada = entrada.replace(caracter,"")

entrada = entrada.split()

repitidos = []

for palavra in entrada:
    if entrada.count(palavra) > 1 and palavra not in repitidos:
        repitidos.append(palavra)

print(repitidos)