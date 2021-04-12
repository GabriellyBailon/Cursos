#Ler números até quando o usuário desejar e mostrar a média, o menor e o maior entre eles

opção = '';
soma = cont = 0;

while opção != "N":
    num = int(input('Digite um número: '));
    soma = soma + num;
    cont += 1;
    opção = str(input("Deseja ler mais números?[Digite S para continuar e N para parar] ")).upper().strip()[0];

    if cont == 1:
        maior = num;
        menor = num;
    else:
        if num > maior:
            maior = num;
        elif num < menor:
            menor = num;

media = soma / cont;
print(f'A media entre os {cont} números inseridos foi {media}');
print(f'E o maior número foi {maior} e o menor {menor}');


