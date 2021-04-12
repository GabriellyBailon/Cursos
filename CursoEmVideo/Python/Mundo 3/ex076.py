# Criar uma única tupla com nomes de objetos e preços em sequência,
# no final mostrá-los de forma tabular

print('--' * 20);
print(f'{"LISTANDO PRODUTOS E PREÇOS":^40}');
print('--' * 20);

produtos = ('Lápis', 1.20, 'Borracha', 0.50, 'Caneta', 2.00, 'Mochila', 55.00);

quantidade = len(produtos);

for p in range(0, quantidade):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end='');
    else:
        print(f'R${produtos[p]:>7.2f}');

print('--' * 20);





