produto_1 = input().split()
produto_2 = input().split()

pagar = (int(produto_1[1])*float(produto_1[2]))+(int(produto_2[1])*float(produto_2[2]))

print(f"VALOR A PAGAR: R$ {pagar:.2f}")