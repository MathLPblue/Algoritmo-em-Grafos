# Algortimo de Dijkstra 
- Usado em grafos ponderados -> **Aresta com valor** 
- Usado para determinar menor custo entre o vértice de origem e os demais vértices -> **Custo pode ser: Distância, tempo, consumo, preço, latência** 

**Não é aplicado em aresta negativa** 

## Como funciona?

1. Inicializa a distância de origem D

2. Inicializa os demais vértices com infinito (∞)

3. Marca todos os vértices não visitados

4. Escolhe o vértice visitado com a menor distância conhecida 

5. Calcula o vizinho alcançavél da seguinte forma: **distância atual + peso aresta** 

6. Se o novo valor for menor que a distância registrada para o vizinho, atualize sua distância e seu predecessor 

7. Marca o vértice escolhido como processado 

8. Repete até o processar todos os vértices necessários ou até tornar o destino procurado 

### Formula do Relaxamento

*Se d[u] + peso(u,v) < d[v] então d[v]:d[u] + peso(u,v)*


