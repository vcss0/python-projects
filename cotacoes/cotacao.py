import requests
import json


def verifica_cotacao(moeda):
    cotacao = requests.get(
        "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    if moeda == 'Dolar - Real':
       return converte(cotacao['USDBRL']['bid'])
    elif moeda == 'Euro - Real':
        return converte(cotacao['EURBRL']['bid'])
    elif moeda == 'BitCoin - Real':

        return converte(float(cotacao['BTCBRL']['bid'])*1000
)
def calculo():
    pass


def converte(moeda):
    moeda = float(moeda)
    return f'{moeda:.2f}'


print(verifica_cotacao('Dolar - Real'))



