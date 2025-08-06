nome = input()
salario_fixo = float(input())
comissao = float(input())*0.15

salario_com_bonus = salario_fixo + comissao

print(f"TOTAL = R$ {salario_com_bonus:.2f}")