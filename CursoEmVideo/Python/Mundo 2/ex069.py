#Cadastrar nome e sexo de várias pessoas até o usuário decidir parar e depois apresentar informações
#sobre os dados inseridos

contidade = contmasculino = contmulher = 0;

while True:
    idade = int(input('Qual a idade da pessoa a ser cadastrada? '));

    sexo = ' ';
    while sexo not in "MF":
        sexo = str(input('Qual o sexo? (F/M): ')).strip().upper()[0];
    if idade > 18:
        contidade += 1;
    if sexo == "M":
        contmasculino += 1;
    if sexo == "F" and idade < 20:
        contmulher += 1;

        opcao = ' ';
        while opcao not in "SN":
            opcao = str(input('Deseja continuar? (S/N) ')).strip().upper()[0];
    if opcao == "N":
        break;

print(f'Cadastro realizado!\nForam cadastradas {contidade} pessoas com mais de 18 anos,', end =' ');
print(f'{contmasculino} homens e {contmulher} mulheres com menos de 21 anos.');






