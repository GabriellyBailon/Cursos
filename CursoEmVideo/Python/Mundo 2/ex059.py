#Ler dois números na tela e mostrar um menu de opções, incluindo a de sair do programa

num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));
resposta = 0;

print("=" * 20, "Menu de opções", "=" * 20);

while resposta != 5:
    print('''[1] somar os dois valores
    [2] multiplicar os valores
    [3] indicar o maior valor entre os digitados
    [4] digitar novos números
    [5] sair do programa ''');
    resposta = int(input("Informe a opção desejada: "));
    if resposta == 1:
        soma = num1 + num2;
        print(f"A soma entre os números {num1} e {num2} é igual à {soma}");
    elif resposta == 2:
        mult = num1 * num2;
        print(f"A multiplicação entre os números digitados {num1} e {num2} é igual à {mult}");

    elif resposta == 3:
        if num1 > num2:
            print(f"O maior número entre {num1} e {num2} é {num1}");

        elif num1 == num2:
            print(f"Os números {num1} e {num2} são iguais.");

        else:
            print(f"O maior número entre {num1} e {num2} é {num2}");

    elif resposta == 4:
        print("Insira os novos números: ");
        num1 = int(input("Digite o novo número 1: "));
        num2 = int(input("Digite o novo número 2: "));

    elif resposta == 5:
        print("Fim do programa");
    else:
        print("Opção inválida, tente novamente!");






