print("********************************")
print("Bem Vindo ao Jogo de Adivinhação")
print("********************************")


numero_da_sorte = 42
chute_str = input("Informe o chute:")
chute = int(chute_str)

acertou = chute == numero_da_sorte
maior   = chute >  numero_da_sorte
menor   = chute <  numero_da_sorte

if (acertou):
    print("Parabens você acertou o numero é :", numero_da_sorte)
elif (maior):
    print("Errou, numero maior que o numero da sorte")
elif (menor):
    print("Errou, numero menor que o numero da sorte")

print("Tchauuuuu até mais!!!!!!")