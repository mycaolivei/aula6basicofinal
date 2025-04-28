soma=0
count=0
notas=[0, 0, 0, 0, 0]
for i in range (len(notas)):
    notas[i]=float(input("Digite uma nota de um aluno: "))

for x in range(len(notas)):
    soma= soma + notas[x]

media= soma / len(notas)
print(media)
for i in range(len(notas)):
    if notas[i] >= 7:
        count= count + 1
print(f"Encontrei {count} alunos acima da media.")

