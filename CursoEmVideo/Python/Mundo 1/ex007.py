#Ler duas notas e calcular a média

nota1 = float(input("Digite a primeira nota: "));
nota2 = float(input("Digite a segunda nota: "));
#Importante usar float aqui, em notas é comum haver, por exemplo "0.5";

media = (nota1+nota2) / 2;
print(f"A média entre as notas \033[0:33m{nota1:.2f}\033[m e \033[35m{nota2:.2f}\033[m é \033[32m{media:.2f}\033[m.");
