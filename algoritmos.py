import heapq
from typing import List, Tuple, Dict, Set
import sys

class Grafo:
    def __init__(self, num_vertices: int, direcionado: bool = False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.arestas = []
        self.adj_list = [[] for _ in range(num_vertices)]
        
    def adicionar_aresta(self, u: int, v: int, peso: int):
        # Add aresta ao grafo
        self.arestas.append((u, v, peso))
        self.adj_list[u].append((v, peso))
        
        if not self.direcionado:
            self.adj_list[v].append((u, peso))

def dijkstra(grafo: Grafo, origem: int) -> Tuple[List[int], List[int]]:
    """
    Algoritmo de Dijkstra para caminho mínimo de origem única
    
    Pseudocódigo:
    DIJKSTRA(G, w, s)
    1  INITIALIZE-SINGLE-SOURCE(G, s)
    2  S ← ∅
    3  Q ← V[G]
    4  while Q ≠ ∅
    5      do u ← EXTRACT-MIN(Q)
    6         S ← S ∪ {u}
    7         for each vertex v ∈ Adj[u]
    8             do RELAX(u, v, w)
    """
    INF = float('inf')
    
    # INITIALIZE-SINGLE-SOURCE(G, s)
    dist = [INF] * grafo.num_vertices
    anterior = [-1] * grafo.num_vertices
    dist[origem] = 0
    
    # Q ← V[G] (usando heap para eficiência)
    heap = [(0, origem)]
    visitados = set()
    
    # while Q diferente de vazio
    while heap:
        """Extract-min de Q e processamento do vértice"""
        dist_atual, u = heapq.heappop(heap)
        
        if u in visitados:
            continue
            
        visitados.add(u)
        
        # for each vertex v ∈ Adj[u]
        for v, peso in grafo.adj_list[u]:
            # RELAX(u, v, w)
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                anterior[v] = u
                heapq.heappush(heap, (dist[v], v))
    
    return dist, anterior

def bellman_ford(grafo: Grafo, origem: int) -> Tuple[List[int], List[int], bool]:
    """
    Algoritmo de Bellman-Ford para grafos com arestas negativas
    
    Pseudocódigo:
    BELLMAN-FORD(G, w, s)
    1  INITIALIZE-SINGLE-SOURCE(G, s)
    2  for i ← 1 to |V[G]| - 1
    3      do for each edge (u, v) ∈ E[G]
    4             do RELAX(u, v, w)
    5  for each edge (u, v) ∈ E[G]
    6      do if d[v] > d[u] + w(u, v)
    7             then return FALSE
    8  return TRUE
    """
    INF = float('inf')
    
    # INITIALIZE-SINGLE-SOURCE(G, s) - linha 1
    dist = [INF] * grafo.num_vertices
    anterior = [-1] * grafo.num_vertices
    dist[origem] = 0
    
    # for i ← 1 to |V[G]| - 1 - linha 2
    for i in range(grafo.num_vertices - 1):
        # for each edge (u, v) ∈ E[G] - linha 3
        for u, v, peso in grafo.arestas:
            # RELAX(u, v, w) - linha 4
            if dist[u] != INF and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                anterior[v] = u
    
    # Verificação de ciclo negativo - linhas 5-7
    # for each edge (u, v) ∈ E[G]
    for u, v, peso in grafo.arestas:
        # if d[v] > d[u] + w(u, v) then return FALSE
        if dist[u] != INF and dist[u] + peso < dist[v]:
            return dist, anterior, False  # Ciclo negativo detectado
    
    # return TRUE - linha 8
    return dist, anterior, True

def floyd_warshall(grafo: Grafo) -> List[List[int]]:
    """
    Algoritmo de Floyd-Warshall para todos os pares de vértices
    
    Pseudocódigo:
    FLOYD-WARSHALL(W)
    1  n ← rows[W]
    2  D⁽⁰⁾ ← W
    3  for k ← 1 to n
    4      do for i ← 1 to n
    5             do for j ← 1 to n
    6                    do d_ij⁽ᵏ⁾ ← min(d_ij⁽ᵏ⁻¹⁾, d_ik⁽ᵏ⁻¹⁾ + d_kj⁽ᵏ⁻¹⁾)
    7  return D⁽ⁿ⁾
    """
    INF = float('inf')
    n = grafo.num_vertices
    
    # Inicializar matriz de distâncias - linhas 1-2
    # D⁽⁰⁾ ← W
    dist = [[INF for _ in range(n)] for _ in range(n)]
    
    # Distância de um vértice para ele mesmo é 0
    for i in range(n):
        dist[i][i] = 0
    
    # Preencher com as arestas do grafo
    for u, v, peso in grafo.arestas:
        dist[u][v] = peso
        if not grafo.direcionado:
            dist[v][u] = peso
    
    # for k ← 1 to n - linha 3
    for k in range(n):
        # for i ← 1 to n - linha 4
        for i in range(n):
            # for j ← 1 to n - linha 5
            for j in range(n):
                # d_ij⁽ᵏ⁾ ← min(d_ij⁽ᵏ⁻¹⁾, d_ik⁽ᵏ⁻¹⁾ + d_kj⁽ᵏ⁻¹⁾) - linha 6
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # return D⁽ⁿ⁾ - linha 7
    return dist

def reconstruir_caminho(anterior: List[int], origem: int, destino: int) -> List[int]:
    """Reconstrói o caminho a partir do vetor de predecessores"""
    caminho = []
    atual = destino
    
    while atual != -1:
        caminho.append(atual)
        atual = anterior[atual]
    
    caminho.reverse()
    
    # Se o primeiro elemento não é a origem, não há caminho
    if caminho[0] != origem:
        return []
    
    return caminho