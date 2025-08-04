entrada = "Programação é divertida"

vogais = ["a","ã","â","á","à","e","é","è","ê","i","í","ì","î","o","ó","ò","õ","ô","u","û","ú","ù"]

answ = 0

for vogal in vogais:
    answ += entrada.lower().count(vogal)

print(answ)

# resposta melhor

for letra in entrada:
    if letra in vogal:
        answ += 1

print(answ)