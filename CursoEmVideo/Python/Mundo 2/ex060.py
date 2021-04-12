#Ler um número e fazer seu fatorial

'''fat = int(input("Digite um número e descubra seu fatorial: "));
fatorial = 1;
print(f"O valor do fatorial de {fat}! é = {fat} x ", end='');

while not (fat == 1):
    fatorial *= fat;
    fat = fat - 1;

    if fat == 1:
        print(fat, end='');
    else:
        print(fat, end=' x ');


print(" =", fatorial);'''

#Fazer com o "for"
print("=*" * 20);

fat = int(input("Digite um número inteiro e saiba seu fatorial: "));
fatorial = 1;
print(f"O fatorial de {fat}! é = ", end='');
for c in range(fat, 0, -1):
    if c == 1:
        print(c, "= ", end='');
    else:
        print(c, end=' x ');

    fatorial = fatorial * c;

print(fatorial);









