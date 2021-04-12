#Apresentar os números pares que estão no intervalo de 1 a 50

#Solução mais otimizada:
for cont in range(2, 51, 2):
    print(cont, end=' ');

#Solução possível mas, menos otimizada, faz o dobro de laços:
#for cont in range(1, 51, 1):
#   if cont % 2 == 0:
#       print(cont, end=' ');

