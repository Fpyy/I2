'''
Desafio de Programação: Gestor de Notas
Desenvolva um programa que permita o cadastro de diversos alunos e suas respectivas notas.
 O programa deve funcionar da seguinte forma:
Entrada de Dados: O programa deve solicitar o nome do aluno (ou a nota). Para encerrar 
a entrada de dados, o usuário deve digitar "fim".
Processamento Individual: Para cada aluno cadastrado, o programa deve solicitar as notas
 (ex: Nota 1 e Nota 2) e exibir imediatamente a média desse aluno.
Acúmulo de Dados: O programa deve manter o controle interno de:
Quantos alunos foram processados.
A soma das médias de todos os alunos para calcular a média global.
Encerramento: Ao digitar "fim", o programa deve exibir um relatório final contendo:
O total de alunos cadastrados.
A média geral da turma.
'''
total_alunos = 0
soma_medias = 0

while True:
    nome = input("Digite o nome do aluno (digite 'fim' para encerrar): ")
    
    if nome == "fim":
        break

    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))

    media = (nota1 + nota2) / 2
    print(f"Média de {nome}: {media:.2f}")

    total_alunos += 1
    soma_medias += media

print("--- RELATÓRIO FINAL ---")
print(f"Total de alunos: {total_alunos}")

if total_alunos > 0:
    media_geral = soma_medias / total_alunos
    print(f"Média geral da turma: {media_geral:.2f}")
else:
    print("Nenhum aluno foi cadastrado.")