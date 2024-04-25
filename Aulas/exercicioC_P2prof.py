#Solucao do Professor
from time import sleep
from threading import Thread

def tarefa(tempo_espera, nome_tarefa):
    print(f"Iniciando a Tarefa {nome_tarefa}")
    sleep(tempo_espera)
    print(f"Conclusão da tarefa {nome_tarefa}")

t1 = Thread(target=tarefa, args=(3, "A"))
t2 = Thread(target=tarefa, args=(2, "B"))
t1.start()
t2.start()
t1.join()
t2.join()
print("A Execução foi concluída!")