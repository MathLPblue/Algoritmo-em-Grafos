# Algoritmo de Bellman-Ford 
# Grafo orientado com validação

def bellman_ford(vertices,arestas,inicio):
    distancias = {v:float('inf') for v in vertices}
    distancias[inicio] = 0 

    # Relaxamento da arestas
    for i in range (len(vertices) - 1):
        alterou = False 
        print(f"\nITERAÇÃO {i + 1}")

        for origem, destino, peso in arestas: 
            if distancias[origem] != float('inf'):
                nova = distancias[origem] + peso
                if nova < distancias[destino]:
                    distancias[destino] = nova
                    alterou = True 

        print("distâncias: ", distancias)
        if not alterou: 
            break 
    # Verificação de ciclo negativo 
    for origem, destino, peso in arestas: 
        if (distancias[origem] != float('inf') and 
            distancias[origem] + peso <
            distancias[destino]):
            print("\nERRO: Existe ciclo negativo!")
            return None 
    return distancias
# =================
# VALIDAÇÃO DE NÚMEROS
# =================

def ler_inteiro(mensagem, minimo=None):
    while True:
        try: 
            numero = int(input(mensagem))
            if minimo is not None and numero < minimo:
                print(f"Digite um número inteiro.")
                continue
            return numero 
        except ValueError:
            print("Erro! Digite um número inteiro.")

# =================
# ENTRADA DE VÉRTICES 
# =================

quantidade = ler_inteiro(
    "Quantidade de vértices: ", 1
)
vertices = []
for i in range(quantidade):
    vertices.append(chr(65 + i))
print("Vértices: ", vertices)

# =================
# ENTRADA DAS ARESTAS
# =================
arestas = []
arestas_cadastradas = set()
max_arestas = quantidade * (quantidade - 1)
qtd_arestas = ler_inteiro(
    f"Quantidade de arestas (0 a {max_arestas}): ", 0
)

while qtd_arestas > max_arestas:
    print("Quantidade de arestas inválida!")
    qtd_arestas = ler_inteiro(
        "Informe novamente: ", 0
    )

while len(arestas) < qtd_arestas:
  print(f"\nAresta {len(arestas) + 1}")
  origem = input("Origem: ").upper().strip()
  destino = input("Destino: ").upper().strip()

  # Validar vértices
  if origem not in vertices or destino not in vertices:
    print("Erro! Vértice inexistente.")
    continue

  # Impedir laços
  if origem == destino:
    print("Erro! Origem e destino iguais.")
    continue

  # Impedir arestas repetidas
  if (origem, destino) in arestas_cadastradas:
    print("Erro! Esta aresta já foi cadastrada.")
    continue

  peso = ler_inteiro("Peso da aresta: ")
  arestas.append((origem, destino, peso))
  arestas_cadastradas.add((origem, destino))
  print("Aresta cadastrada com sucesso!")

# =================
# EXIBIR GRAFO 
# =================

print("\nARESTAS CADASTRADAS")
for origem, destino, peso in arestas:
    print(f"{origem} -> {destino} | Peso:{peso}")

# =================
# VÉRTICE INICIAL 
# =================
while True: 
    inicio = input("\nVértice inicial: ").upper().strip()
    if inicio in vertices:
        break 
    print("Erro! Vértice inexistente.")

# =================
# EXECUÇÃO 
# =================
resultado = bellman_ford(vertices, arestas, inicio)
if resultado is not None:
    print("\nRESULTADO FINAL")
    for vertice, distancia in resultado.items():
        if distancia == float('inf'):
            print(f"{vertice}: inalcançável")
        else:
            print(f"{vertice}: {distancia}")