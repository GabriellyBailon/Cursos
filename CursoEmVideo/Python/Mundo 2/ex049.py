#Refazer o desafio 9 mostrando a tabuada do número que o usuário pedir, dessa vez usando o for

from random import randint

cor = randint(30, 37);
num = int(input("Digite um número inteiro e veja sua tabuada: "));

for c in range(0, 11):
    print(f"\033[{cor}m{num}\033[m x \033[{cor}m{c}\033[m = \033[{cor}m{num * c}\033[m");



