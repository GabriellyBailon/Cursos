km = float(input("Digite a quantidade de km rodados: "));
dias = int(input("Digite a quantidade de dias em que carro foi alugado:"));
valor = ((0.15 * km) + (60 * dias));
print(f"O valor a ser pago pelos {dias} dias e {km}km é R${valor:.2f}");

