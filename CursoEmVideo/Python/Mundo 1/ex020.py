#Ler o nome de quatro alunos e devolver uma ordem aleatória desses nomes

from random import sample
print("Digite os nomes dos 4 alunos: ");
n1 = str(input("Nome do primeiro aluno: "));
n2 = str(input("Nome do segundo aluno: "));
n3 = str(input("Nome do terceiro aluno: "));
n4 = str(input("Nome do quarto aluno: "));
lista = [n1,n2,n3,n4];

sorteio = sample(lista, k=4);
#Primeiro parâmetro é a lista que vai ser randomizada e o segundo, o número de itens da lista que se deseja randomizar;

#Pode se usar o shuffle no lugar do sample. Ele não precisa do parâmetro "k";

print(f"A ordem de apresentação será: {sorteio}.");