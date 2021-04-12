#Ler um número de 0 a 9999 e dizer quantas unidades, dezenas, centenas e milhares ele tem

num = int(input("Digite um número: "));
unidades = num // 1 % 10;
dezenas = num // 10 % 10;
centenas = num // 100 % 10;
milhares = num // 1000 % 10;
#Aqui, dividimos a parte inteira por 1, 10, 100 ou 1000 e logo após fazemos seu módulo por 10;

print(f"O número digitado foi: {num}");

print(f"Ele tem {unidades} unidades \n{dezenas} dezenas \n{centenas} centenas \n{milhares} milhar(es)");