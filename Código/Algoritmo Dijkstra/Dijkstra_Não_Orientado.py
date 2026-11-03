import heapq 
# ===============
# FUNÇÃO DIJSKTRA
# ===============
def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0 
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso 

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))
    return distancias

# ===============
# ENTRADA DO GRAFO
# ===============
grafo = {}
qtd_vertices = int(input("quantidade de vertices: "))

for i in range(qtd_vertices):
    vertice = input(f"nome do vértice {i+1}: ")
    grafo[vertice] = []

qtd_arestas = int(input("quantidade de arestas: "))

for i in range(qtd_arestas):
    origem = input("origem: ")
    destino = input("destino: ")

    peso = int(input("Peso da aresta"))

    grafo[origem].append((destino, peso))
    grafo[destino].append((origem, peso))

# ===============
# EXECUÇÃO DO GRAFO
# ===============
inicio = input("vertice inicial: ")
resultado = dijkstra(grafo, inicio)
print("\nMenores distancias")

for vertice, distancia in resultado.items():
    print(f"{inicio} -> {vertice} = {distancia}")


