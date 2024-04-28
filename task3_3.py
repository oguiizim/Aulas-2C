name = str(input("Digite seu nome: "))
while len(name) <= 3:
    name = str(input("Nome curto demais.\nDigite seu nome: "))

idade = int(input("Digite sua idade: "))
while idade < 0 or  idade > 150:
    print("Idade inválida.")
    idade = int(input("Digite uma idade entre 0 e 150: "))

salario = float(input("Digite seu salario mensal: "))
while salario < 0:
    print("Salario inválido.")
    salario = float(input("Digite um salario maior que 0"))

sexo = str(input("Digite a inicial do seu sexo: "))
sexo = sexo.lower()
while sexo!="f" and sexo!="m":
    sexo = str(input("Sexo invalido.\nDigite a inicial do seu sexo (F ou M): "))

estadoCivil = str(input("Digite a inicial do seu estado civil: "))
estadoCivil = estadoCivil.lower()
while (estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d"):
    estadoCivil = str(input("Estado Civil invalido.\nDigite a inicial do seu estado civil: "))