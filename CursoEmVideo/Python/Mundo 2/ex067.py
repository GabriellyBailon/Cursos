#Mostrar a tabuada de qualquer número solicitado e repita até o usuário digitar um número negativo

n = cont = 0;

while True:
    print('*=' * 25);
    n = int(input(f'De qual número você deseja ver a tabuada? '));
    print('*=' * 25);
    if n < 0:
        break;
    while cont <= 10:
        mult = n * cont;
        print(f'{n} x {cont} = {mult}');
        cont += 1;
print('Fim do programa da TABUADA. VOLTE SEMPRE!');


