#Ler um ano e mostrar se ele é bissexto ou não
from datetime import date
#Importa a função que pega a data da máquina que está executando o programa

ano = int(input("Digite o ano que deseja analisar ou digite 0 para analisar o ano atual: "));

if ano == 0:
    ano = date.today().year;
#Se receber 0 como resposta, o ano a ser analisado passa a ser o ano atual

if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
    print(f"O ano de {ano} é bissexto!");
else:
    print(f"O ano de {ano} não é bissexto!")