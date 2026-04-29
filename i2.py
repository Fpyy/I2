totalalunos = 0
somamedias = 0

while True:
    nome = input("Qual o nome do aluno: (fim para parar) ")
    
    if nome == "fim":
        break

    nota1 = float(input("Digite uma nota: "))
    nota2 = float(input("Digite a outra nota "))

    media = (nota1 + nota2) / 2
    print(f"Média de {nome}: {media:.2f}")

    totalalunos += 1
    somamedias += media

print("- RELATÓRIO FINAL -")
print(f"Total de alunos: {totalalunos}")

if totalalunos > 0:
    media = somamedias / totalalunos
    print(f"Média da turma: {media:.2f}")
else:
    print("Sem alunos cadastrados")