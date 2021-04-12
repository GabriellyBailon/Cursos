#Ler o valor da compra e o modo de pagamento
print("=" * 10, "LOJAS BAILON", "=" * 10);
valor = float(input("Digite o valor da compra: R$"));
print ('''Qual será o meio de pagamento?
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] em 3x ou mais no cartão''');
resposta = int(input("Sua opção: "));
if resposta == 1:
    total = valor - ((valor / 100) * 10);
    print(f"O valor de R${valor:.2f} à vista fica R${total:.2f}");
elif resposta == 2:
    total = valor - ((valor/100) * 5);
    print(f"O valor de R${valor:.2f} à vista no cartão fica R${total:.2f}");
elif resposta == 3:
    print(f"O valor de R${valor:.2f} em 2x no cartão não sofre alteração, continua R${valor:.2f}")
elif resposta == 4:
    parcelas = int(input("Em quantas parcelas? "));
    total = valor + ((valor / 100) * 20);
    print(f"O valor de R${valor:.2f} em {parcelas}x no cartão, gera {parcelas} parcelas de R${(total / parcelas):.2f} e um total de R${total:.2f}");
else:
    print("Opção inválida! Tente novamente.");






