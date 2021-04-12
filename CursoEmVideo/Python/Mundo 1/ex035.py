#Ler a medida das 3 retas de um triângulo e verificar se sua condição de existência é verdadeira

reta1 = float(input("Digite o valor da primeira reta: "));
reta2 = float(input("Digite o valor da segunda reta: "));
reta3 = float(input("Digite o valor da terceira reta: "));

if (reta1 < (reta2 + reta3)) and (reta2 < (reta1 + reta3)) and (reta3 < (reta1 + reta2)):
    print("Os comprimentos das retas acima PODEM SIM formar um triângulo!");
else:
    print("Os comprimentos das retas acima NÃO PODEM formar um triângulo!");


