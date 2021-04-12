#Refazer o Desafio 61 agora dando a opção para o usuário escolher se quer que o programa mostre
#mais termos da PA e quantos serão

primeirotermo = int(input('Digite o primeiro termo da PA: '));
razao = int(input('Agora digite a razão da PA: '));
cont = 1;
qtstermos = 10;
pa = primeirotermo;
total = 0;
maistermos = '';

while maistermos != 0:
    while cont <= qtstermos:
        print(pa, end=' ');
        total = total + 1;
        pa += razao;
        cont += 1;
    maistermos = int(input('\nQuantos termos a mais da PA deseja que sejam calculados? '));
    if maistermos == 0:
        print(f'\nFim do programa, ao todo foram mostrados {total} termos.');
    else:
        qtstermos += maistermos;





