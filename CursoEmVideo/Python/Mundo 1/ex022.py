#Ler um nome completo, mostrar ele maiúsculo, minúsculo, contar quantas letras (sem os espaços) e
#contar quantas letras têm o primeiro nome

nome = str(input("Digite um nome: ")).strip();
#O ".strip()" já elimina os espaços laterais, caso algum seja digitado a mais;

maiusculo = nome.upper();
#Coloca tudo em maiúsculo;

minusculo = nome.lower();
#Coloca tudo em minúsculo;

tamanho = len(nome);
#Mostra o tamanho da string;

espaços = nome.count(' ');
#Conta o número de espaços da string;

tamfinal = (tamanho - espaços);
#Calcula o tamanho da string menos a quantidade de espaços;

primeiro = nome.split();
#Divide a string recebida como se fosse uma lista;

contp = len(primeiro[0]);
#Conta quantas letras têm o primeiro nome, ou seja, o item 0 da lista;

print(f"O nome em maiúsculo é: \033[31m{maiusculo}\033[m. \nEm minúsculo fica: \033[33m{minusculo}\033[m.");
print(f"O nome tem \033[30:47m{tamfinal}\033[m letras sendo \033[7:35m{contp}\033[m no primeiro nome.");

