#Ler duas notas, calcular a média e mostrar se o aluno foi aprovado, reprovado ou ficou de recuperação

nota1 = float(input("Digite a primeira nota: "));
nota2 = float(input("Digite a segunda nota: "));
media = (nota1 + nota2) / 2;

if media <= 5.0:
    print(f"A sua média foi de \033[31m{media:.2f}\033[m pontos. Você foi reprovado, estude mais na próxima!");
elif (media > 5) and (media <= 6.9):
    print(f"A sua média foi \033[33m{media:.2f}\033[m. Você está de recuperação, estude para a prova!");
else:
    print(f"Parabéns! Você foi aprovado! Sua média foi de \033[34m{media:.2f}\033[m pontos!")
