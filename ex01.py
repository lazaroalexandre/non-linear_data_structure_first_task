def valores_entre(vetor, de, ate):
    vetor_filtro = []

    for indice in vetor:
        if indice > de and indice < ate:
            vetor_filtro.append(indice)

    return vetor_filtro


vetor = [2, 3, 1, 10, 5, 6, 9, 7]

print(valores_entre(vetor, 3, 7))
