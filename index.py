from Gerenciador import Gerencia

def index():
    #chamando a class gerencia 
    Geren = Gerencia()

    while True:

        print("\n Gerenciador de Atividade")
        print(" 1 - Adicionar atividadde ")
        print(" 2 - Concluir atividade ")
        print(" 3 - Lista atividades com maior prioridade ")
        print(" 4 - Lista atividades sem ordem")
        print(" 5 - Verificar o historico de atividade concluidas")
        print(" 0 - Sair")
        E = input("Escolha alguma opção: ")

        match E:
            case "1":
                titulo = input("Titulo da atividade: ")
                descricao = input("Descrição: ")
                prioridade = int(input("Prioridade 1=Alta, 2=Média, 3=Baixa: "))
                Geren.adicionando_atividade(titulo,descricao,prioridade)
            case "2":
                Geren.concluir_atividade_prioridade()
            
            case "3":
                Geren.listando_prioridade()
            
            case "4":
                Geren.listando_atividades()

            case "5":
                Geren.listar_historico()
            
            case "0":
                break

            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    index()