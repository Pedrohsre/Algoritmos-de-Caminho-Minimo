"""
Script principal
"""

import sys
import os

def executar_cenarios():
    """Executa todos os três cenários"""
    
    print("=" * 80)
    print("ALGORITMOS DE CAMINHO MÍNIMO")
    print("=" * 80)
    
    # Importar os módulos dos cenários
    try:
        from cenario1 import encontrar_estacao_central
        from cenario2 import otimizar_caminho_carro
        from cenario3 import encontrar_caminho_robo
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")
        return
    
    print("\n" + "=" * 80)
    print("EXECUTANDO TODOS OS CENÁRIOS")
    print("=" * 80)
    
    # Cenário 1
    try:
        print("\n")
        encontrar_estacao_central("graph1.txt")
    except Exception as e:
        print(f"Erro no Cenário 1: {e}")
    
    # Cenário 2  
    try:
        print("\n" + "=" * 80)
        otimizar_caminho_carro("graph2.txt", 0, 6)
    except Exception as e:
        print(f"Erro no Cenário 2: {e}")
    
    # Cenário 3
    try:
        print("\n" + "=" * 80)
        encontrar_caminho_robo("grid_example.txt")
    except Exception as e:
        print(f"Erro no Cenário 3: {e}")
    
    print("\n" + "=" * 80)
    print("EXECUÇÃO COMPLETA!")
    print("=" * 80)

def main():
    if len(sys.argv) > 1:
        cenario = sys.argv[1]
        
        if cenario == "1":
            from cenario1 import encontrar_estacao_central
            encontrar_estacao_central("graph1.txt")
        elif cenario == "2":
            from cenario2 import otimizar_caminho_carro
            otimizar_caminho_carro("graph2.txt", 0, 6)
        elif cenario == "3":
            from cenario3 import encontrar_caminho_robo
            encontrar_caminho_robo("grid_example.txt")
        elif cenario == "todos" or cenario == "all":
            executar_cenarios()
        else:
            print("Uso: python main.py [1|2|3|todos]")
            print("  1 - Cenário 1: Estação Central")
            print("  2 - Cenário 2: Carro Elétrico") 
            print("  3 - Cenário 3: Robô de Armazém")
            print("  todos - Executar todos os cenários")
    else:
        executar_cenarios()

if __name__ == "__main__":
    main()