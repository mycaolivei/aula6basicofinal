lista_numeros=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
cont=0
for i in range(len(lista_numeros)):
    lista_numeros[i]=int(input("Digite um número: "))
numero=int(input("Digite um número para encontrar: "))
for i in range(len(lista_numeros)):
    if numero == lista_numeros[i]:
        cont+=1
print(f"Encontrei {numero}, {cont} vezes na lista")

