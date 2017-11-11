
# -*- coding: utf-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot("488787929:AAG_tytXMIWNgdXgiS5Gq5bftWfEOW14vtA")

# @bot.message_handler(func = lambda message: 't' in message.text)
# def handler_soccer(message):
#
#     keyboard = types.InlineKeyboardMarkup()
#     url_button1 = types.InlineKeyboardButton(text="1")
#     url_button2 = types.InlineKeyboardButton(text="2")
#     keyboard.add(url_button1,url_button2)
#     # bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)
#
#     bot.send_message(message.chat.id,'dsfgsdf', parse_mode = 'Markdown', reply_markup = keyboard)


@bot.message_handler(commands=["start"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1curse = types.KeyboardButton(text="1 Курс")
    button_2curse = types.KeyboardButton(text="2 Курс")
    button_3curse = types.KeyboardButton(text="3 Курс")
    button_4curse = types.KeyboardButton(text="4 Курс")
    keyboard.add(button_1curse, button_2curse,button_3curse, button_4curse)
    bot.send_message(message.chat.id, "kek", reply_markup=keyboard)

@bot.message_handler(func = lambda message: '1 Курс' in message.text)
def curse1(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    url_button1 = types.KeyboardButton(text="Перейти на 1 семестр")
    url_button2 = types.KeyboardButton(text="Перейти на 2 семестр")
    keyboard.add(url_button1,url_button2)
    bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)

# @bot.message_handler(func = lambda message: '2 Курс' in message.text)
# def curse2(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button1 = types.InlineKeyboardButton(text="Перейти на 3 семестр", url="https://drive.google.com/drive/folders/0B3X-aNp1PbmXci0zdFJHNDlkWTA")
#     url_button2 = types.InlineKeyboardButton(text="Перейти на 4 семестр", url="https://drive.google.com/drive/folders/0BwaacHCmP7LAV1hTcHlydVhadlE")
#     keyboard.add(url_button1,url_button2)
#     bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)
#
# @bot.message_handler(func = lambda message: '3 Курс' in message.text)
# def curse2(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button1 = types.InlineKeyboardButton(text="Перейти на 5 семестр", url="https://drive.google.com/drive/u/0/folders/0B9qN1T1nMz9FSHRtRjBFcFhUaVU")
#     url_button2 = types.InlineKeyboardButton(text="Перейти на 6 семестр", url="https://drive.google.com/drive/folders/0B8cYxZLGIxRQUXRpX0hZVTJ1Zjg")
#     keyboard.add(url_button1,url_button2)
#     bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)
#
# @bot.message_handler(func = lambda message: '4 Курс' in message.text)
# def curse2(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button1 = types.InlineKeyboardButton(text="Перейти на 7 семестр", url="https://drive.google.com/drive/u/0/folders/0B-O4veK6VCAufkhvci1Yb0M5MUtwTUlpcjUzd1dhTHJxb3FDRExsVHUwOE1HRGpXZmlnVnc")
#     url_button2 = types.InlineKeyboardButton(text="Перейти на 8 семестр", url="https://drive.google.com/drive/u/0/folders/0B1YnwwOvhsXHb3FsY3pLWjBBRDA")
#     keyboard.add(url_button1,url_button2)
#     bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling(none_stop=True)
