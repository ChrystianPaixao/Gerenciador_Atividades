from estruturas.fila_ordenada import Historico
from estruturas.heap import prioridade
from estruturas.fila import Fila
from estruturas.atividade import Atividade

class Gerencia:

    #juntando todos as estruturas de dados dentro de uma estrutura
    def __init__(self):
        self.fila_orde = Historico()
        self.fila = Fila()
        self.heap = prioridade()
        self.contador = 1
    
    #adicionando o que foi digitado pelo usuario 
    def adicionando_atividade(self, titulo, descricao, prioridade):
        novo = Atividade(self.contador, titulo, descricao, prioridade)
        self.contador +=1 #o contador serve como id para cada atividade

        self.fila.append_(novo)
        self.heap.append_(novo)
        print(f"\n Nova Atividade {titulo}, foi adicionado com sucesso! ")

    #listando todas as atividades em ordem que foi adicionada na fila
    def listando_atividades(self):
        print("\n Atividades listadas: ")
        self.fila.listar_()
    
    def concluir_atividade_prioridade(self):
        atividade = self.heap.remover() # removendo a atividade do heap
        if atividade:
            self.fila_orde.append_(atividade) #adicionando a atividade concluida na fila_ordenada
            print(f"Atividade concluida: {atividade}")
        else:
            print("Nenhum atividade foi concluida")
    #listando as atividades com prioridade 
    def listando_prioridade(self):
        print("\n Listando atividade com mais prioridade: ")
        self.heap.prioridade()
    #listando as atividades concluidas 
    def listar_historico(self):
        print("\n Listando historico de prioridade: ")
        self.fila_orde.listar_atividades()