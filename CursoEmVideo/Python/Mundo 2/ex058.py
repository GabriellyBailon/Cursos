#Melhorar o jogo do Desafio 28, fazendo-o rodar até o usuário  acertar e mostrando quantas tentativas
#foram necessárias para isso

from random import randint

cont = 0;
computador = randint(0, 10);
usuario = int(input("Digite um número inteiro: "));

while not (computador == usuario):
    if usuario < computador:
        usuario = int(input("Ops, meu número é maior!\nEm qual número o computador pensou? "));
    else:
        usuario = int(input("Ops, meu número é menor!\nEm qual número o computador pensou? "));

    cont += 1;

print(f"PARABÉNS!!! Você acertou! O computador pensou em \033[35m{computador}\033[m e você em \033[35m{usuario}\033[m em \033[34m{cont}\033[m chance(s)!");










