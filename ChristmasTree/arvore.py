tamanho = 12    #Define o tamanho da árvore em altura

def construir_arvore(tamanho):  #Marca o inicio da função e usar 'tamanho' como propriedade
    largura_base = tamanho * 2 - 1  #Define o tamanho da base de acordo com a altura da arvore

    print(" " * (tamanho - 1) + "*")    #Imprime a estrela no ponto mais alto da árvore

    for i in range(tamanho):    #Cria um laço de repetição para fazer a copa da árvore 
        folhas = "=" * (2 * i + 1)  #Define quantas folhas vão ter na linha
        espacos = " " * (tamanho - i - 1)   #Define quantos espações vão ter na linha
        print(espacos + folhas - espacos)   #Imprime os espaços e as folhas

    tronco = " " * (tamanho - 1) + "|" + " " * (tamanho - 1)    #Imprime o tronco da árvore

construir_arvore(tamanho)   #Chama a função