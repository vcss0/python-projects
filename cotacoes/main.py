import PySimpleGUI as sg
import cotacao


class Cotacao_moedas:
    def __init__(self) -> None:
        self.theme = sg.theme('LightBrown10')

        self.layout = [
            [sg.Text('Qual cotação deseja verificar?')],
            [sg.Button('Dolar - Real'), sg.Button('Euro - Real'),
             sg.Button('BitCoin - Real')],
            [sg.HSeparator()],
            [sg.Text(''), sg.Text(key='VerCotacao')],

        ]

        self.window = window = sg.Window('Cotacoes | 1.0', self.layout)

        while True:
            event, self.values = window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 'Dolar - Real':
                resultado = cotacao.verifica_cotacao(event)
                window['VerCotacao'].Update(
                    f'Cotação atual {event}: {resultado}')

            elif event == 'Euro - Real':
                resultado = cotacao.verifica_cotacao(event)
                window['VerCotacao'].Update(
                    f'Cotação atual {event}: {resultado}')

            elif event == 'BitCoin - Real':
                resultado = cotacao.verifica_cotacao(event)
                window['VerCotacao'].Update(
                    f'Cotação atual {event}: {resultado}')


Cotacao_moedas()
