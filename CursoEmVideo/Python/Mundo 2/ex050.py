#Ler 6 números inteiros e somar apenas os pares desconsiderando ímpares

soma = 0;
contador = 0;

for c in range(0, 6):
    num = int(input(f"Digite o {c+1}° número inteiro: "));
    if num % 2 == 0:
        soma = soma + num;
        contador = contador + 1;

print(f"A soma do(s) {contador} número(s) par(es) é: {soma}");







