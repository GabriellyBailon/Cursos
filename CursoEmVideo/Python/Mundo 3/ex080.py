# Ler 5 números, colocá-los em uma lista já em ordem sem utilizar o método "sort"

lista = [];

for item in range(0, 5):
    n = (int(input('Digite um número: ')));

    if item == 0:
        maior = menor = n;
        lista.append(n);
        print('O item foi colocado ao final da lista');

    elif n >= maior:
        lista.append(n);
        print(f'O item foi colocado no final da lista');
        maior = n;

    elif n <= menor:
        lista.insert(0, n);
        print(f'O item foi colocado na posição {len(lista)}');
        menor = n;
    else:
        for cont in range(0, len(lista)):
            if n > lista[cont] and n < lista[cont + 1]:
                lista.insert(cont+1, n);
                print(f'O item foi colocado na posição {len(lista)}');

print(lista);
