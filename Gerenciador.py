from estruturas.fila_ordenada import Historico
from estruturas.heap import prioridade
from estruturas.fila import Fila
from estruturas.atividade import Atividade

class Gerencia:

    def __init__(self):
        self.fila_orde = Historico()
        self.fila = Fila()
        self.heap = prioridade()
        self.contador = 1
    
    def adicionando_atividade(self, titulo, descricao, prioridade):
        novo = Atividade(self.contador, titulo, descricao, prioridade)
        self.contador +=1

        self.fila.append_(novo)
        self.heap.append_(novo)
        print(f"\n Nova Atividade {titulo}, foi adicionado com sucesso! ")

    
    def listando_atividades(self):
        print("\n Atividades listadas: ")
        self.fila.listar_()
    
    def concluir_atividade_prioridade(self):
        atividade = self.heap.remover()
        if atividade:
            self.fila_orde.append_(atividade)
            print(f"Atividade concluida: {atividade}")
        else:
            print("Nenhum atividade foi concluida")
    
    def listando_prioridade(self):
        print("\n Listando atividade com mais prioridade: ")
        self.heap.prioridade()

    def listar_historico(self):
        print("\n Listando historico de prioridade: ")
        self.fila_orde.listar_atividades()