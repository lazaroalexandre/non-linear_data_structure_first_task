def somar_entre(de, ate):
    if de != ate:
        print(f"{de} + 1 = {de+1}")
        de += 1
        return somar_entre(de, ate)


print(somar_entre(0, 5))
