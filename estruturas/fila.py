#importando da biblioteca collection 
from collections import deque

class Fila:

    def __init__(self):
        self.fila = deque()

    #Adicionando atividade na fila 
    def append_(self, atividade):
        self.fila.append(atividade)
    
    #visualizando a fila 
    def listar_(self):
        if self.vazia():
            return None
        else:
            for atividade in self.fila:
                print(atividade)

    #removendo atividade da lista 
    def popp_(self):
        if self.vazia():
            return None
        return self.fila.popleft()
    
    def vazia(self):
        return len(self.fila) == 0