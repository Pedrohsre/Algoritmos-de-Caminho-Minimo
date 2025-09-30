"""
Funções utilitárias para leitura de arquivos e formatação de saída
"""

from typing import List, Tuple
from algoritmos import Grafo

def ler_grafo_arquivo(nome_arquivo: str, direcionado: bool = False) -> Grafo:
    """
    Lê um grafo de um arquivo de texto
    Formato: primeira linha contém num_vertices e num_arestas
    Linhas seguintes contêm: vertice_origem vertice_destino peso
    """
    with open(nome_arquivo, 'r') as arquivo:
        linha = arquivo.readline().strip().split()
        num_vertices = int(linha[0])
        num_arestas = int(linha[1])
        
        grafo = Grafo(num_vertices, direcionado)
        
        for _ in range(num_arestas):
            linha = arquivo.readline().strip().split()
            u = int(linha[0])
            v = int(linha[1]) 
            peso = int(linha[2])
            
            # Para graph1.txt, ajustar para indexação base 0
            # Para graph2.txt, já está em base 0
            if nome_arquivo == "graph1.txt" and u > 0:
                u -= 1
                v -= 1
                
            grafo.adicionar_aresta(u, v, peso)
    
    return grafo

def ler_grid_arquivo(nome_arquivo: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    """
    Lê um grid de um arquivo
    Retorna: (grid, posição_inicial, posição_objetivo)
    """
    with open(nome_arquivo, 'r') as arquivo:
        linha = arquivo.readline().strip().split()
        linhas = int(linha[0])
        colunas = int(linha[1])
        
        grid = []
        pos_inicial = None
        pos_objetivo = None
        
        for i in range(linhas):
            linha_grid = list(arquivo.readline().strip())
            grid.append(linha_grid)
            
            for j in range(colunas):
                if linha_grid[j] == 'S':
                    pos_inicial = (i, j)
                elif linha_grid[j] == 'G':
                    pos_objetivo = (i, j)
    
    return grid, pos_inicial, pos_objetivo

def grid_para_grafo(grid: List[List[str]]) -> Tuple[Grafo, dict, dict]:
    """
    Converte um grid em um grafo
    Retorna: (grafo, mapeamento_posicao_para_id, mapeamento_id_para_posicao)
    """
    linhas = len(grid)
    colunas = len(grid[0])
    
    # Mapear posições válidas para IDs de vértices
    pos_para_id = {}
    id_para_pos = {}
    id_atual = 0
    
    # Primeiro, identificar células válidas (não são obstáculos)
    for i in range(linhas):
        for j in range(colunas):
            if grid[i][j] != '#':
                pos_para_id[(i, j)] = id_atual
                id_para_pos[id_atual] = (i, j)
                id_atual += 1
    
    # Criar grafo
    grafo = Grafo(id_atual, direcionado=True)
    
    # Direções: Norte, Sul, Leste, Oeste
    direcoes = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # Adicionar arestas
    for (i, j), id_origem in pos_para_id.items():
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            
            # Verificar se a nova posição está dentro dos limites
            if 0 <= ni < linhas and 0 <= nj < colunas:
                if (ni, nj) in pos_para_id:  # Célula válida
                    id_destino = pos_para_id[(ni, nj)]
                    
                    # Determinar o custo baseado no tipo de célula de destino
                    custo = obter_custo_celula(grid[ni][nj])
                    grafo.adicionar_aresta(id_origem, id_destino, custo)
    
    return grafo, pos_para_id, id_para_pos

def obter_custo_celula(celula: str) -> int:
    """Retorna o custo de movimento para um tipo de célula"""
    custos = {
        '.': 1,    # célula livre
        'S': 1,    # início
        'G': 1,    # objetivo  
        '~': 3     # piso difícil
    }
    return custos.get(celula, 1)

def imprimir_matriz(matriz: List[List[int]], titulo: str = "Matriz"):
    """Imprime uma matriz de forma formatada"""
    print(f"\n{titulo}:")
    for linha in matriz:
        print(" ".join(f"{val:3}" if val != float('inf') else "∞" for val in linha))

def imprimir_vetor(vetor: List[int], titulo: str = "Vetor"):
    """Imprime um vetor de forma formatada"""
    print(f"\n{titulo}:")
    print(" ".join(f"{val:3}" if val != float('inf') else "∞" for val in vetor))

def imprimir_caminho_grid(grid: List[List[str]], caminho_ids: List[int], 
                         id_para_pos: dict, pos_inicial: Tuple[int, int], 
                         pos_objetivo: Tuple[int, int]):
    """Imprime o grid com o caminho marcado"""
    # Criar cópia do grid
    grid_caminho = [linha[:] for linha in grid]
    
    # Marcar o caminho
    for id_vertice in caminho_ids:
        if id_vertice in id_para_pos:
            i, j = id_para_pos[id_vertice]
            if (i, j) != pos_inicial and (i, j) != pos_objetivo:
                grid_caminho[i][j] = '*'
    
    print("\nGrid com caminho marcado (* indica o caminho):")
    for linha in grid_caminho:
        print(''.join(linha))