#Ler a opção do usuário e "jogar" pedra, papel, tesoura "com" ele

from random import choice

print("-=" * 10,"Vamos jogar PEDRA PAPEL TESOURA!", "-=" * 10);
usuario = str(input("Sua vez! Digite PEDRA PAPEL ou TESOURA: ")).upper().strip();
jogadas = ['PEDRA','PAPEL','TESOURA'];
pc = choice(jogadas);
if usuario == pc:
    print(f"Empate! O usuário escolheu {usuario} e o computador {pc}!"); #Empate
elif (usuario == "PEDRA" and pc == "TESOURA") or (usuario == "PAPEL" and pc == "PEDRA") or (usuario == "TESOURA" and pc == "PAPEL"): #Jogador vence
    print(f"Você ganhou!!! Você jogou {usuario} e o computador jogou {pc}!");
elif (pc == "PEDRA" and usuario == "TESOURA") or (pc == "PAPEL" and usuario == "PEDRA") or (pc == "TESOURA" and usuario == "PAPEL"): #Computador vence
    print(f"O computador venceu! Você jogou {usuario} e o computador jogou {pc}!");
else:   #Opção que não existe
    print("Ops, opção inválida. Tente novamente!");





