                            # Início dos exercícios de LISTAS parte 1

# Fazer um programa que leia 5 valores (int), os coloque em uma lista e mostre informações sobre ela

posmaior = posmenor = 0;

lista = list();

for num in range(0, 5):
    lista.append(int(input('Digite um valor: ')));
print(f'Os números digitados foram: {lista}');

maior = lista[0];
menor = lista[0];

# Laço para encontrar o maior e o menor valor da lista
for valor in lista:
    if valor > maior:
        maior = valor;

    if valor < menor:
        menor = valor;

print(f'O maior valor encontrado na lista foi {maior} na(s) posição(ões) ', end='');

# Verificando a posição (ou as) em que o maior valor da lista aparece
for pos, item in enumerate(lista):
    if item == maior:
        print(pos, end='...');

# Verificando agora sobre o menor valor da lista e sua(s) ocorrência(s)
print(f'\nO menor número digitado foi {menor} na(s) posição(ões) ', end='');
for pos, item in enumerate(lista):
    if item == menor:
        print(pos, end='...');
        


