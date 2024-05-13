while True:

    print("\n1 - Sim\n2 - Não")
    cont = int(input("\nVocê deseja continuar: "))

    if(cont == 1):
        num = int(input("Digite um número: "))
        for i in range(1, 11):
            calculate = num * i
            print("{} * {} = {}".format(num, i, calculate))
    elif(cont == 2):
        break
    else:
        print("Opção invalida. Digite novamente.")
