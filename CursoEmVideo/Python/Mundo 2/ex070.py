#Criar um programa que lê o nome e o preço de vários produtos e mostra análises no final

cont = menorpreco = totalcompra = tot1000 = 0;
nomemenorpreco = ' ';

print('LOJA Curso em Video');

while True:
    nome = str(input('Nome do produto: ')).strip().title();
    preco = int(input('Preço do produto: R$'));
    totalcompra += preco;
    cont += 1;

    if preco > 1000:
        tot1000 += 1;

    if cont == 1 or preco < menorpreco:
        menorpreco = preco;
        nomemenorpreco = nome;
    #else:
        #if preco < menorpreco:
            #menorpreco = preco;
            #nomemenorpreco = nome;
    opcao = ' ';                #LEMBRAR DE DEIXAR UM ESPAÇO!
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0];

    if opcao == 'N':
        break;
print('=' * 10, "Fim do programa", '=' * 10);
print(f'O total da compra foi R${totalcompra:.2f}');
print(f'Houve {tot1000} produtos que custaram mais de R$1000,00');
print(f'O nome do produto de menor preço é {nomemenorpreco} e o valor dele foi de R${menorpreco:.2f}');



