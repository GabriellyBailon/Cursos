#Ler uma frase, contar quantas letras "a" ela tem e mostrar a posição
#da primeira e a última ocorrência do "a"

frase = str(input("Digite uma frase: ")).strip().upper();
#Importante usar o ".strip()" para garantir erros de excesso de espaço e o upper para garantir que
#todas os "A"s sejam analisados

conta = frase.count('A');
primeiroa = frase.find('A');
ultimoa = frase.rfind('A');

print(f"A frase digitada tem {conta} letras a.");
print(f"O primeiro a está na posição {(primeiroa)+1} da frase.");
#Colocar o "+1" para deixar a posição em números como 1°, 2°, 3°...;
print(f"E o último a está na posição {(ultimoa)+1} da frase.");
