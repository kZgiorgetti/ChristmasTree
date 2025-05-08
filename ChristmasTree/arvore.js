const tamanho = 12; // Você pode mudar esse valor para árvores maiores

const construirArvore = (tamanho) => {
  const larguraBase = tamanho * 2 - 1;

  // Estrela no topo
  console.log(" ".repeat(tamanho - 1) + "*");

  // Corpo da árvore
  for (let i = 0; i < tamanho; i++) {
    const folhas = "=".repeat(2 * i + 1);
    const espacos = " ".repeat(tamanho - i - 1);
    console.log(espacos + folhas + espacos);
  }

  // Tronco
  const tronco = "_".repeat(tamanho - 1) + "|" + "_".repeat(tamanho - 1);
  console.log(tronco);

};

construirArvore(tamanho);
