nomes=["jully", "mika", "polly", "agatha", "gabriel"]

nome=input("Digite o nome que voce quer encontrar: ")
for y in range(len(nomes)):
    if nome == nomes[y]:
        print(f"Achei {nome} da pessoa na posição {y}")
    else:
        print("Tá não")



