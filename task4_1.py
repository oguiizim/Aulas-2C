par = 0
impar = 0
for _ in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        par += 1
    else:
        impar += 1
print("Pares: {}\nÍmpares: {}".format(par, impar))