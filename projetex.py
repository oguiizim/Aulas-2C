alunos = []

num_alunos = int(input("Quantos alunos deseja registrar? "))

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    data_nascimento = input(f"Digite a data de nascimento do aluno {i+1}: ")
    
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota do {j+1}º bimestre para o aluno {nome}: "))
        notas.append(nota)
    
    alunos.append([nome, data_nascimento, notas])

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

for aluno in alunos:
    nome = aluno[0]
    data_nascimento = aluno[1]
    notas = aluno[2]
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)
    
    print(f'Aluno: {nome}')
    print(f'Data de nascimento: {data_nascimento}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')
    print()
