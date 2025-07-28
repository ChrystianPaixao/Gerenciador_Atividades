import heapq

class prioridade:

    def __init__(self):
        self.heap = []
    
    #adicionando prioridade
    def append_(self, atividade):
        heapq.heappush(self.heap, atividade)

    #removendo atividade com prioridade 
    def remover(self):
        if self.vazio():
            return None
        return heapq.heappop(self.heap)
    
    #listando prioridade
    def prioridade(self):
        if self.vazio():
            return None
        else:
            for atividade in sorted(self.heap):
                print(atividade)

    def vazio(self):
        return len(self.heap) == 0