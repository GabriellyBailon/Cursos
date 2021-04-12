#Ler uma medida em metros e devolver em centímetros e milímetros
medida = float(input("Digite o número de metros a serem convertidos: "));
km = (medida/1000);
hm = (medida/100);
dam= (medida/10);
dm = (medida * 10);
cm = (medida * 100);
mm = (medida * 1000);
print(f"Calculando...\n{medida} metros equivalem a:\n{km} km \n{hm} hm \n{dam} dam");
print(f"{dm} dm \n{cm:.0f} cm \n{mm:.0f} mm");
#.0f formata o número com nenhuma casa decimal;