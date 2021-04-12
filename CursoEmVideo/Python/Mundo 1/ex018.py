#Ler um ângulo e mostrar seu seno, cosseno e tangente
import math
angulo = float(input("Digite o valor do ângulo: "));
#É necessário converter o ângulo para radianos antes de fazer os cálculos
anguloconvert = math.radians(angulo);
seno = math.sin(anguloconvert);
cosseno = math.cos(anguloconvert);
tangente = math.tan(anguloconvert);
#É possível fazer de forma mais direta utilizando por exemplo, seno = math.sin((math.radians (angulo));
print(f"O seno de {angulo}° é {seno:.2f}.\nO cosseno de {angulo}° é {cosseno:.2f}.\nA tangente de {angulo}° é {tangente:.2f}.");


