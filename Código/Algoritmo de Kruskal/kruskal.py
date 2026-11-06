# ================
# ALGORITMO DE KURSKAL
# ================

def ler_inteiro(mensagem, minimo, maximo =None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue 

            if maximo is not None and valor > maximo: 
                print(f"Digite um valor menor ou igual a {maximo}")
                continue 
            return valor 

        except ValueError:
            print("Erro! Digite um número inteiro válido.")

def ler(peso):
    while True:
        try:
            peso = float(input("Peso da aresta: "))
            if not (0 <= peso < float("inf")):
                print("O peso deve ser finito e não negativo.")
                continue 
            return peso
        except ValueError:
            print("Erro! Digite um peso numérico válido.")

def encontrar(pai, vertice):
    if pai[vertice] != vertice: 
        pai[vertice] = encontrar(pai, pai[vertice])
    return pai[vertice] 

    def unir(pai, tamanho, u, v):
        raiz_u = encontrar(pai, u)
        raiz_v = encontrar(pai, v)
        if raiz_u == raiz_v: 
            return False 
        
        if tamanho [raiz_u] < tamanho[raiz_v]:
            raiz_u, raiz_v = raiz_v, raiz_u 
        
        pai[raiz_v] = raiz_u 
        tamanho[raiz_u] += tamanho[raiz_v]