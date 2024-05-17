alunos = []

num_alunos = int(input("Quantos alunos deseja registrar? "))

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    data_nascimento = input(f"Digite a data de nascimento do aluno {i+1}: ")
    
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota do {j+1}º bimestre para o aluno {nome} (0-10): "))
        notas.append(nota)
    
    alunos.append([nome, data_nascimento, notas])

def calcularMedia(notas):
    return sum(notas) / len(notas)

def verificarAprovacao(media):
    if media <= 1:
        return "Reprovado"
    elif media <= 6:
        return "Recuperação"
    else: 
        return "Aprovado"
    
for aluno in alunos:
    nome = aluno[0]
    data_nascimento = aluno[1]
    notas = aluno[2]
    media = calcularMedia(notas)
    situacao = verificarAprovacao(media)
    
    print(f'Aluno: {nome}')
    print(f'Data de nascimento: {data_nascimento}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')
    # print()
