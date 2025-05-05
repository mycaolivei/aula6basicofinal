nomes=["mika","jully", "agatha", "polly", "davila"]
senha=["123", "456", "765", "987", "099"]

senhas = input("Digite a sua senha: ")
for i in range(len(nomes)):
    if senhas == senha[i]:
        print(f"Login efetuado com sucesso {nomes[i]}.")









