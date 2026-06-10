class Pilha:
    #ultimo a entrar e primeiro a sair - historico de alertas
    def __init__(self):
        self._dados = []

    def empilhar(self, item):
        #adiciona item no topo
        self._dados.append(item)

    def desempilhar(self):
        #remove e retorna o item do topo
        if self.esta_vazia():
            raise IndexError("Pilha vazia, não é possível desempilhar.")
        return self._dados.pop()

    def topo(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia.")
        return self._dados[-1]

    def esta_vazia(self):
        return len(self._dados) == 0

    def tamanho(self):
        return len(self._dados)

    def __repr__(self):
        return f"Pilha({self._dados})"


class Fila:
    #primeiro a entrar e primeiro a sair - organizar a ordem de atendimento das regioes em risco
    def __init__(self):
        self._dados = []

    def enfileirar(self, item):
        #adiciona item no final da fila
        self._dados.append(item)

    def desenfileirar(self):
        #remove e retorna o primeiro item da fila
        if self.esta_vazia():
            raise IndexError("Fila vazia, não é possível desenfileirar.")
        return self._dados.pop(0)

    def frente(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self._dados[0]

    def esta_vazia(self):
        return len(self._dados) == 0

    def tamanho(self):
        return len(self._dados)

    def __repr__(self):
        return f"Fila({self._dados})"


#no - lista ligada, cada no guarda um valor e aponta pro proximo
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None  #começa apontando pra nada


class ListaLigada:
    #lista ligada - registra as regioes monitoradas em cadeia
    def __init__(self):
        self._cabeca = None  #primeiro no da lista
        self._tamanho = 0

    def inserir(self, valor):
        #cria novo no e coloca no final da lista
        novo = No(valor)
        if self._cabeca is None:
            #lista vazia, novo no vira o header
            self._cabeca = novo
        else:
            #percorre ate o ultimo no e liga o novo
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1

    def remover(self, valor):
        #percorre a lista procurando o valor pra remover
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    #removendo o head
                    self._cabeca = atual.proximo
                else:
                    #pula o no removido
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar(self, valor):
        #percorre a lista procurando o valor
        atual = self._cabeca
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        #imprime todos os nos da lista
        atual = self._cabeca
        i = 1
        while atual is not None:
            print(f"[{i}] {atual.valor}")
            atual = atual.proximo
            i += 1
        if i == 1:
            print("(lista vazia)")

    def esta_vazia(self):
        return self._cabeca is None

    def tamanho(self):
        return self._tamanho

    def __repr__(self):
        elementos = []
        atual = self._cabeca
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return "--> ".join(elementos) + "--> None"