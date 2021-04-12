#Ler uma frase e descobrir se ela é um palíndromo

frase = str(input("Digite a frase e descubra se ela é um palíndromo: ")).strip().upper().split();
junto = ''.join(frase);             #"Junta" as palavras e não coloca nada entre elas
inverso = '';

for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra];
print(f"O inverso de {junto} é {inverso}.");
if inverso == junto:
    print("TEMOS um PALÍNDROMO!");
else:
    print("NÃO temos um PALÍNDROMO!");

#Ainda é possível (no Python) usar a função de fatiamento [::-1] para encontrar e guardar o inverso
#da variável junto;














