"""
Módulo para o cálculo da função recursiva F(n).

Este script resolve a equação de recorrência F(n) = 2F(n-1) + n^2,
implementando tanto a abordagem recursiva quanto a fórmula fechada,
conforme as regras e convenções do dever de casa.
"""

import math

def calcular_f_recursivo(n: int) -> int:
    """
    Calcula o valor da função F(n) recursivamente.
    
    A função chama a si mesma até atingir o caso base F(1) = 2.
    
    Args:
        n (int): O valor de entrada para a função (deve ser >= 1).
        
    Returns:
        int: O resultado calculado para F(n).
    """
    if n == 1:
        return 2
    
    return 2 * calcular_f_recursivo(n - 1) + n**2


def calcular_f_formula_fechada(n: int) -> int:
    """
    Calcula o valor da função F(n) utilizando sua fórmula matemática fechada.
    
    A fórmula fechada derivada da recorrência é:
    F(n) = 13 * 2^(n-1) - n^2 - 4n - 6
    
    Args:
        n (int): O valor de entrada para a função.
        
    Returns:
        int: O resultado exato da função utilizando a biblioteca math.
    """
    termo_exponencial = 13 * math.pow(2, n - 1)
    termo_polinomial = math.pow(n, 2) + 4 * n + 6
    
    # math.pow retorna float, então convertemos o resultado final para int
    return int(termo_exponencial - termo_polinomial)


def main():
    """Função principal que solicita os dados ao usuário e exibe os resultados."""
    print("--- Calculadora de Função Recursiva F(n) ---")
    print("Aviso: A complexidade do valor é alta, evite testar um n muito grande!\n")
    
    try:
        n = int(input("Digite um valor inteiro para n (n >= 1): "))
        
        if n < 1:
            print("Entrada inválida. O valor de n deve ser maior ou igual a 1.")
            return
            
        print("\nCalculando...")
        
        # 1. Usando a recursão exigida na tarefa
        resultado_recursao = calcular_f_recursivo(n)
        print(f"Resultado via Recursão: F({n}) = {resultado_recursao}")
        
        # 2. Usando a fórmula fechada exigida na dica
        resultado_fechado = calcular_f_formula_fechada(n)
        print(f"Resultado via Fórmula Fechada: F({n}) = {resultado_fechado}")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")
        
    except RecursionError:
        print("Erro: O valor de n é grande demais e excedeu o limite de recursão do Python.")

if __name__ == "__main__":
    main()