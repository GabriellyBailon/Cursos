#                          Início dos exercícios sobre a parte 2 de LISTAS

# Guardar nomes e pesos numa mesma lista e analisar dados sobre eles

lista = [];
temporaria = [];  # Essa lista vai guardar temporariamente para que consigamos operar com ela
maiorpeso = 0;
menorpeso = 0;

while True:
    nome = str(input("Nome: "));
    temporaria.append(nome);
    peso = int(input("Peso: "));
    temporaria.append(peso);

    if len(lista) == 0:
        maiorpeso = peso;
        menorpeso = peso;
    else:
        if peso > maiorpeso:
            maiorpeso = peso;
        if peso < menorpeso:
            menorpeso = peso;

    lista.append(temporaria[:])  # Aqui criamos uma copia, sem o # se torna uma ligação, o que NÃO QUEREMOS
    temporaria.clear();  # Limpamos a lista temporaria, senão ela adiciona os itens anteriores e os atuais

    opcao = str(input("Você deseja continuar?")).upper().strip()[0];
    if opcao == "N":
        break;

print(f'Foram cadastradas {len(lista)} pessoas');   # Dá o tamanho da lista
print(f'O maior peso cadastrado foi de {maiorpeso} kg de ', end='');
for p in lista:
    if p[1] == maiorpeso:
        print(f'{p[0]} ');
print(f'O menor peso cadastrado foi de {menorpeso} kg de ', end='');
for p in lista:
    if p[1] == menorpeso:
        print(f'{p[0]} ');
