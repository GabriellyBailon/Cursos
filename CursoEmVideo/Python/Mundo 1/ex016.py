#Ler um número e mostrar sua parte inteira
from math import trunc
num = float(input("Digite um número: "));
print(f"A parte inteira do número {num} é {trunc(num)}.");

#Outros modos:
'''import math
num = float(input("Digite um número: "));
print(f"A parte inteira do número {num} é {math.trunc(num)}."); 
'''

'''num = float (input("Digite um número: ");
print(f"A parte inteira do número {num} é {int(num)}");
'''
