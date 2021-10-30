total_de_tentativas = 3
rodada = 1
numero_da_sorte = 12

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número:")
    chute = int(chute_str)

    acertou = chute == numero_da_sorte
    maior   = chute >  numero_da_sorte
    menor   = chute <  numero_da_sorte

    if(acertou):
        print("Acertou meu Jovem.")
        break
    elif (maior):
        print("Errou!!!, o valor é menor")
    elif (menor):
        print("Errou!!!, o valor é maior")
    else:
        print("Número invalido.")

    rodada = rodada + 1


print("O Jogo acabou!")