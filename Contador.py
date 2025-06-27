
def es_par_o_impar(numero):
    """
    Devuelve una cadena indicando si el número es par o impar.

    Parámetros:
    numero (int): número a evaluar.

    Retorna:
    str: una cadena con el número y su clasificación (par o impar).
    """
    if numero % 2 == 0:
        return f"{numero} - par"
    else:
        return f"{numero} - impar"

def cuenta_regresiva(n):
    """
    Imprime los números desde n hasta 0 utilizando un bucle for,
    mostrando también si son pares o impares.

    Parámetros:
    n (int): número entero desde el cual iniciar la cuenta regresiva.
    """
    # range(n, -1, -1) genera una secuencia desde n hasta 0, descendiendo de uno en uno.
    for i in range(n, -1, -1):
        # Imprime el número con su clasificación de paridad (par o impar).
        print(es_par_o_impar(i))
