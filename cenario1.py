"""
Cenário 1: Determinando a estação central

Algoritmo utilizado: Floyd-Warshall
Precisamos calcular as distâncias de todos os vértices para todos os outros
para determinar qual vértice minimiza a soma das distâncias para todos os demais.
"""

from algoritmos import floyd_warshall
from utils import ler_grafo_arquivo, imprimir_matriz, imprimir_vetor

def encontrar_estacao_central(arquivo_grafo: str):
    """
    Encontra a estação central de um grafo de metrô
    """
    print("=== Cenário 1: Determinando a estação central ===")
    print(f"Lendo grafo do arquivo: {arquivo_grafo}")
    
    # Ler o grafo (não-direcionado)
    grafo = ler_grafo_arquivo(arquivo_grafo, direcionado=False)
    print(f"Grafo carregado: {grafo.num_vertices} vértices")
    
    # Aplicar Floyd-Warshall para obter todas as distâncias
    print("\nAplicando algoritmo Floyd-Warshall...")
    matriz_distancias = floyd_warshall(grafo)
    
    # Imprimir matriz de distâncias
    imprimir_matriz(matriz_distancias, "Matriz de Distâncias (Floyd-Warshall)")
    
    # Calcular somas das distâncias para cada vértice
    somas_distancias = []
    for i in range(grafo.num_vertices):
        soma = sum(matriz_distancias[i])
        somas_distancias.append(soma)
    
    # Encontrar a estação central (menor soma)
    estacao_central = somas_distancias.index(min(somas_distancias))
    
    # Distâncias da estação central para todos os outros vértices
    distancias_central = matriz_distancias[estacao_central]
    
    # Encontrar o vértice mais distante da estação central
    max_dist = max(dist for dist in distancias_central if dist != float('inf'))
    vertice_mais_distante = distancias_central.index(max_dist)
    
    print(f"Estação central escolhida: Vértice {estacao_central + 1}")  # +1 para numeração original
    print(f"Soma das distâncias da estação central: {somas_distancias[estacao_central]}")
    
    print(f"\nDistâncias da estação central (vértice {estacao_central + 1}) para todos os outros:")
    for i, dist in enumerate(distancias_central):
        if i != estacao_central:
            print(f"  Para vértice {i + 1}: {dist}")
    
    print(f"\nVértice mais distante da estação central:")
    print(f"  Vértice {vertice_mais_distante + 1} com distância {max_dist}")
    
    print(f"\nMatriz completa de distâncias entre todos os vértices:")
    print("(Linha i, Coluna j = distância do vértice i+1 para o vértice j+1)")
    imprimir_matriz(matriz_distancias, "Matriz Completa")
    
    return estacao_central, distancias_central, vertice_mais_distante, matriz_distancias

if __name__ == "__main__":
    encontrar_estacao_central("graph1.txt")