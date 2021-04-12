#Fazer um programa em que o computador escolhe um número aleatório e que leia a tentativa do usuário
#de acertar, mostrando uma mensagem na tela de acordo com o acerto ou não

from random import randint
from time import sleep
#O sleep é um tempinho que o computador espera

num = int(input("Digite um número entre 0 e 5: "));

aleatorio = randint(0, 5);
#Pega um número inteiro aleatório entre 0 e 5;

print("PROCESSANDO...");
sleep(1);

if num == aleatorio:
    print(f"Boooa, acertou, o número foi \033[32m{aleatorio}\033[m mesmo!");
else:
    print(f"Opa, não foi dessa vez! O número sorteado foi \033[35m{aleatorio}\033[m.");
