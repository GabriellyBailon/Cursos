#Ler uma quantia em reais e convertê-la em dólares
reais = float(input("Qual a quantidade de reais que você deseja converter? R$"));
dolares = (reais / 5.15);
euro = (reais / 6.04);
iene = (reais * 20);
#Iene está aproximado;
#Cotação do dia 28/07/2020;
print(f"Com R${reais:.2f}, você poderá obter US${dolares:.2f}, EUR${euro:.2f} ou ${iene:.2f} Ienes.");
