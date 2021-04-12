#Ler um salário e calular o aumento, se o salário for menor ou até 1250, o aumento será de 15%, se for
#maior que esse valor, aumento de 10%

salario = float(input("Digite o valor do salário atual: R$"));

if salario <= 1250.00:
    aumento = salario + ((salario / 100) * 15);
else:
    aumento = salario + ((salario / 100) * 10);

print(f"O salário atual de \033[30mR${salario:.2f}\033[m com o aumento, passa ao valor de \033[32mR${aumento:.2f}\033[m");

