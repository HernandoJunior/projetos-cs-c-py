class Tarefa:
    def __init__(self, texto_da_tarefa, status=False):
        self.texto_da_tarefa = texto_da_tarefa
        self.status = status
        
    def marcar_como_concluida(self):
        self.status = True

    def desmarcar_concluida(self):
        self.status = False
    
    def __str__(self):
        if self.status == True:
            return f"\x1b[9m{self.texto_da_tarefa}\x1b[0m"
        else:
            return f"{self.texto_da_tarefa}"
        
class ListaDeTarefas:
    def __init__(self):
        self.listaTarefas =[]
     
    def adicionar_tarefa(self, texto_da_tarefa):
        tarefa1 = Tarefa(texto_da_tarefa)
        self.listaTarefas.append(tarefa1)
        
    def deletar_tarefa(self, deletado):
        if not self.listaTarefas:
            return False
        elif 1 <= deletado <= len(self.listaTarefas):
            del self.listaTarefas[deletado - 1]
            return True  
        else:
            return False 
        
    def marcar_tarefa(self, marcacao):
        if 1 <= marcacao <= len(self.listaTarefas):
            self.listaTarefas[marcacao-1].marcar_como_concluida()
        else:
            print("Opcao invalida!")
            
    def desmarcar_tarefa(self, desmarcar):
        if 1 <= desmarcar <= len(self.listaTarefas):
            self.listaTarefas[desmarcar-1].desmarcar_concluida()
        else:
            print("Opcao invalida")
            
    def mostrar_tarefas(self):
        mostrador = ''
        if not self.listaTarefas:
            return False
        else:
            mostrador += "Id  | Tarefa\n" if not mostrador else ''
            for i, tarefa in enumerate(self.listaTarefas, start=1):
                mostrador += f" {i}  | {tarefa}\n"
            return mostrador

def run():
    import os
    instancia = ListaDeTarefas()
    while True:
        print()
        print("########## LISTA DE TAREFAS ##########")
        print(" 1 - Adicionar tarefa")
        print(" 2 - Marcar como tarefa concluída")
        print(" 3 - Desmarcar tarefa como concluída")
        print(" 4 - Mostrar tarefas")
        print(" 5 - Deletar tarefa")
        print(" 6 - Sair do programa")

        opcao = input(" -> ")

        os.system('cls')
        try: 
            match opcao:
                case '1':
                    tarefa = input('Digite o texto da tarefa: ')
                    instancia.adicionar_tarefa(tarefa)
                case '2':
                    if not instancia:
                        print("Não existem tarefas na lista.")
                    else:
                        print(instancia.mostrar_tarefas())
                        indice = int(input("Informe o ÍNDICE de qual tarefa você quer MARCAR como concluída: "))
                        instancia.marcar_tarefa(indice)
                        print(instancia.mostrar_tarefas())
                case '3':
                    if not instancia:
                        print("Não existem tarefas na lista.")
                    else:
                        print(instancia.mostrar_tarefas())
                        indice = int(input("Informe o ÍNDICE de qual tarefa você quer DESMARCAR como concluída: "))
                        instancia.desmarcar_tarefa(indice)
                        print(instancia.mostrar_tarefas())
                case '4':
                    print(instancia.mostrar_tarefas())
                case '5':
                    if not instancia:
                        print("Não existem tarefas na lista.")
                    else:
                        print(instancia.mostrar_tarefas())
                        indice = int(input("Informe o ÍNDICE de qual tarefa você quer DELETAR: "))
                        if instancia.deletar_tarefa(indice):
                            print(f"Tarefa {indice} deletada.")
                        else:
                            print("Índice inválido.")
                        print(instancia.mostrar_tarefas())
                case '6':
                    break
                case _:
                    print("Opção inválida")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
        except KeyboardInterrupt:
            print("\nEncerrando a aplicação.")
            break

run()       
        
          
    

    
        
        
        