#minha solução
import threading
import time

def minha_thread(mensagem):
    print("Iniciando a Thread.")
    print("Mensagem: ", mensagem)
    time.sleep(1)
    print("\nFinalizando a Thread.")

mensagem = "Threads em execução"
minha_thread = threading.Thread(target=minha_thread, args=(mensagem,))
minha_thread.start()

print("\nStart da Thread")

minha_thread.join()

print("A thread principal terminou.")