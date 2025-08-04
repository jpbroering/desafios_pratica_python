entrada = "Aprender Python é muito divertido"

entrada = entrada.split()

entrada.sort(key=lambda x: len(x),reverse=True)

answ = entrada[0]

print(answ)