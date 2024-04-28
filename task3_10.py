
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
while num2 < num1:
	num1 = int(input("Digite um numero: "))
	num2 = int(input("Digite outro numero: "))
else:
	for i in range(num1,num2,1):
		print(i)
