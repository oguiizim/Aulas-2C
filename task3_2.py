user = str(input("Digite seu nome de usuario: "))
senha = str(input("Digite sua senha: "))

user = user.lower()
senha = senha.lower()

while user==senha:
    print("Sua senha não pode ser igual ao usuario")
    senha = str(input("Digite sua senha: "))

else:
    print("Cadastro concluido!")