#Ler números até o 999 ser digitado, quando chegar ao final, mostrar a soma deles e quantos foram

num = cont = soma = 0;

while True:
    num = int(input('Digite um número: '));
    if num == 999:
        break;
    soma += num;
    cont += 1;


print(f'Foi/Foram digitado(s) {cont} número(s) e a soma dele(s) foi {soma}');




