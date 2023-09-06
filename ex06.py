class NoLista:
    
    def __init__(self, valor):
        self._valor = valor
        self._proximo = None

    
    def __repr__(self):
        return f"{self._valor} -> {self._proximo}"


class ListaLigada:
    
    def __init__(self):
        self._cabeca = None

    
    def __repr__(self):
        return f"[ {self._cabeca} ]"

    
    def adicionar_inicio(self, novo_valor):
        self._novo_no = NoLista(novo_valor)
        self._novo_no._proximo = self._cabeca
        self._cabeca = self._novo_no


lista = ListaLigada()
print(f"Lista: {lista}.")

lista.adicionar_inicio(5)
print(f"Lista: {lista}.")

lista.adicionar_inicio(10)
print(f"Lista: {lista}.")
