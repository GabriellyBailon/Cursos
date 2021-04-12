#Ler o peso e a altura, calcular o IMC e mostrar a faixa que o usuário se encontra

peso = float(input("Digite o seu peso (Kg): "));
altura = float(input("Digite sua altura (m): "));
imc = peso / (altura ** 2);
if imc < 18.5:
    print(f"Seu IMC é igual a {imc:.1f} e indica que você está ABAIXO DO PESO recomendado.");
elif imc < 25:
    print(f"Seu IMC é igual a {imc:.1f} e indica que você está dentro do PESO IDEAL recomendado.");
elif imc < 30:
    print(f"Seu IMC é igual a {imc:.1f} e indica que você está com SOBREPESO, acima do recomendado.");
elif imc < 40:
    print(f"Seu IMC é igual a {imc:.1f} e indica que você está com OBESIDADE, acima do recomendado.");
else:
    print(f"Seu IMC é igual a {imc:.1f} e você está com OBESIDADE MÓRBIDA, acima do peso recomendado.");



