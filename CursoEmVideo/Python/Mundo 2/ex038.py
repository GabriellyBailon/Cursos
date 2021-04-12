#Ler dois números inteiros, compará-los e dizer qual o menor e qual o maior

num1 = int(input("Digite um número inteiro: "));
num2 = int(input("Digite outro número inteiro: "));

if num1 > num2:
    print("O PRIMEIRO número é MAIOR!");
elif num2 > num1:
    print("O SEGUNDO número é MAIOR!");
else:
    print(f"Os números digitados {num1} e {num2} são iguais.")