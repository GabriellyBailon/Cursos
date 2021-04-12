#Fazer aparecer a contagem regressiva de 10 até 0, com pausa de 1 segundo e "fogos de artifício"
#no final

from time import sleep


for c in range(10, -1, -1):
    sleep(1);
    print(c);
print("FELIZ ANO NOVOOOOO!");




