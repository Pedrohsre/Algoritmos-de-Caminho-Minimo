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

2. **Script Principal**:
```bash
# Executar todos os cenários (USE ESTE)
python main.py

# Executar cenário específico
python main.py 1    # Apenas cenário 1
python main.py 2    # Apenas cenário 2  
python main.py 3    # Apenas cenário 3
python main.py todos # Todos os cenários
```

## Motivação

### Cenário 1: Floyd-Warshall
- Precisamos calcular distâncias entre TODOS os pares de vértices para comparar qual é o melhor candidato a estação central. Floyd-Warshall resolve o problema "todos-para-todos" em uma única execução.

### Cenário 2: Bellman-Ford
- O grafo possui arestas NEGATIVAS (regeneração de energia). Dijkstra não funciona com pesos negativos, mas Bellman-Ford foi projetado especificamente para isso.

### Cenário 3: Dijkstra
- Todos os custos são não-negativos e precisamos apenas de um caminho origem→destino. Dijkstra é o mais eficiente para esse caso.

## Comparativo do pseudocódigo 
- Análise lado a lado dos algoritmos apresentados no livro versus as implementações práticas desenvolvidas no projeto no arquivo `comparativo_algoritmo.md`.
