import telebot
from telebot import types

TOKEN = '5161029295:AAEn6S0Otvu_DMyVuHGK5xzVJZ_OW7H69yc'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите номер урока от 1 до 23'.format(message.from_user))

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '1':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '2':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '3':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '4':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '5':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '6':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '7':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '8':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '9':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '10':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '11':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '12':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '13':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '14':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '15':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '16':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '17':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '18':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '19':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '20':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '21':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '22':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)
        elif message.text == '23':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Видео", url='t.me/checking_assignments_bot')
            markup.add(button1)
            button2 = types.InlineKeyboardButton("Код", url='t.me/checking_assignments_bot')
            markup.add(button2)
            bot.send_message(message.chat.id, 'Проверка задания'.format(message.from_user),reply_markup=markup)



bot.polling(non_stop = True)

