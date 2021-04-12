# Gerar 5 números aleatórios em uma tupla, mostrá-los e mostrar também o maior e o menor

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10));                 # Sorteando 5 números sem usar o "for"

print('Os números sorteados são: ', end='');
for n in numeros:
    print(n, end=' ');

maior = numeros[0];
menor = numeros[0];

for c in range(0, 5):
    if maior < numeros[c]:
        maior = numeros[c];

    if menor > numeros[c]:
        menor = numeros[c];

print(f'\nO maior número sorteado foi {maior}');           #Pode-se usar o método "max(numeros)"

print(f'O menor número sorteado foi {menor}');             #Pode-se usar o método "min(numeros)"


