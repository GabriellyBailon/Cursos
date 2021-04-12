# Fazer um programa que leia 4 valores pelo usuário,
# os guarde em uma tupla e apresente informações sobre eles

# MACETE para uma tupla LER valores já que tuplas são IMUTÁVEIS
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ', )),
           int(input('Digite mais um número: ', )), int(input('Digite um último número: ')));
print(f'Você digitou os números {numeros}');

print(f'O número 9 apareceu {numeros.count(9)} vezes.');

# Verificando se o número 3 foi digitado
if 3 in numeros:
    print(f'O valor 3 foi digitado pela primeira vez na posição {numeros.index(3)+1}');
else:
    print('O número 3 não foi digitado em nenhuma posição.');

print('Os números pares digitados foram: ', end='');
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ');







