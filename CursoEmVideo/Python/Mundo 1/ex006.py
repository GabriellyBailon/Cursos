#Ler um número e mostrar seu dobro, triplo e raíz quadrada
n= int(input("Digite um número:"));
dobro = n * 2;
triplo = n * 3;
rq = n ** (1/2);
print(f"O número digitado foi {n}. Seu dobro é {dobro}, seu triplo é {triplo} e a raíz quadrada dele é {rq:.2f}.")


