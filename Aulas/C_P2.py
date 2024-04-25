import threading
import time

#exemplo de funcao com parametros
def funcao(mensagem):
    for i in range(3):
        print(i,mensagem)
        time.sleep(0.2)

print("Inciciando o programa")
x = threading.Thread(target=funcao, args=("Executando!!",))
x.start()
print("Finalzando o Programa!")