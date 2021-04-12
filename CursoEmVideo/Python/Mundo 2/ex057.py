#Ler a informação sobre o sexo do usuário e não aceitar enquanto não for digitada uma opção válida

sexo = str(input("Informe seu sexo (M/F): ")).strip()[0];
                                        #O zero pega faz a variável pegar somente a primeira letra

while sexo not in "MmFf":
    print("Dados inválidos. Digite novamente")
    sexo = str(input("Informe seu sexo (M/F): ")).strip()[0];

print("O sexo informado foi registrado com sucesso.");



