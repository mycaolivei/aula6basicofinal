valores=[]
valores_pares=[]
soma=0
cont=0
for i in range(10):
    valores.append(int(input("Digite um valor inteiro: ")))
    if valores[i] %2==0:
        valores_pares.append(valores[i])
print(f"Os números pares são {valores_pares}")
maior_valor=valores[0]
menor_valor=valores[0]

for u in range(len(valores)):
    if valores[u] < menor_valor:
     menor_valor=valores[u]
print(f"O menor valor é {menor_valor}")

for x in range(len(valores)):
    if valores[x] > maior_valor:
        maior_valor=valores[x]
print(f"O maior valor é {maior_valor}")

for s in range(len(valores)):
    soma += valores[s]
print(f"A soma dos valores é {soma}")
media= soma / len(valores)
print(f"A media dos valores é {media}")
for z in range(len(valores)):
    if valores[z] > media:
        cont+=1
print(f"Encontrei {cont} valores maiores que a media")