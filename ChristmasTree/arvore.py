# Define o tamanho da árvore
tamanho = 12  # Você pode mudar esse valor para árvores maiores

def construir_arvore(tamanho):
    largura_base = tamanho * 2 - 1

    # Estrela no topo
    print(" " * (tamanho - 1) + "*")

    # Corpo da árvore
    for i in range(tamanho):
        folhas = "=" * (2 * i + 1)
        espacos = " " * (tamanho - i - 1)
        print(espacos + folhas + espacos)

    # Tronco com sublinhados e barra vertical no centro
    tronco = "_" * (tamanho - 1) + "|" + "_" * (tamanho - 1)
    print(tronco)

# Chamada da função
construir_arvore(tamanho)
