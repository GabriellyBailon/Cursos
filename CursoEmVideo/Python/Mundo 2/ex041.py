#Ler a idade e mostrar em qual categoria o nadador se encaixa

from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: "));
atual = date.today().year;
idade = (atual - nascimento);

if idade <= 9:
    print(f"Você tem \033[32m{idade}\033[m anos e você é considerado um nadador da categoria \033[32mMIRIM\033[m!");
elif (idade > 9) and (idade <= 14):
    print(f"Você tem \033[33m{idade}\033[m anos e você é considerado um nadador da categoria \033[33mINFANTIL\033[m!");
elif (idade > 14) and (idade <= 19):
    print(f"Você tem \033[34m{idade}\033[m anos e você é considerado um nadador da categoria \033[34mJÚNIOR\033[m!");
elif (idade > 19) and (idade <= 25):
    print(f"Você tem \033[35m{idade}\033[m anos e você é considerado um nadador da categoria \033[35mSÊNIOR\033[m!");
else:
    print(f"Você tem \033[36m{idade}\033[m anos e você é considerado um nadador da categoria \033[36mMASTER\033[m!");
