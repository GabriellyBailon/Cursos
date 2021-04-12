#Mostrar a soma dos múltiplos inteiros de 3 que existem entre 1 e 500

soma = 0;
cont = 0;
for c in range(3, 501, 6):
        soma = soma + c;
        cont = cont + 1;
print(f"A soma desses {cont} números múltiplos de 3, é igual à {soma}");

#Realizando o laço com incrementação 3, se nota um padrão de que os números necessários crescem de 6
#em 6, o que demonstra que inserir essa informação no laço diretamente otimiza o código;



