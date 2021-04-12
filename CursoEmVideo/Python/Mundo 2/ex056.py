#Ler o nome, idade e sexo de 4 pessoas e mostrar no final, a média das idades, o nome do homem mais
#velho e quantas mulheres tem menos de 20 anos

somaidades = 0;
conthomem = 0;
maisvelho = 0;
contmulhermenoridade = 0;
contpessoas = 0;

for c in range(0, 4):
    nome = str(input(f"Digite o nome da {c+1} pessoa: ")).upper().strip();
    idade = int(input("Digite a idade dessa pessoa: "));
    sexo = str(input("Digite M se a pessoa for mulher e H se for homem: ")).upper();
    somaidades = somaidades + idade;
    contpessoas = contpessoas + 1;

    if sexo == "H":                         #DESCOBRINDO HOMEM MAIS VELHO
        conthomem = conthomem + 1;
    if conthomem == 1:
        nome_domaisvelho = nome;
        maisvelho = idade;
    else:
        if maisvelho < idade:
            maisvelho = idade;
            nome_domaisvelho = nome;

    if sexo == "M":                         #DESCOBRINDO QUANTIDADES DE MULHERES COM MENOS DE 20
        if idade < 20:
            contmulhermenoridade = contmulhermenoridade + 1;

media = somaidades / (contpessoas);

print(f"A média das {contpessoas} idades é {media}.");
print(f"O nome do homem mais velho é: {nome_domaisvelho}.");
print(f"E houveram {contmulhermenoridade} mulheres abaixo de 20 anos.");




