def calcular_potencia(base, expoente):
    if expoente == 0:
        resultado = 1
        return resultado
    else:
        expoente -= 1
        resultado = base * calcular_potencia(base, expoente)
        return resultado


print(calcular_potencia(2, 3))
