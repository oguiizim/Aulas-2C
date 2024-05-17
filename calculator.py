def sum(num, num2):
    print(num + num2)

def minus(num, num2):
    print(num - num2)

def multiply(num, num2):
    print(num * num2) 

def divide(num, num2):
    if(num2 == 0):
        print("Error... Impossible divide per zero!")
    else:
        print(num / num2)

while True:
    print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair")
    verify = int(input("\nDigite sua opção: "))
    if(verify == 0):
        break
    else:
        num = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        if(verify == 1):
            print("\n")
            sum(num, num2)
        elif(verify == 2):
            print("\n")
            minus(num, num2)
        elif(verify == 3):
            print("\n")
            multiply(num, num2)
        elif(verify == 4):
            print("\n")
            divide(num, num2)