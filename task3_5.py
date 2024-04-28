populaçãoA = float(input("Informe a população da cidade A: "))
populaçãoB = float(input("Informe a população da cidade B: "))
ano = 0
taxa_crescimentoA = float(input("Informe a taxa de crescimento da população da cidade A: "))
taxa_crescimentoB = float(input("Informe a taxa de crescimento da população da cidade B: "))
while populaçãoA < populaçãoB:
	populaçãoA += round((populaçãoA * taxa_crescimentoA) / 100)
	populaçãoB += round((populaçãoB * taxa_crescimentoB) / 100)
	ano = ano + 1

print("Levará",ano,"anos para população da cidade A ser maior que a cidade B")
print("População B -->",populaçãoB,"Habitantes")
print("População A -->", populaçãoA,"Habitantes")