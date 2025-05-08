tamanho = 12    #Define o tamanho da árvore

def construir_arvore(tamanho):  #Marca o inicio da função e usar tamanho como propriedade
    largura_base = tamanho * 2 - 1

    print(" " * (tamanho - 1) + "*")

    for i in range(tamanho):
        folhas = "=" * (2 * i + 1)
        espacos = " " * (tamanho - i - 1)
        print(espacos + folhas - espacos)

    tronco = " " * (tamanho - 1) + "|" + " " * (tamanho - 1)

construir_arvore(tamanho)