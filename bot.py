import telebot
from telebot import types


TOKEN = '5184801601:AAHcy3NULOTk_T24ikA68KthAoAf01l_YLk'



bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.InlineKeyboardButton('Проверка заданий')
    item2 = types.InlineKeyboardButton('Вопросы и пожелания')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Проверка заданий':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Проверка", url='t.me/checking_assignments_bot')
            markup.add(button1)
            bot.send_message(message.chat.id, 'Нажми на кнопку и проверь задания'.format(message.from_user),reply_markup=markup)

        elif message.text == 'Вопросы и пожелания':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Спросить", url='https://t.me/coursepython')
            markup.add(button1)
            bot.send_message(message.chat.id, 'Нажми на кнопку и пообщайся с нами'.format(message.from_user),reply_markup=markup)



bot.polling(non_stop = True)