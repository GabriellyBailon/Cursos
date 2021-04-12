#Ler o nome de uma pessoa e mostrar o primeiro e o último nome

nome = str(input("Digite seu nome: ")).strip().split();

quantidadenomes = len(nome);
#Conta quantos nomes foram digitados, o ".split()" faz a lista observando os espaços entre as palavras;

primeironome = nome[0];
#Item 0 da lista, o primeiro;

print(f"O primeiro nome digitado foi: {primeironome}. \nJá o último foi: {nome[quantidadenomes - 1]}");
#A lista se inicia pelo item 0, então o último item da lista será o número total de nomes -1;