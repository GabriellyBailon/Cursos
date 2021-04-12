#Assim como no ex035, ler 3 segmentos de reta, mostrar se é possível obter um triângulo com eles
#e nesse aqui, demonstrar se esse triângulo será equilátero, isóceles ou escaleno

reta1 = float(input("Tamanho da primeira reta: "));
reta2 = float(input("Tamanho da segunda reta: "));
reta3 = float(input("Tamanho da terceira reta: "));

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print("Os valores digitados podem sim formar um triângilo!");
    if reta1 == reta2 == reta3:
        print("E o triângulo formado por eles é EQUILÁTERO!");
    elif (reta1 != reta2 != reta3) and (reta1 != reta3):
        print("E o triângulo formado por eles é ESCALENO!");
    else:
        print("E o triângulo formado por eles é ISÓCELES!");
else:
    print("Com esses valores de retas, não foi possível gerar um triângulo!");









