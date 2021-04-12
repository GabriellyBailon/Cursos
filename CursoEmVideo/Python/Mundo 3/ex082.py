# Ler vários números e colocá-los em uma lista, organizá-los em diferentes listas se forem pares ou
# ímpares e ao fim, mostrar as 3 listas para o usuário

lista = [];
listapares = [];
listaimpares = [];

while True:
    lista.append(int(input('Digite um número: ')));
    opcao = ' ';
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0];
    if opcao == 'N':
        break;
print(f'Os números digitados foram {lista}');

for item in lista:
    if item % 2 == 0:
        listapares.append(item);
    else:
        listaimpares.append(item);

print(f'Os valores pares digitados foram {listapares}'
      f'\nE os valores ímpares foram {listaimpares}');



