
# -*- coding: utf-8 -*-
# ver 1.1.0


import telebot
from telebot import types

bot = telebot.TeleBot("484353959:AAFzVzbMcHNhhmKCmbyxIjkQJ5PWbbE4Ils")

start_letter = "Цей бот створений для потоку ІО/ІВ. Тут ви зможете знайти  'палєво' по команді /palevo. Також дізнатися по яким предметам у вас будуть заліки /credits або екзамени /exams.Якщо ти староста, можеш використати цю команду /append_students_list щоб надати своїм тудентам доступ до функцій бота."

start_letter = "Цей бот створений для потоку ІО/ІВ. Тут ви зможете знайти  'палєво' по команді /palevo. Також дізнатися по яким предметам у вас будуть заліки /credits або екзамени /exams. /append_students_list"


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

# Словарь для хранения "состояний чата"
user_step = dict()

# Если пользователь воодит команды START OR HELP выполняется эта функция
@bot.message_handler(commands=["start","help"])
def start_message(message):
    bot.send_message(message.chat.id, str(start_letter))
    user_step[message.chat.id] = "USER_START"



# функция для получения белого списка студентов и старост с удаленного сервера
@bot.message_handler(commands=["get_all"])
def get_students_list(message):
    file_with_usernames = open("students.txt", "r")
    sl = file_with_usernames.read()
    file_with_usernames.close()

    file_with_captains_usernames = open("captains.txt", "r")
    cl = file_with_captains_usernames.read()
    file_with_captains_usernames.close()

    bot.send_message(chat_id = '3384244', text = "Старости:\n{0}\n\nСтуденти:\n{1}".format(cl,sl))

@bot.message_handler(commands=["append_captains_list"])
def append_students_list(message):
    user_step[message.chat.id] = "USER_EDIT_CAPTAINS_LIST_START"

    file_with_captains_usernames = open("captains.txt", "r")
    captains_usernames = file_with_captains_usernames.read()
    file_with_captains_usernames.close()

    if message.from_user.username in captains_usernames:
        bot.send_message(message.chat.id, str('Напиши юзернейми старост, яким ти хочеш дати доступ до адмінки бота у вигляді @ЮЗЕР_НЕЙМ.'))
    else:
        bot.send_message(message.chat.id, 'F U')


@bot.message_handler(func=lambda message: user_step.get(message.chat.id) == "USER_EDIT_CAPTAINS_LIST_START")
def add_student(message):
    file_with_usernames = open("captains.txt", "a")
    sl = message.text.split(" ")
    for i in sl:
        if "@" in i:
            file_with_usernames.write(i[1:]+'\n')
        else:
            file_with_usernames.write(i+'\n')
    file_with_usernames.close()

    keyboard = types.InlineKeyboardMarkup()
    button_stop = types.InlineKeyboardButton(text='Завершити редагування.',callback_data="USER_EDIT_STUDENT_LIST_STOP, {}".format(message.message_id))
    keyboard.add(button_stop)

    bot.send_message(message.chat.id, "users {} add".format(message.text), reply_markup=keyboard)


# Если пользователь захотел добавить людей в белый список
# нужно доделать админку с редактированием этого списка
@bot.message_handler(commands=["append_students_list"])
def append_students_list(message):
    user_step[message.chat.id] = "USER_EDIT_STUDENT_LIST_START"

    file_with_captains_usernames = open("captains.txt", "r")
    captains_usernames = file_with_captains_usernames.read()
    file_with_captains_usernames.close()

    if message.from_user.username in captains_usernames:
        bot.send_message(message.chat.id, str('Напиши юзернейми всіх студентів групи, яким ти хочеш дати доступ до бота у вигляді @ЮЗЕР_НЕЙМ.'))
    else:
        bot.send_message(message.chat.id, 'F U')


# ввод юзернеймов пользователей которых добавляет староста
@bot.message_handler(func=lambda message: user_step.get(message.chat.id) == "USER_EDIT_STUDENT_LIST_START")
def add_student(message):
    file_with_usernames = open("students.txt", "a")
    sl = message.text.split(" ")
    for i in sl:
        if "@" in i:
            file_with_usernames.write(i[1:]+'\n')
        else:
            file_with_usernames.write(i+'\n')
    file_with_usernames.close()

    keyboard = types.InlineKeyboardMarkup()
    button_stop = types.InlineKeyboardButton(text=' ❌ Завершити редагування.',callback_data="USER_EDIT_STUDENT_LIST_STOP, {}".format(message.message_id))
    keyboard.add(button_stop)

    bot.send_message(message.chat.id, "users {} add".format(message.text), reply_markup=keyboard)


