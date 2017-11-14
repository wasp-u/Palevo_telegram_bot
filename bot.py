
# -*- coding: utf-8 -*-
# ver 1.0.0

import telebot
from telebot import types

bot = telebot.TeleBot("488787929:AAG_tytXMIWNgdXgiS5Gq5bftWfEOW14vtA")

start_letter = "Цей бот створений для потоку ІО/ІВ. Тут ви зможете знайти  'палєво' по команді /palevo. Також дізнатися по яким предметам у вас будуть заліки /credits або екзамени /exams. Якщо ти староста, то в тебе є можливість додати студентів до 'білого списку бота', тобто надати доступ студентам групи до бота. Це можна зробити по команді /append_students_list ."

# value - url;  key - curse;
palevo_bot_urls = {1:("https://drive.google.com/drive/u/0/folders/0B0BNlrWqUEvVRHhXTVMwY3BORDA","https://drive.google.com/drive/folders/0B0vn58kzRhxpU0lwWFlQcUxYeWs"),
               2:("https://drive.google.com/drive/folders/0B3X-aNp1PbmXci0zdFJHNDlkWTA","https://drive.google.com/drive/folders/0BwaacHCmP7LAV1hTcHlydVhadlE"),
               3:("https://drive.google.com/drive/u/0/folders/0B9qN1T1nMz9FSHRtRjBFcFhUaVU","https://drive.google.com/drive/folders/0B8cYxZLGIxRQUXRpX0hZVTJ1Zjg"),
               4:("https://drive.google.com/drive/u/0/folders/0B-O4veK6VCAufkhvci1Yb0M5MUtwTUlpcjUzd1dhTHJxb3FDRExsVHUwOE1HRGpXZmlnVnc","https://drive.google.com/drive/u/0/folders/0B1YnwwOvhsXHb3FsY3pLWjBBRDA")}

# value - exams;  key - curse;
palevo_bot_exams = {1:("Програмування\nВища математика\nКомп'ютерна логіка","ООП\nФізика\nВища математика"),
                    2:(None,None),
                    3:(None,None),
                    4:(None,None)}

# value - credits;  key - curse;
palevo_bot_credits = {1:("Історія\nАлгоритми\nФП\nВступ до ОС Linux\nАналітична геометрія\nКурсач(Комп. логіка)","Англійська мова\nДМ\nФП\nКомп'ютерна арифметика\nУкр. мова"),
                      2:(None,None),
                      3:(None,None),
                      4:(None,None)}


try:
    @bot.message_handler(commands=["append_students_list"])
    def admin_students_list(message):
        file_with_captains_usernames = open("captains.txt", "r")
        captains_usernames = file_with_captains_usernames.read()
        file_with_captains_usernames.close()

        if message.from_user.username in captains_usernames:
            bot.send_message(message.chat.id, str('Напиши через кому юзернейми всіх студентів групи, яким ти хочеш дати доступ до бота у вигляді @ЮЗЕР_НЕЙМ.'))
        else:
            bot.send_message(message.chat.id, 'F U')


    @bot.message_handler(func = lambda message: "@" in message.text)
    def add_student(message):
        file_with_usernames = open("students.txt", "a")
        sl = message.text.split(",")
        for i in sl:
            file_with_usernames.write(i[1:]+'\n')

        file_with_usernames.close()
        bot.send_message(message.chat.id, 'these people were added: '+str(sl))


    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, str(start_letter))


    @bot.message_handler(commands=["get_students_list"])
    def get_students_list(message):
        file_with_usernames = open("students.txt", "r")
        sl = file_with_usernames.read()
        file_with_usernames.close()
        bot.send_message(chat_id = '3384244', text = str(sl))
    # @bot.message_handler(func = lambda message: 't' in message.text)
    # def handler_soccer(message):
    #
    #     keyboard = types.InlineKeyboardMarkup()
    #     url_button1 = types.InlineKeyboardButton(text="1")
    #     url_button2 = types.InlineKeyboardButton(text="2")
    #     keyboard.add(url_button1,url_button2)
    #     # bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)s
    #
    #     bot.send_message(message.chat.id,'dsfgsdf', parse_mode = 'Markdown', reply_markup = keyboard)



    def create_keyboard(first_word,input_list):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for i in input_list:
            button_curse = types.KeyboardButton(text=str(first_word+i))
            keyboard.add(button_curse)
        return keyboard


    @bot.message_handler(commands=["credits","exams","palevo"])
    def add_keyboard(message):
        file_with_usernames = open("students.txt", "r")
        usernames = file_with_usernames.read()
        file_with_usernames.close()

        if message.from_user.username in usernames:
            input_list = ('1 курс','2 курс','3 курс','4 курс')

            if message.text == "/credits":
                keyboard = create_keyboard('Заліки ',input_list)
            if message.text == "/exams":
                keyboard = create_keyboard('Екзамени ',input_list)
            if message.text == "/palevo":
                keyboard = create_keyboard("Палєво ",input_list)

            bot.send_message(message.chat.id, "Вибери курс: ", reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'F U')

    @bot.message_handler(func = lambda message: True)
    def curse(message):
        for i in message.text:
            try:
                number_curse = int(i)
                keyboard = types.InlineKeyboardMarkup()

                if 'Палєво' in message.text:
                    button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", url=palevo_bot_urls[number_curse][0])
                    button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", url=palevo_bot_urls[number_curse][1])
                elif 'Заліки' in message.text:
                    button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", callback_data=str(number_curse)+str(0)+'credits')
                    button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", callback_data=str(number_curse)+str(1)+'credits')
                elif 'Екзамени' in message.text:
                    button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", callback_data=str(number_curse)+str(0)+'exams')
                    button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", callback_data=str(number_curse)+str(1)+'exams')
                else:
                    bot.send_message(message.chat.id, "WTF!?!?!?!")
                keyboard.add(button1,button2)
                bot.send_message(message.chat.id, "Выбери семестр", reply_markup=keyboard)
            except:
                pass


    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        number_curse = int(str(call.data[0]))
        # Если сообщение из чата с ботом
        if call.message:
            if call.data[2:] == "credits":
                if palevo_bot_credits[number_curse][int(call.data[1])] == None:
                    bot.send_message(call.message.chat.id, text = "Вибачте, але інформація за цей семестр відсутня")
                else:
                    bot.send_message(call.message.chat.id, text = palevo_bot_credits[number_curse][int(call.data[1])])
            if call.data[2:] == "exams":
                if palevo_bot_exams[number_curse][int(call.data[1])] == None:
                    bot.send_message(call.message.chat.id, text = "Вибачте, але інформація за цей семестр відсутня")
                else:
                    bot.send_message(call.message.chat.id, text = palevo_bot_exams[number_curse][int(call.data[1])])

        # Если сообщение из инлайн-режима
        # elif call.inline_message_id:
        #     if call.data == "credits":
        #         bot.send_message(call.message.chat.id, text = palevo_bot_credits[number_curse])
        #     if call.data == "exams":
        #         bot.send_message(call.message.chat.id, text = palevo_bot_exams[number_curse])
except:
    bot.send_message(chat_id = 3384244, text = 'Бот пытался упасть!!!!!!!!!!!')

if __name__ == "__main__":
    bot.polling(none_stop=True)
