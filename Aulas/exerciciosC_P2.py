#minha solucao com ajuda do GPT
import threading
from time import sleep

def primeira_thread(tempo_espera, mensagem):
    print("\nInciando tarefa.", mensagem)
    sleep(tempo_espera)
    print("Conclusão primeira thread", mensagem)

def segunda_thread(tempo_espera, mensagem):
    print("\nIniciando tarefa", mensagem)
    sleep(tempo_espera)
    print("Conclusão Segunda thread", mensagem)

thread1 = threading.Thread(target=primeira_thread, args=(3, "\nThread 1 em execução..."))
thread2 = threading.Thread(target=segunda_thread, args=(2, "\nThread 2 em execução..."))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as threads foram executadas e concluidas.")