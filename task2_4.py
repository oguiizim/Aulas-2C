preco_hora = int(input("Quanto você ganha por hora: "))
horas_mes = int(input("Quantas horas por mês você trabalha: "))

def salario(preco_hora, horas_mes):
    salario = preco_hora * horas_mes
    return salario

salario = salario(preco_hora, horas_mes)

imposto_de_renda = salario * (11 / 100)
desconto_IR = salario - (salario - imposto_de_renda)

inss = salario * (8 / 100)
desconto_IN = salario - (salario - inss)

sindicato = salario * (5 / 100)
desconto_SN = salario - (salario - sindicato)

salario_liquido = salario - (imposto_de_renda + inss + sindicato)

print("Salario Bruto: R${:.2f}".format(salario))
print("Imposto de Renda (11%): R${:.2f}".format(desconto_IR))
print("INSS (8%): R${:.2f}".format(desconto_IN))
print("Sindicato (5%): R${:.2f}".format(desconto_SN))
print("Salario Liquido: R${:.2f}".format(salario_liquido))