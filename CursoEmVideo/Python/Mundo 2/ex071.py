#Caixa eletrônico, o usuário irá solicitar um valor inteiro e vai ser mostrada a ele as possibilidades
#de notas a serem entregues

from math import floor              #Para arredondar para baixo a divisão do 50, pois ocorria um erro

cont100 = cont50 = cont20 = cont10 = cont1 = 0;

print('=' * 40);
print('{:^40}'.format('Banco Olá'));
print('=' * 40);

while True:
    usuario = int(input('Digite o valor que deseja sacar: R$'));
    print('=' *40);

    print("Analisando...", end='');
    print("Será possível realizar o saque da seguinte forma: ");

    if usuario >= 50:
        cont50 += floor(usuario / 50);
        print(f'{cont50:.0f} cédula(s) de R$50,00');
        usuario = usuario % 50;
    if usuario >= 20:
        cont20 += floor(usuario / 20);
        print(f'{cont20:.0f} cédula(s) de R$20,00');
        usuario = usuario % 20;
    if usuario >= 10:
        cont10 += floor(usuario /10);
        print(f'{cont10:.0f} cédula(s) de R$10,00')
        usuario %= 10;
    if usuario >= 1:
        cont1 += usuario / 1;
        print(f'{cont1:.0f} cédula(s) de R$1,00');

    break;
print('=' * 40);
print('O nosso Banco agradece o seu contato. Volte sempre e tenha um ótimo dia!');


