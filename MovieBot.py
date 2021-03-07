import requests
import json
import datetime
import urllib
import telepot
import locale

bot = telepot.Bot('1682510966:AAHLZWvkjvV90g3q9CvSKM5IygkAB5z0RNA')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def requisicao(titulo):
    try:
        req = requests.get(
            'https://api.themoviedb.org/3/search/movie?&language=pt-BR&api_key=b3a156870abcdcfc2c7515e1950f5fea&query=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None


def Receive_msg(msg):
    print(msg['chat']['id'])
    print(msg['text'])
    print(msg['chat']['first_name'])
    print(msg)

    bot.sendMessage(msg['chat']['id'], "Olá " + msg['chat']['first_name'])
    bot.sendMessage(msg['chat']['id'],
                    "Bem vindo ao BOT Oráculo do Cinema!\nDigite o Título do Filme que deseja informação:")

    filme = requisicao(msg['text'])
    print("Total de resultados: " + str(filme['total_results']))
    total_result = filme['total_results']
    for i in range(1, total_result):
        print(i)

        bot.sendMessage(msg['chat']['id'], filme(['results'][i]))
    return None


##bot2.message_loop(start,5)
bot.message_loop(Receive_msg, 5)
# response = bot2.getUpdates()
# Receive_msg(response)
while True:
    pass
