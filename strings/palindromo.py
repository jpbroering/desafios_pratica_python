entradas = ["arara",
"Roma me tem amor",
"Python"]

for entrada in entradas:
    memoria = entrada.lower().replace(" ","")

    answ = True if memoria == memoria[::-1] else False
    
    print(answ)
