# Preencher uma tupla com os 20 participantes do Campeonato Brasileiro e mostrar dados sobre eles

brasileirao2020 = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras',
                   'Vasco da Gama', 'Flamengo', 'Santos', 'Fortaleza',
                   'Fluminense', 'Sport Recife', 'Ceará', 'Grêmio',
                   'Corinthians', 'Atlético-GO', 'Athlético-PR', 'Coritiba',
                   'Bragantino-SP', 'Botafogo', 'Bahia', 'Goiás');

print(f'Os cinco primeiros colocados são: {brasileirao2020[0:5]}');

print(f'\nOs últimos 4 colocados são: {brasileirao2020[-4:]}');


print(f'\nOs times em ordem alfabética ficam: {sorted(brasileirao2020)}');

print(f'O time do Sport está na {brasileirao2020.index("Sport Recife") + 1} posição.');












