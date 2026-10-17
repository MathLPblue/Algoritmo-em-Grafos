#Grafo Orientado 
#Matriz de Adjacência e Lista de Adjacência

n = int(input("Digite o número de vértices"))

#Criar matriz de adjacência
matriz = []

for i in range(n):
    matriz.append([0] * n)

#Criar lista de adjacência
lista = []
for i in range(n):
    lista.append([])

#Conjunto de arestas cadastradas 
arestas_cadastradas = set()

quantidade = int(input("Digite o número de arestas"))
contador = 0

while contador < quantidade:
    print("\nAresta", contador + 1)
    
    origem = int(input("Vértice de origem: "))
    destino = int(input("Vértice de destino: "))

    #Validar vértice fora do intervalo
    if origem < 1 or origem > n or destino < 1 or destino > n:
        print("Erro: Vértice inválido")
        print("Digite vértices entre 1 e", n)
        continue

    #Evitar ligação do vértice com ele mesmo
    if origem == destino:
        print("Erro: não é permitido ligar um vértice a ele mesmo")
        continue 

    #No Grafo Orientado, a ordem importa
    aresta = (origem, destino)

    #Verificar se aresta já existe
    if aresta in arestas_cadastradas:
        print("Erro: aresta já cadastrada")
        continue
    
    #Guardar aresta
    arestas_cadastradas.add(aresta)

    #Preencher matriz
    matriz[origem - 1][destino - 1] = 1

    #Preencher lista 
    lista[origem - 1].append(destino)

    contador += 1 

# Mostrar matriz adjacência 
print("\nMATRIZ DE ADJACÊNCIA")
for linha in matriz:
    print(linha)

# Mostrar Lista de Adjacência
print("\nLISTA DE ADJACÊNCIA")    
for i in range(n):
    print(i + 1, "->", lista[i])