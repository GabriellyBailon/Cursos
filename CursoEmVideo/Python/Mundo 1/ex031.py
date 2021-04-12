#Ler a distância a ser viajada, se for até 200km, cobrar R$0,50 por km, caso for mais, cobrar R$0,45 a
#cada km

distancia = float(input("Digite a distância a ser percorrida em km: "));

if distancia <= 200.00:
    valor = (distancia * 0.50);
else:
    valor = (distancia * 0.45);

print(f"A sua passagem custará R${valor:.2f}. Boa viagem!");
