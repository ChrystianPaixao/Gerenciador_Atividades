class Atividade:

    def __init__(self, id, titulo, descricao, prioridade):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
    
    #comparando a prioridade da Atividade
    def __lt__(self, other):
        return self.prioridade < other.prioridade

    def __str__(self):
        return f"{self.id} Titulo - {self.titulo},   Descricao - {self.descricao},  Prioridade - {self.prioridade}"