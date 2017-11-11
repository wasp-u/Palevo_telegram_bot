# -*- coding: utf-8 -*-
import config
import telebot
import selenium_uz
import uz




bot = telebot.TeleBot(config.token)
global s
s=False
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['monitoring'])
def monitoring(message):
    bot.send_message(message.chat.id, message.text)
    try:
        global ticket
        ticket = selenium_uz.BoockTicket("Киев", "Львов","2", type='П', train="099 К")

        place_number = ticket.place_number

        bot.send_message(message.chat.id, "Ticket was booked")
        bot.send_message(message.chat.id, 'Place number is: '+place_number)

    except:
        bot.send_message(message.chat.id, "Ошибка")

@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.send_message(message.chat.id, "cancel")
    global ticket
    try:
        ticket.cancel_booking()
    except:
        bot.send_message(message.chat.id, "Ошибка")


@bot.message_handler(commands=['search'])
def search(message):
    global s
    s = True
    msg = bot.send_message(message.chat.id, "Input station from")
    bot.register_next_step_handler(msg, select_station_from)

    # stations = uz.get_staton_by_name(message.text)
    #
    # keyboard = telebot.types.InlineKeyboardMarkup()
    # for station in stations:
    #     callback_button = telebot.types.InlineKeyboardButton(text=station[0], callback_data=station[1])
    #     keyboard.add(callback_button)
    # bot.send_message(message.chat.id, "asdf", reply_markup=keyboard)

    # uz.get_staton_by_name()
    # bot.send_message(message.chat.id, "cancel")
    # global ticket
    # try:
    #     ticket.cancel_booking()
    # except:
    #     bot.send_message(message.chat.id, "Ошибка")

# @bot.message_handler(func=lambda message: s,
#                      content_types=['text'])

def select_station_from(message):
    # global s
    # s = False
    stations = uz.get_staton_by_name(message.text)

    keyboard = telebot.types.InlineKeyboardMarkup()
    for station in stations:
        callback_button = telebot.types.InlineKeyboardButton(text=station[0], callback_data=station[1])
        keyboard.add(callback_button)
    bot.send_message(message.chat.id, "================", reply_markup=keyboard)

    # bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # pass
    # Если сообщение из чата с ботом
    # print(call.callback)
    if call.message:
        bot.send_message(call.message.chat.id,text=call.data)
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
