"""Módulo para verificação recursiva de palíndromos em arrays."""


def verificar_palindromo(array):
    """
    Verifica se um array é um palíndromo de forma recursiva.

    Args:
        array (list): O array (lista) a ser verificado.

    Returns:
        bool: True se for palíndromo, False caso contrário.
    """
    # Caso base: se o array tem 0 ou 1 elemento, ele é um palíndromo por natureza
    if len(array) <= 1:
        return True

    # Verifica se o primeiro e o último elemento são iguais
    if array[0] == array[-1]:
        # Chamada recursiva com o "miolo" do array (excluindo as pontas que já foram checadas)
        return verificar_palindromo(array[1:-1])

    # Se as pontas forem diferentes, não é palíndromo
    return False


if __name__ == "__main__":
    # Casos de teste exatamente como os exemplos da imagem
    testes = [
        ([0, 1, 2, 3, 2, 1, 0], True),
        (["a", "b", "b", "a"], True),
        (["a", "b", "c", "b", "a"], True),
        (["a", "b", "c", "f", "b", "a"], False),
    ]

    print("Testando os arrays de exemplo:")
    for i, (lista, esperado) in enumerate(testes, start=1):
        resultado = verificar_palindromo(lista)
        status = "Correto" if resultado == esperado else "Erro"
        print(f"array{i} = {lista} -> É palíndromo? {resultado} [{status}]")