# Comparação dos principais algoritmos de grafos

**Dijkstra:** Menor caminho origem -> Peso não negativo -> Rastreamente e GPS por exemplo 

**Bellman-Ford:** Menor caminho desde uma origem -> Admite pesos negativos e ciclos negativos -> Analise de custos por exemplo 

**Floyd-Warshal:** Menores caminhos entre todos os pares -> Admite pesos negativos sem ciclos negativos -> Matriz de distâncias 

**Prim:** Árvore geradora mínima -> expande a árvore por menor aresta possível -> Cabeamento por exemplo 

**Kruskal:** Árvore geradora mínima -> seleciona arestas crescentes sem ciclos -> Infraestrutura por exemplo

**BFS:** Busca por nível -> Fila -> menor número de arestas em grafo não ponderado -> Redes sociais por exemplo

**DFS:** Exploração em profundidade -> pilha ou recurssão -> Detecção de ciclos por exemplo


| Algoritmo       | Dirigido | Não-Dirigido | Peso Negativo |
|-----------------|----------|--------------|---------------|
| `Dijkstra`      | Sim      | Sim          | Não           |
| `Bellman-Ford`  | Sim      | Sim          | Sim           |
| `Floyd Warshal` | Sim      | Sim          | Sim           |
| `Prim`          | Não      | Sim          | Sim           |
| `Kruskal`       | Não      | Sim          | Sim           |
| `BFS`           | Sim      | Sim          | Ignora Peso   |
| `DFS`           | Sim      | Sim          | Ignora Peso   |


*Observações* 
O algoritmo de dijsktra busca os menores caminhos desde um vértice de origem sem usar arestas negativas. 

O algoritmo de Bellman Ford também busca menores caminhos, porém considera pesos engativos e  ciclos no grafo. 

O algoritmo de Prim constrói árvores geradores minimas, expandido uma arvore a partir de um vértice

O algoritmo de Krukal constrói uma árvore geradora minima, considerando sempre arestas com menor peso

**Concorrentes:***
- Bellman Ford e Dijsktra
- Prim e Kruskal 
- BFS e DFS


### Árvore geradora mínima 
É uma técnica da estrutura de algoritmo em grafo que permite conectar todos os vértices dos grafos utilizando arestas cujo a soma dos valores é a menor possível. 