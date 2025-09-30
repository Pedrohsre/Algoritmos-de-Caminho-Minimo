# Algoritmos de Caminho Mínimo

Este projeto implementa três algoritmos clássicos de caminho mínimo em grafos: Dijkstra, Bellman-Ford e Floyd-Warshall.

## Compilação/Utilização

### Utilizados
- Python 3.13.7
- Bibliotecas padrão do Python

### Execução dos Cenários

1. **Execução Individual**:
```bash
# Cenário 1 - Estação Central
python cenario1.py

# Cenário 2 - Carro Elétrico  
python cenario2.py

# Cenário 3 - Robô de Armazém
python cenario3.py
```

2. **Script Principal** (rode nesse):
```bash
# Executar todos os cenários
python main.py

# Executar cenário específico
python main.py 1    # Apenas cenário 1
python main.py 2    # Apenas cenário 2  
python main.py 3    # Apenas cenário 3
python main.py todos # Todos os cenários
```

## Algoritmos Utilizados

### Cenário 1: Floyd-Warshall
- Necessário calcular distâncias de todos os vértices para todos os outros para determinar a estação central

### Cenário 2: Bellman-Ford
- O grafo possui arestas com pesos negativos (regeneração de energia)

### Cenário 3: Dijkstra
- Grafo com pesos não-negativos e necessidade de caminho ótimo de um único ponto de origem

## Comparativo do pseudo código 
- Comparativo entre os psudo códigos no livro e implementados no arquivo comparativo_algoritmo.md