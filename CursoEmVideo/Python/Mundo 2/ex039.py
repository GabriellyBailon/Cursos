#Ler o ano de nascimento de um jovem e verificar se ele está na hora de alistar, se está muito cedo
#para isso ou já passou do momento certo
from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: "));
sexo = str(input("Você é homem ou mulher? Digite H para homem e M se for mulher: ")).upper().strip();

atual = date.today().year;
idade = (atual - nascimento);
if sexo == "H":
    if idade < 18:
        print(f"Você ainda tem \033[1:38m{idade}\033[m anos, ainda não está na hora de se alistar.  Faltam \033[1:39m{18-idade}\033[m anos.");
        print(f"Você deve se alistar em {nascimento + 18}")
    elif idade == 18:
        print(f"Você já tem \033[1:35m{idade}\033[m anos, chegou a hora! Aliste-se!");
    elif idade > 18:
        print(f"Você tem \033[1:34m{idade}\033[m anos, seu alistamento foi em \033[1:31m{nascimento + 18}\033[m. Verifique sua situação e caso necessário, regularize-a o mais rápido possível.");
else:
    print("Como você é uma mulher, não precisa se alistar.");


