#Ler um número, mostrar seu antecessor e sucessor
n = int(input("Digite um número:"));
antecessor = n - 1;
sucessor = n + 1;
print(f"O número digitado foi {n:^10}.\nO sucessor dele é {sucessor} e seu antecessor é {antecessor}.");
#Segundo modo:
#print(f"O número digitado foi {n}. Seu sucessor é {(n+1)} e seu antecessor é {n-1}.");

