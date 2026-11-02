import heapq

# Leitura e validação de números inteiros
def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Erro! digite um número inteiro válido")


# Validação e leitura dos pesos
def ler_peso():
    while True:
        try:
            peso = float(input("Peso da aresta: "))
            if not (0 <= peso < float("inf")):
                print("O peso deve ser finito e não negativo")
                continue
            return peso
        except ValueError:
            print("Erro! Digite um peso numérico válido")


# Algoritmo de Prim
def prim(grafo, inicio=0):
    visitados = set()
    fila = [(0, inicio, -1)]
    arvore = []
    custo_total = 0

    while fila:
        peso, atual, origem = heapq.heappop(fila)

        if atual in visitados:
            continue

        visitados.add(atual)

        if origem != -1:
            arvore.append((origem, atual, peso))
            custo_total += peso

        for vizinho, peso_aresta in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(
                    fila,
                    (peso_aresta, vizinho, atual)
                )

    if len(visitados) != len(grafo):
        return None, None

    return arvore, custo_total


# Programa principal
print("=== ALGORITMO DE PRIM ===")
print("Grafo Não Orientado")

n = ler_inteiro("Quantidade de vértices: ", 1)
max_arestas = n * (n - 1) // 2

m = ler_inteiro(
    f"Quantidade de arestas (0 a {max_arestas}): ",
    0,
    max_arestas
)

grafo = [[] for _ in range(n)]
arestas_cadastradas = set()


# Cadastro das arestas
for i in range(m):
    print(f"\nAresta {i + 1}")

    while True:
        u = ler_inteiro(
            f"Vértice de origem (0 a {n - 1}): ",
            0, n - 1
        )

        v = ler_inteiro(
            f"Vértice de destino (0 a {n - 1}): ",
            0, n - 1
        )

        if u == v:
            print("Erro! Não são permitidos laços.")
            continue

        # Normaliza a aresta para evitar repetição
        aresta = tuple(sorted((u, v)))

        if aresta in arestas_cadastradas:
            print("Erro! Essa aresta já foi cadastrada.")
            continue

        break

    peso = ler_peso()
    arestas_cadastradas.add(aresta)

    # Grafo não orientado: duas direções
    grafo[u].append((v, peso))
    grafo[v].append((u, peso))


# Exibir o grafo
print("\n=== GRAFO CADASTRADO ===")

for vertice in range(n):
    print(f" Vértice {vertice}: {grafo[vertice]}")


# Executar Prim
arvore, custo = prim(grafo)

print("\n=== ÁRVORE GERADORA MÍNIMA ===")

if arvore is None:
    print("O grafo não é conexo.")
    print("Não existe árvore geradora mínima.")
else:
    for u, v, peso in arvore:
        print(f"{u} -- {v} | Peso: {peso:g}")

    print(f"\nPeso total da AGM: {custo:g}")
    print(f"Quantidade de arestas da AGM: {len(arvore)}")