#Ler um número inteiro e convertê-lo em binário, octal ou hexadecimal

num = int(input("Digite um número: "));

print('''Digite a opção desejada para a conversão do número:)
[1] para binário \n[2] para octal \n[3] para hexadecimal''');
#3 vírgulas são usadas para digitar um texto maior;

resposta = int(input("A opção desejada é: "));

if resposta == 1:
    print(f"Em base BINÁRIA, o número será: {bin(num)[2:]}");
elif resposta == 2:
    print(f"Em base OCTAL, o número será: {oct(num)[2:]}");
elif resposta == 3:
    print(f"Em base HEXADECIMAL, o número será: {hex(num)[2:]}");
#Usado o "[2:]" pois o Python mostra 2 caractéres no início para indicar qual a base da conversão
#e para o usuário isso não é necessário, então não mostramos no print (conceito de fatiamento);
else:
    print("Opção inválida. Tente novamente.");




