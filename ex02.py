def interseccionar_valores(primeiro_vetor, segundo_vetor):
    vetor_interseccao = []
    for primeiro in primeiro_vetor:
        for segundo in segundo_vetor:
            if segundo == primeiro:
                vetor_interseccao.append(segundo)

    return vetor_interseccao


primeiro_vetor = [2, 3, 1, 4, 5]
segundo_vetor = [6, 2, 7, 4, 8]

print(interseccionar_valores(primeiro_vetor, segundo_vetor))
