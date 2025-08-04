entrada = """
Aprender Python é muito divertido. 
Python é simples, poderoso e versátil. 
Com Python, você pode automatizar tarefas, analisar dados e até criar jogos!
"""

analise = entrada.lower()
caracteres_especiais = [",",".","!","?",":",";","'","[","]","{","}","(",")",'"']

contador = {}
palavras_unicas = 0

for caracter in caracteres_especiais:
    analise = analise.replace(caracter,"")

lista = analise.split()

total_palavras = len(lista)

for palavra in lista:
    if palavra not in contador:
        contador[palavra] = 1
    else:
        contador[palavra] += 1

contador = dict(sorted(contador.items(), key=lambda item: (-item[1], item[0])))

top3 = [palavra for palavra in list(contador)[:3]]

for quantidade in contador.values():
    if quantidade == 1:
        palavras_unicas += 1



print(total_palavras)
print(palavras_unicas)
print(top3)