term = int(input("Digite o numero de termos da série de Fibonacci: "))
num = 1
num_anterior = 0
for _ in range(term):
    print(num)
    aux = num
    num += num_anterior
    num_anterior = aux