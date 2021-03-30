def contar_caracteres(s):
    """Funcão que conta os caracteres de uma strung

    EX:

    >>> contar_caracteres('jackson')
    {'a': 1, 'c': 1, 'j': 1, 'k': 1, 'n': 1, 's': 1, 'o': 1}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0)+1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('jackson'))
    print()
    print(contar_caracteres('banana'))
