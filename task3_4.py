populaçãoA = 80000
populaçãoB = 200000
ano = 0
while populaçãoA < populaçãoB:
	populaçãoA += round((populaçãoA*3.0) / 100)
	populaçãoB += round((populaçãoB*1.5) / 100)
	ano = ano + 1

print("Levará", ano ,"anos para população da cidade A ser maior que a cidade B")
print("PopulaçãoB-->", populaçãoB ,"Habitantes")
print("PopulaçãoA-->", populaçãoA ,"Habitantes")