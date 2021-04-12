#Ler números até o usuário digitar 999 e então mostrar a soma deles

num = soma = cont = 0;
num = int(input('Digite um número (999 para parar): '));

while num != 999:
    cont += 1;
    soma = soma + num;
    num = int(input('Digite um número (999 para parar): '));

print(f'A soma entre os {cont} números é {soma}');