# когда пользователь нажал кнопку ЗАКОНЧИТЬ РЕДАКТИРОВАНИЕ
# нужно доделать редактирование сообщения. Что бы не присылать еще одно
#                       (смотрится некрасиво)
@bot.callback_query_handler(func=lambda call:  "USER_EDIT_STUDENT_LIST_STOP" in call.data )
def exit_in_append_students_list(call):
    user_step[call.message.chat.id] = call.data.split(', ')[0]
    # m_id = call.data.split(', ')[1]
    # print(m_id)
    # bot.edit_message_text(chat_id=call.message.chat.id, message_id=m_id, text='Редагування білого списку завершено')
    bot.send_message(call.message.chat.id,'✅✅✅ЗАВЕРШЕНО!✅✅✅')


#         Создается инлайн клавиатура "первого уровня"
#               На ней можно выбрать курс
#           (создается одинаково для 3-х команд)
def create_keyboard(first_word,input_list):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for i in input_list:
        button_curse = types.InlineKeyboardButton(text=str(first_word+i),callback_data="USER_STEP_1LVL_{0}_{1}".format(first_word,i[0]))
        keyboard.add(button_curse)
    return keyboard


#              Функция отвечает за 3 команды
#   и создает инлайн клавиатуру на которой можно выбрать курс
@bot.message_handler(commands=["credits","exams","palevo"])
def add_keyboard(message):
    user_step[message.chat.id] = "USER_ENTER_COMMAND"
    file_with_usernames = open("students.txt", "r")
    usernames = file_with_usernames.read()
    file_with_usernames.close()

    if message.from_user.username in usernames:
        input_list = ('1️⃣ курс','2️⃣ курс','3️⃣ курс','4️⃣ курс')

        if "/credits" in message.text:
            keyboard = create_keyboard('Заліки ',input_list)
        if "/exams" in message.text:
            keyboard = create_keyboard('Екзамени ',input_list)
        if "/palevo" in message.text:
            keyboard = create_keyboard("Палєво ",input_list)

        bot.send_message(message.chat.id, text="Вибери курс: " , reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'F U')


#       Эта ф-ия выполняется при нажатии кнопки CANCEL
# в принципе она делать то же самое что и ф-ия для команд
@bot.callback_query_handler(func=lambda call:  "CANCEL" in call.data )
def add_keyboard_after_cancel(call):
    input_list = ('1️⃣ курс','2️⃣ курс','3️⃣ курс','4️⃣ курс')

    if "Заліки" in call.data:
        keyboard = create_keyboard('Заліки ',input_list)
    if "Екзамени" in call.data:
        keyboard = create_keyboard('Екзамени ',input_list)
    if "Палєво" in call.data:
        keyboard = create_keyboard("Палєво ",input_list)

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вибери курс: " , reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: '1LVL' in call.data)
def curse_inline(call):
    for i in call.data:
        try:
            number_curse = int(i)
        except:
            continue
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    cancel_button = types.InlineKeyboardButton(text="⬅️ Назад", callback_data="CANCEL"+call.data)
    if call.message:
        if "Палєво" in call.data:
            button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", url=palevo_bot_urls[number_curse][0])
            button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", url=palevo_bot_urls[number_curse][1])
        if "Заліки" in call.data:
            button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", callback_data="2LVL_{0}_{1}_{2}".format(number_curse,0,'credits'))
            button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", callback_data="2LVL_{0}_{1}_{2}".format(number_curse,1,'credits'))
        if "Екзамени" in call.data:
            button1 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse-1) + " семестр", callback_data="2LVL_{0}_{1}_exams".format(number_curse,0))
            button2 = types.InlineKeyboardButton(text="Перейти на " + str(2*number_curse) + " семестр", callback_data="2LVL_{0}_{1}_exams".format(number_curse,1))
        else:
            pass

    keyboard.add(button1,button2,cancel_button)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери семестр", reply_markup=keyboard )



@bot.callback_query_handler(func=lambda call: '2LVL' in call.data)
def semester_inline(call):
    number_curse = int(call.data.split('_')[1])
    if call.data.split('_')[3] == "credits":
        if palevo_bot_credits[number_curse][int(call.data.split('_')[2])] == None:
            bot.send_message(call.message.chat.id, text = "Вибачте, але інформація за цей семестр відсутня")
        else:
            bot.send_message(call.message.chat.id, text = palevo_bot_credits[number_curse][int(call.data.split('_')[2])])

    if call.data.split('_')[3] == "exams":
        if palevo_bot_exams[number_curse][int(call.data.split('_')[2])] == None:
            bot.send_message(call.message.chat.id, text = "Вибачте, але інформація за цей семестр відсутня")
        else:
            bot.send_message(call.message.chat.id, text = palevo_bot_exams[number_curse][int(call.data.split('_')[2])])


#       Эта ф-ия должна бить после функции для команд, потому что она принимает текст
#           и команду тоже распознает как текст
#       По этому если мы введем команду то ее перехватит верхняя ф-ия
@bot.message_handler(func=lambda message: user_step.get(message.chat.id) != "USER_EDIT_STUDENT_LIST_STAPT")
def free_message(message):
    print(message.text)
    bot.send_message(message.chat.id, 'Меньше слов - больше дела!')


if __name__ == "__main__":
    bot.polling(none_stop=True)
