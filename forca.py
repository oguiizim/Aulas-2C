word1 = "porco"
word2 = "pedra"
word3 = "biblioteca"


palavraVazia = []
errors = 0 
rights = 0
while True:
    verify = int(input("Digite o num:"))
    if(verify == 1):
        print("\n1 - Digitar uma letra\n2 - Chutar uma palavra")
        verify2 = int(input("Digite sua opção: "))
        if(verify == 1):
            letter = str(input("Digite uma letra: "))
            palavraVazia.append(letter)
            # print(palavraVazia)
            if(letter in word1):
                rights += 1
                print("Você tem {} acertos".format(rights))
            else:
                errors += 1
                print("Você tem {} erros até o momento!".format(errors))
    else:
        break