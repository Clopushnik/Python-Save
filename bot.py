import telebot

from telebot import types


bot = telebot.TeleBot('6461201629:AAHU9QDdpLHT3O-OxXCTJQCmnDn7hZwSf0A')

#отслеживание команд
@bot.message_handler(commands=['start'])


#функции для команд 
def start(message):
    mess= f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'# текст, который выводить бот при написании команды /start
    bot.send_message(message.chat.id, mess, parse_mode='html')


#отслеживаем любые текстовые записи
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'ку' or message.text == 'Ку':
        bot.send_message(message.chat.id, '<b>Здарова!</b>', parse_mode='html')
    elif message.text == 'id' or message.text == 'ID':
        bot.send_message(message.chat.id, f'<b>Твой ID:<u>{message.from_user.id}</u></b>', parse_mode='html')
    elif message.text == 'покажи пенис':
        bot.send_message(message.chat.id, f'<b><s>иди нахуй да)</s></b>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, '<b>Че ты несешь?</b>', parse_mode='html')

@bot.message_handler(commands=['buttons'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    sanya = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(sanya, start)
    bot.send_message(message.chat.id, 'rfdj', reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Саня', url='https://vk.com/monegasik17'))
    bot.send_message(message.chat.id, 'уфффффф', reply_markup=markup)


bot.polling(none_stop=True)