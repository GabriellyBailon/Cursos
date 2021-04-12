# "Jogar" par ou ímpar com o usuário até ele perder e mostrar quantas vitórias consecutivas houveram

from random import randint

cont = 0;

while True:
    print("*=" * 15);
    print('Vamos jogar PAR OU ÍMPAR!');
    print("*=" * 15);
    opcao = False;

    while opcao == False:  #Laço para conferir se a opção digitada é válida
        usuario = str(input('Sua vez! Você quer PAR ou IMPAR?(ESCREVA SEM ACENTOS) ')).strip().upper();
        if usuario == "PAR" or usuario == "IMPAR":
            opcao = True;

    if usuario == "PAR":
        computador = "IMPAR";
    elif usuario == "IMPAR":
        computador = "PAR";

    num1 = int(input("Vamos lá! Digite um número entre 0 e 10! "));
    num2 = randint(0, 10);

    soma = num1 + num2;

    if ((soma % 2 == 0) and (usuario == "PAR")) or ((soma % 2 != 0) and (usuario == "IMPAR")):
        cont += 1;
        print(
            f"Boooa, VOCÊ venceu! Você escolheu {num1} e o computador {num2}\nA soma foi {soma} e o resultado foi {usuario}!");
    else:
        break;

print(
    f'Vitória do COMPUTADOR! Você escolheu {num1} e o computador {num2}\nA soma foi {soma} e o resultado foi {computador}!');
print(f'FIM DE JOGO. Você ganhou {cont} vezes consecutivas!');
