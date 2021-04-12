#Ler o primeiro termo e a razão de uma PA e mostrar os seus 10 primeiros termos

primeiro = int(input("Digite o primeiro termo da PA: "));
razao = int(input("Agora, digite a razão da sua PA: "));
print(primeiro, end=' ');

pa = primeiro;

for c in range(0, 9):
    pa = pa + razao;
    print(pa, end=' ');

#Solução do vídeo (";" não inseridos lá), solução mais otimizada
Primeiro = int(input("Primeiro termo: "));
razão = int(input("Razão: "));
décimo = Primeiro + ((10 - 1) * razão);
for c in range(Primeiro, décimo + razão, razão):
    print(c, end=' ');
print("ACABOU");




