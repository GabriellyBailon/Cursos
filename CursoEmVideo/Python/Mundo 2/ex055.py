#Ler o peso de 5 pessoas e no final, mostrar qual o menor e o maior peso lidos

for c in range(0, 5):
    peso = float(input(f"Digite o peso da {c + 1}° pessoa (Kg): "));
    if c == 0:      #Acontece se for a primeira ocorrência do/da laço/verificação
        maior = peso;
        menor = peso;
    else:
        if peso > maior:
            maior = peso;
        if peso < menor:
            menor = peso;
print(f"O maior peso encontrado foi {maior}Kg e o menor foi {menor}Kg");


