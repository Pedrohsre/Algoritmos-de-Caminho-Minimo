"""
Cenário 3: Robô de armazém com obstáculos

Algoritmo utilizado: Dijkstra
O grid só possui custos não-negativos (células livres custam 1, 
piso difícil custa 3), permitindo o uso eficiente do Dijkstra para 
encontrar o caminho ótimo de um único ponto de origem (S) ao destino (G).
"""

from algoritmos import dijkstra, reconstruir_caminho
from utils import ler_grid_arquivo, grid_para_grafo, imprimir_caminho_grid

def encontrar_caminho_robo(arquivo_grid: str):
    """
    Encontra o caminho de menor custo para um robô navegar em um armazém
    """
    print("=== Cenário 3: Robô de armazém com obstáculos ===")
    print(f"Lendo grid do arquivo: {arquivo_grid}")
    
    # Ler o grid
    grid, pos_inicial, pos_objetivo = ler_grid_arquivo(arquivo_grid)
    
    if pos_inicial is None or pos_objetivo is None:
        print("Erro")
        return
    
    print(f"Grid carregado: {len(grid)}x{len(grid[0])}")
    print(f"Posição inicial (S): {pos_inicial}")
    print(f"Posição objetivo (G): {pos_objetivo}")
    
    # Imprimir grid original
    print(f"\nGrid original:")
    for linha in grid:
        print(''.join(linha))
    
    # Converter grid para grafo
    print(f"\nConvertendo grid para grafo...")
    grafo, pos_para_id, id_para_pos = grid_para_grafo(grid)
    print(f"Grafo criado com {grafo.num_vertices} vértices válidos")
    
    # Obter IDs dos vértices de origem e destino
    id_origem = pos_para_id[pos_inicial]
    id_destino = pos_para_id[pos_objetivo]
    
    print(f"ID do vértice origem: {id_origem}")
    print(f"ID do vértice destino: {id_destino}")
    
    # Aplicar Dijkstra
    print(f"\nAplicando algoritmo Dijkstra...")
    distancias, anterior = dijkstra(grafo, id_origem)
    
    # Verificar se há caminho
    if distancias[id_destino] == float('inf'):
        print("Não há caminho possível de S para G!")
        return
    
    # Reconstruir o caminho e converter IDs de volta para posições

    caminho_ids = reconstruir_caminho(anterior, id_origem, id_destino)
    caminho_posicoes = [id_para_pos[id_v] for id_v in caminho_ids]
    
    # Custo total
    custo_total = distancias[id_destino]
    
    # Resultados
    print(f"Caminho encontrado de S para G:")
    print(f"Sequência de posições (linha, coluna):")
    for i, pos in enumerate(caminho_posicoes):
        if i == 0:
            print(f"  {i+1}. {pos} (S - início)")
        elif i == len(caminho_posicoes) - 1:
            print(f"  {i+1}. {pos} (G - objetivo)")
        else:
            print(f"  {i+1}. {pos}")
    
    print(f"\nCusto total do caminho: {custo_total}")
    print(f"Número de passos: {len(caminho_posicoes) - 1}")
    
    # Mostrar custos detalhados
    print(f"\nDetalhamento dos custos por movimento:")
    custo_acumulado = 0
    for i in range(len(caminho_posicoes) - 1):
        pos_atual = caminho_posicoes[i]
        pos_proxima = caminho_posicoes[i + 1]
        
        # Custo é baseado na célula de destino
        celula_destino = grid[pos_proxima[0]][pos_proxima[1]]
        custo_movimento = 1 if celula_destino in ['.', 'S', 'G'] else 3
        custo_acumulado += custo_movimento
        
        direcao = obter_direcao(pos_atual, pos_proxima)
        print(f"  {i+1}. {pos_atual} -> {pos_proxima} ({direcao}): +{custo_movimento} = {custo_acumulado}")
    
    # Visualizar caminho no grid
    imprimir_caminho_grid(grid, caminho_ids, id_para_pos, pos_inicial, pos_objetivo)
    
    # Estatísticas dos tipos de célula no caminho
    tipos_celula = {}
    for pos in caminho_posicoes:
        celula = grid[pos[0]][pos[1]]
        tipos_celula[celula] = tipos_celula.get(celula, 0) + 1
    
    print(f"\nEstatísticas do caminho:")
    for tipo, quantidade in tipos_celula.items():
        descricao = {
            'S': 'Início',
            'G': 'Objetivo', 
            '.': 'Células livres',
            '~': 'Piso difícil'
        }.get(tipo, 'Desconhecido')
        print(f"  {descricao}: {quantidade}")
    
    return caminho_posicoes, custo_total

def obter_direcao(pos1, pos2):
    """Retorna a direção do movimento entre duas posições"""
    di = pos2[0] - pos1[0]
    dj = pos2[1] - pos1[1]
    
    if di == -1:
        return "Norte"
    elif di == 1:
        return "Sul"
    elif dj == 1:
        return "Leste"
    elif dj == -1:
        return "Oeste"
    else:
        return "?"

if __name__ == "__main__":
    encontrar_caminho_robo("grid_example.txt")