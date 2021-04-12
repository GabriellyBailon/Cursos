# Faça uma lista que receba números enquanto o usuário desejar, mas apenas os não repetidos e mostre
# algumas informações sobre

lista =[];
opcao = ' ';


while True:
        lista2 = lista[:];
        lista.append(int(input('Digite um número: ')));
        if lista[-1] in lista2:
            print('O item já existe na lista e não será adicionado');
            lista.pop();

        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0];

        while opcao not in 'SN':
            opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0];
        if opcao == 'N':
            break;

# A função deve ser chamada antes da impressão
lista.sort();
print(f'Os números digitados (em ordem crescente) foram {lista}');

