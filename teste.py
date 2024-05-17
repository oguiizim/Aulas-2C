import random

palavras = ["porco", "pedra", "biblioteca"]

palavra_secreta = random.choice(palavras)

palavraVazia = ["_"] * len(palavra_secreta)
erros = 0 
acertos = 0
letras_usadas = []

def mostrar_palavra(palavraVazia):
    print("Palavra: ", " ".join(palavraVazia))

while True:
    print("\n1 - Digitar uma letra\n2 - Chutar uma palavra")
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue
        
        letras_usadas.append(letra)
        
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavraVazia[i] = letra
            acertos += 1
            print("Você acertou uma letra!")
        else:
            erros += 1
            print("Você errou!")
        
        print("Você tem {} acertos e {} erros até o momento!".format(acertos, erros))
        mostrar_palavra(palavraVazia)
        
        if "_" not in palavraVazia:
            print("Parabéns! Você ganhou!")
            break
        
    elif opcao == 2:
        chute = input("Digite sua palavra: ").lower()
        
        if chute == palavra_secreta:
            print("Parabéns! Você acertou a palavra secreta!")
            break
        else:
            erros += 1
            print("Você errou! A palavra não é essa.")
            print("Você tem {} erros até o momento!".format(erros))
            
        if erros >= 6:
            print("Você perdeu! A palavra era '{}'.".format(palavra_secreta))
            break
    else:
        print("Opção inválida. Tente novamente.")
    
    if erros >= 6:
        print("Você perdeu! A palavra era '{}'.".format(palavra_secreta))
        break
