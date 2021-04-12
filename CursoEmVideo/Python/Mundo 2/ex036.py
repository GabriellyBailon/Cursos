#Ler o valor da casa, o salário de uma pessoa e em quantos anos ele pretende quitar esse valor,
#o programa aprovará o empréstimo se a parcela não ultrapassar 30% do salário de quem está requisitando

casa = float(input("Qual o valor da casa que deseja financiar? "));
salario = float(input("Qual é o valor do seu salário atual? R$"));
anos = int(input("Em quantos anos planeja pagar esse empréstimo? "));

parcela = casa / (anos * 12);
maximo = (salario / 100) * 30;

if parcela <= maximo:
    print(f"Seu empréstimo foi \033[32mAPROVADO!\033[m Sua parcela será no valor de R${parcela:.2f}");
else:
    print(f"Seu empréstimo foi recusado. Para financiar uma casa de R${casa:.2f}",end=" ");
    #O "end = " "" é de quebra de linha e continuação;
    print(f"A parcela teria o valor de R${parcela:.2f}");


