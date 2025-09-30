"""
Cenário 2: Otimizando caminho com regeneração

Algoritmo utilizado: Bellman-Ford  
O grafo possui arestas com pesos negativos (regeneração de energia),
o que torna impossível o uso do algoritmo de Dijkstra. Bellman-Ford é capaz
de lidar com pesos negativos e detectar ciclos negativos.
"""

from algoritmos import bellman_ford, reconstruir_caminho
from utils import ler_grafo_arquivo

def otimizar_caminho_carro(arquivo_grafo: str, origem: int = 0, destino: int = 6):
    """
    Encontra o caminho de menor custo energético para um carro elétrico
    """
    print("=== Cenário 2: Otimizando caminho com regeneração ===")
    print(f"Lendo grafo do arquivo: {arquivo_grafo}")
    
    # Ler o grafo (direcionado, pois a regeneração não é simétrica)
    grafo = ler_grafo_arquivo(arquivo_grafo, direcionado=True)
    print(f"Grafo carregado: {grafo.num_vertices} vértices (direcionado)")
    
    # Verificar se origem e destino são válidos
    if origem >= grafo.num_vertices or destino >= grafo.num_vertices:
        print(f"Erro: Vértices de origem ({origem}) ou destino ({destino}) inválidos")
        return
    
    print(f"Calculando caminho de menor custo do vértice {origem} ao vértice {destino}")
    
    # Aplicar Bellman-Ford
    print("\nAplicando algoritmo Bellman-Ford...")
    distancias, anterior, sem_ciclo_negativo = bellman_ford(grafo, origem)
    
    if not sem_ciclo_negativo:
        print("Ciclo negativo detectado no grafo!") # Isso significa que existe um ciclo onde se ganha energia infinita.
        return
    
    # Verificar se há caminho para o destino
    if distancias[destino] == float('inf'):
        print(f"Não há caminho do vértice")
        return
    
    # Reconstruir o caminho e calcular custo total

    caminho = reconstruir_caminho(anterior, origem, destino)
    custo_total = distancias[destino]
    
    # Resultados
    print(f"Caminho mínimo do vértice {origem} ao vértice {destino}:")
    print(" -> ".join(str(v) for v in caminho))
    
    print(f"\nCusto total do caminho: {custo_total} Wh")
    if custo_total < 0:
        print("(Valor negativo indica que o carro chega com mais energia do que saiu!)")
    elif custo_total > 0:
        print("(Energia líquida consumida)")
    else:
        print("(Energia balanceada)")
    
    # Mostrar custos de cada trecho
    print(f"\nDetalhamento dos custos por trecho:")
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        # Encontrar o custo da aresta
        for aresta_u, aresta_v, peso in grafo.arestas:
            if aresta_u == u and aresta_v == v:
                print(f"  {u} -> {v}: {peso} Wh")
                break
    
    # Mostrar todas as distâncias calculadas
    print(f"\nDistâncias mínimas do vértice {origem} para todos os outros:")
    for i, dist in enumerate(distancias):
        if dist != float('inf'):
            print(f"  Para vértice {i}: {dist} Wh")
        else:
            print(f"  Para vértice {i}: Inalcançável")
    
    return caminho, custo_total

if __name__ == "__main__":
    otimizar_caminho_carro("graph2.txt", 0, 6)