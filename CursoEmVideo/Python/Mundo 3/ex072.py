                                        # INÍCIO EXERCÍCIOS TUPLAS

# Usando tuplas, fazer um programa que leia um número de 0 a 20 e escreva-o por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte');

print('Digite um número entre 0 e 20 e veja-o por extenso!');
while True:
    while True:
        usuario = int(input('Qual número você deseja ver? '));
        if usuario >= 0 and usuario <= 20:
            break;
        else:
            print("Tente novamente.", end=' ');

    print(f'Você digitou o número {numeros[usuario]}.');

    opcao = ' ';
    while opcao not in 'SN':
        opcao = str(input("Deseja continuar? [S/N] ")).strip().upper();
    if opcao == 'N':
        break;

print("Fim do programa.");








