from math import inf

numeros = []

while True:
    valor = input(
        "Digite um número ou 'r' para parar e exibir os resultados: "
    )
    if valor.upper() == "r":
        break
    numeros.append(float(valor))

menor_numero = inf
for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero
print(f"O menor número é {menor_numero}")

maior_numero = -inf
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número é {maior_numero}")

soma = 0
for numero in numeros:
    soma += numero
print(f"A soma dos números é {soma}")