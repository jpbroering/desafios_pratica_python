# Usando o replace()
entrada = "Hoje é um bom dia. Um dia para aproveitar o dia!"

substituir = "dia"
por = "momento"

saida = entrada.lower().replace(substituir.lower(),por)

print(saida)

# sem usar o replace()
entrada = "Hoje é um bom dia. Um dia para aproveitar o dia!"

entrada = entrada.lower()

substituir = "dia"
por = "momento"

saida = ""

saida = por.join(entrada.split(substituir))

print(saida)