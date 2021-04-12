#Ler um número e mostrar se ele é primo ou não

num = int(input("Digite um número inteiro: "));
cont = 0;

for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[33m{c}\033[m", end=' ');
        cont += 1;
    else:
        print(f"\033[31m{c}\033[m", end=' ');

if cont == 2:
    print(f"\nO número {num} foi dividido {cont} vezes e É SIM um número PRIMO!");
else:
    print(f"\nO número {num} foi divido {cont} vezes e NÃO É um número PRIMO!");




