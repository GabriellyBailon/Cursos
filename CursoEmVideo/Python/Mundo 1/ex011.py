#Receber altura e largura de uma parede, mostrar sua área e dizer quantos litros de tinta serão necessários para pintar
altura = float(input("Digite a altura: "));
largura = float(input("Digite a largura: "));
area = (altura * largura);
tinta= (area/2);
print(f"A área de {altura} x {largura} calculada foi igual a {area} metros quadrados.");
print(f"Serão necessários {tinta:.2f} latas de tinta para pintar essa superfície.");
