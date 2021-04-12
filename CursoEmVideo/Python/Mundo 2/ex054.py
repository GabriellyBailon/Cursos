#Ler o ano de nascimento de 7 pessoas, mostrar quantas são maiores de 21 anos e quantas ainda não
from datetime import date

atual = date.today().year;
jovem = 0;
maior = 0;
for c in range(0, 7):
    ano = int(input(f"Em que ano a {c+1}° nasceu? "));
    if (atual - ano) >= 21:
        jovem += 1;
    else:
        maior += 1;
print(f"{jovem} pessoa(s) tem 21 anos ou mais.\nE {maior} pessoas tem menos de 21 anos.");
