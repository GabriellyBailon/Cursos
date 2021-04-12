#Ler o preço de um produto e calculá-lo com 5% de desconto
preco = float(input("Digite o valor do produto: R$"));
desc = (preco/100) * 5;
novopreco = preco - desc;
prazo= preco + (preco/100*8);
#Cálculo do produto à prazo com 8% de acréscimo;
print(f"O produto custava R${preco:.2f}, agora com desconto passou a custar R${novopreco:.2f}.");
print(f"Já à prazo, o valor do produto passa a ser R${prazo:.2f}.");
