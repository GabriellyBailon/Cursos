#Ler a velocidade de um carro, se ele ultrapassar os 80km/h, ele será multado em 7 reais por cada km
#acima do limite. Mostrar o valor da multa ou mensagem de velocidade permitida

velocidade = float(input("Digite a velocidade do carro em km: "));
if velocidade > 80:
    multa = (velocidade - 80) * 7.00;
    print(f"Velocidade acima do permitido (80 km/h)! Sua multa será no valor de R${multa:.2f}.");
else:
    print("Velocidade dentro do permitido. Prossiga com cuidado e boa viagem!");