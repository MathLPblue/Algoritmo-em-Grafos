# Algortimo de Prim 
O algortimo de prim é um algoritmo guloso (greedy) utilizado para encontrar a Árvore Geradora Mínima (AGM) de um grafo não orientado, ponderado e conexo.
Seu objetivo é conectar todos os vértices do grafo utilizando arestas cuja soma dos pessos seja a menor possível, sem formar ciclos.
**Como funciona?**
1. Escolha incial: Seleciona um vértice qualquer para iniciar.
2. Seleção da menor aresta: Procura a aresta de menor peso que conecta um vértice já visitado a outro não visitado. 
3. Inclusção do vértice: Adciiona a aresta e o novo vértice à árvore. 
4. Repetição: Continua selecionando as menores arestas disponíveis, sem formar ciclos 
5. Finalização: Termina  quando todos os vértices estão conectados 

