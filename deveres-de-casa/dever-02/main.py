import sys
import time

# Constante para definir os valores de teste (SCREAMING_SNAKE_CASE)
VALORES_TESTE = [10, 100, 500, 1000]

# Aumentamos o limite de recursão do Python.
# Por padrão, o limite é 1000, o que causaria um erro (RecursionError) ao testar n=1000.
sys.setrecursionlimit(2000)

def calcular_fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro de forma recursiva.

    Args:
        n (int): O número inteiro para o qual o fatorial será calculado.

    Returns:
        int: O resultado de n! (fatorial de n).
    """
    # Caso base: O fatorial de 0 ou 1 é 1. Isso para a recursão.
    if n == 0 or n == 1:
        return 1
    
    # Chamada recursiva: n multiplicado pelo fatorial de (n - 1)
    return n * calcular_fatorial(n - 1)

def medir_desempenho() -> None:
    """
    Mede o tempo de execução do algoritmo de fatorial para diferentes tamanhos de entrada (n).
    """
    print("\n--- Medição de Tempo de Execução ---")
    for valor in VALORES_TESTE:
        inicio = time.perf_counter() # Inicia o cronômetro com alta precisão
        
        calcular_fatorial(valor) # Executa o cálculo
        
        fim = time.perf_counter() # Para o cronômetro
        tempo_execucao = fim - inicio
        
        print(f"Tempo para n = {valor:<4}: {tempo_execucao:.8f} segundos")

if __name__ == "__main__":
    # Instrução 1.1: Lê um número inteiro n do usuário
    try:
        entrada_usuario = int(input("Digite um número inteiro 'n' para calcular o fatorial: "))
        if entrada_usuario < 0:
            print("Não existe fatorial de número negativo.")
        else:
            resultado = calcular_fatorial(entrada_usuario)
            print(f"O fatorial de {entrada_usuario} é {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

    # Instrução 2: Mede o tempo de execução para 10, 100, 500 e 1000
    medir_desempenho()