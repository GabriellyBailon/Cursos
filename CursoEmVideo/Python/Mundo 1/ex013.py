#Ler o salário de um funcionário, calculá-lo com um acréscimo de 15% e mostrar na tela
salario = float(input("Digite o valor do salário: R$"));
aumento = (salario/100) * 15;
novosalario= salario + aumento;
print(f"O salário antigo era de R${salario:.2f}, agora com o aumento de 15%, passará ao valor de R${novosalario:.2f}");