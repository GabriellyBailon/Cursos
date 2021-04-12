algo = input("Digite algo:");
print(f"O que foi digitado é do tipo primitivo {type(algo)}.");
print(f"Isso possui letras e/ou números? {algo.isalnum()}.");
print(f"Isso é composto apenas de letras? {algo.isalpha()}");
print(f"Isso é um ascii? {algo.isascii()}.");
print(f"Isso é decimal? {algo.isdecimal()}.");
print(f"Isso é um número de base 10? {algo.isdigit()}.");
print(f"Isso pode ser utilizado como identificador? {algo.isidentifier()}.");
print(f"Isso é numérico? {algo.isnumeric()}.");
print(f"É possível imprimir isso na tela? {algo.isprintable()}.");
print(f"Isso são espaços em branco? {algo.isspace()}.");
print(f"Isso está em somente em maiúsculas? {algo.isupper()}.");
print(f"Isso está somente em minúsculas? {algo.islower()}.");
print(f"Isso está capitalizado, ou seja, tem a inicial maiúscula e o restante não? {algo.istitle()}.");
#print(f"Isso pode {algo.__init_subclass__()}."); não sei o que esse método faz
print("Ufa, verificação concluída com sucesso!");
