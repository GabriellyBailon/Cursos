#Refazer o Desafio 51 da PA usando o "while"

primeirotermo = int(input('Digite o primeiro termo da PA: '));
razao = int(input('Agora digite a razão da PA: '));
vezes = 10;
cont = 0;
pa = primeirotermo;

print(f'Os {vezes} termos da PA são: {pa}', end=' ');
cont += 1;
while cont < vezes:
    pa = pa + razao;
    cont += 1;
    print(pa, end=' ');

print('\nFim do programa');












        