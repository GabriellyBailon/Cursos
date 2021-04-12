#Ler o nome de uma cidade e ver se esse se inicia com "SANTO"

cidade = str(input("Digite o nome da cidade: "));
print("O nome da cidade começa com a palavra SANTO?");
dividir = cidade.split();
#Divide o nome da cidade para a análise;

analisar = dividir[0].upper();
#Deixa tudo em maiúsculas para facilitar a procura;

print('SANTO' == analisar);
#Procura se há ocorrência da palavra, com o "==" garante que alguns erros não ocorram;

#Outra opção é usar ".find";

