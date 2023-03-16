import PySimpleGUI as sg
import random

#(Escolhendo Aleatorio Filme - Dicionario)
eafd = {'1960':['The Great Escape', 'What Ever Happened to Baby Jane?', 'For a Few Dollars More', 'Night of the Living Dead', 'Psycho', 'Harakiri', 'The Good, the Bad and the Ugly', 'Eyes Without a Face']
    , '1970':['Alien', 'Blazing Saddles', 'Taxi Driver', 'The Godfather', 'Stalker', 'Jaws', 'The Exorcist', 'A Clockwork Orange']
    , '1980':['Beetlejuice', 'An American Werewolf in London', 'The Thing', 'Scarface', 'The Color Purple', 'The Shining', 'Apocalypse Now', 'Once Upon a Time in America']
    , '1990':['Malcolm X', 'Se7en', 'Heat', 'The Devils Advocate', 'Perfect Blue', 'Misery', 'Schindlers List', 'GoodFellas']
    , '2000':['Office Space', 'No Country for Old Men', 'Watchmen', 'Who Am I', 'The Conjuring', 'Into the Wild', 'The Imitation Game', 'Get Out']}

# Escolhendo uma chave aleatória do dicionário
Ano_Aleatorio = random.choice(list(eafd.keys()))

# Escolhendo um conteúdo aleatório da lista correspondente à chave aleatória
Filme_Aleatorio = random.choice(eafd[Ano_Aleatorio])


#layout
sg.theme('LightBrown13')
layout = [
    [sg.Text(f'O Ano escolhido foi {Ano_Aleatorio} e o Filme escolhido foi {Filme_Aleatorio}')],
    [sg.Button('Aleatorizar')]
]
# Janela
janela = sg.Window('Escolhendo Filmes', layout)
# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Aleatorizar':
        
        Ano_Aleatorio = random.choice(list(eafd.keys()))
        Filme_Aleatorio = random.choice(eafd[Ano_Aleatorio])
        # layout
        sg.theme('LightBrown13')
        layout = [
            [sg.Text(f'O Ano escolhido foi {Ano_Aleatorio} e o Filme escolhido foi {Filme_Aleatorio}')],
            [sg.Button('Aleatorizar')]
        ]
        # Janela
        janela = sg.Window('Escolhendo Filmes', layout)