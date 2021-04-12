#Ler cateto oposto e cateto adjacente e mostrar a medida da hipotenusa

from math import sqrt

catetooposto = float(input("Digite a medida do cateto oposto: "));
catetoadj = float(input("Digite a medida do cateto adjacente: "));
hip = sqrt((catetooposto ** 2) + (catetoadj ** 2));
#Possível fazer com "** (1/2) também;
#Ou ainda, importando "hypot" da biblioteca math e implementando ficaria hypot(catetooposto, catetoadj);

print(f"A medida da hipotenusa, com um cateto oposto medindo {catetooposto} e o cateto adjacente medindo {catetoadj} é igual a {hip:.2f}.");
