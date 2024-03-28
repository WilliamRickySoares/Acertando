
palavra = str(input("Palavra: "))
dica = str(input("Dica: "))
t = (len(palavra))
letra_certa = letra_errada = tentativa = 0

while letra_certa < t:
    print(f"\nPalavra com {t} letras. \nDica: {dica}")
    if tentativa == 0:
        for i in range(0, t):
            print('___ ', end = '')

    letra = str(input("\nEscolha uma letra: "))
    tentativa += 1

    # Desenha as linhas das palavas
    pos = 0
    for a in range(0, t):
        if letra in palavra[pos]:
            print(f' {letra} ', end = '')
        else:
            print(f' ___ ', end = '')
        palavra.find(letra)
        letra_certa += 1
        pos += 1
