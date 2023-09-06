def eliminar_menor_valor(matriz, valor):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] <= valor:
                matriz[linha][coluna] = 0

    return matriz


matriz = [[2, 4, 5], [3, 5, 4], [5, 2, 1]]

print(eliminar_menor_valor(matriz, 3))
