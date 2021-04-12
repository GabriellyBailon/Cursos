#Ler um nome e verificar se nele há a palavra "SILVA"

nome = str(input("Digite o nome: ")).strip().upper().split();
#Retira os espaços excedentes, divide e deixa tudo maiúsculo para facilitar a análise;

print("O nome digitado possui a palavra Silva?");
print("SILVA" in nome);

