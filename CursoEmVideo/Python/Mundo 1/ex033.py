#Ler 3 números e mostrar quem é o maior e o menor

primeiro = int(input("Digite o primeiro número: "));
segundo = int(input("Digite o segundo número: "));
terceiro = int(input("Digite o terceiro número: "));

menor = primeiro;
maior = primeiro;

if segundo < menor:
    menor = segundo;
if terceiro < menor:
    menor = terceiro;
#Calcula o menor;

if segundo > maior:
    maior = segundo;
if terceiro > maior:
    maior = terceiro;
#Calcula o maior;

print(f"O menor número digitado foi {menor}.\nO maior número digitado foi {maior}.");


