class Fila_ordenada:

    def __init__(self, atividade):
        self.atividade = atividade
        self.atiPr = None
    
class Historico:

    def __init__(self):
        self.histor = None

    #adicionando uma atividade concluida 
    def append_(self, atividade):
        novo = Fila_ordenada(atividade)
        if self.histor is None:
            self.histor = novo
        else:
            inicio = self.histor
            while inicio.atiPr:
                inicio = self.histor
            inicio.atiPr = novo

    #listar atividade concluidas
    def listar_atividades(self):
        if self.histor is None:
            return None
        else:
            inicio = self.histor
            while inicio:
                print(inicio.atividade)
                inicio = inicio.atiPr