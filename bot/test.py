import requests
import telebot
url = "https://api.telegram.org/bot487787232:AAFtlqRRvLuugfpDIbiDLLnqVDd6j0nQzag/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    print(response.json())
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1

    if len(results) > 0:
        last_update = results[-1]
    else:
        last_update = results[len(results)]
    return last_update

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Your message goes here')

