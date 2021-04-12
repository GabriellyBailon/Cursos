# Ler vários números, colocando-os em uma lista e analisar informações sobre eles

lista = [];

while True:
    lista.append(int(input('Digite um número: ')));

    #Limpa a opção e garante o funcionamento correto do loop
    opcao = ' ';
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?[S/N] ')).strip().upper()[0];

    if opcao == 'N':
            break;
print('-=' * 30);
print(f'Foram digitados {len(lista)} números');

lista.sort(reverse=True);
print(f'A lista em ordem decrescente: {lista}');

if 5 in lista:
    print('O número 5 foi digitado!');
else:
    print('O número 5 não foi digitado!');
    





