# palavra1 = ["porco"]
# teste = len(palavra1)
# teste2 = teste

# for i in range(0,teste2):
#     letter = palavra1[i]
#     print(letter)

palavra = "porco"
palavraVazia = []

while True:
    verify = int(input("Digite o num:"))
    if(verify == 1):
        letter = str(input("Digite uma letra: "))
        palavraVazia.append(letter)

        print(palavraVazia)
        if(letter in palavra):
            print("try")

        print(len(letter in palavra))
    else:
        break