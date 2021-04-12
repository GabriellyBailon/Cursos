#Ler nome de quatro alunos e sortear um nome

from random import choice
print("Digite o nome dos alunos: ");
a1 = input("Nome do aluno 1: ");
a2 = input("Nome do aluno 2: ");
a3 = input("Nome do aluno 3: ");
a4 = input("Nome do aluno 4: ");
lista = [a1,a2,a3,a4];

sorteio = choice(lista);
#O método choice escolhe aleatoriamente um item da lista

print(f"O nome escolhido foi: {sorteio}");
