def media_mediana(matriz):
    soma = ultimo_valor = penultimo_valor = media = mediana = 0
    lista = []

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]
            lista.append(matriz[linha][coluna])
            lista.sort()
    media = soma / len(lista)

    if len(lista) % 2 == 1:
        for i in range(len(lista) // 2 + 1):
            if i == (len(lista) // 2):
                mediana = lista[i]
    else:
        for i in range(len(lista) // 2 + 1):
            if i == ((len(lista) // 2) - 1):
                penultimo_valor = lista[i]
            elif i == ((len(lista) // 2)):
                ultimo_valor = lista[i]
        mediana = (ultimo_valor + penultimo_valor) / 2

    return f"Média: {media:.2f}\nMediana {mediana}"


matriz = [[2, 4, 5], [3, 5, 4], [5, 2, 1]]

print(media_mediana(matriz))
