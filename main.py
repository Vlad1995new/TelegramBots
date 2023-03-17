import telebot
from telebot import types


photo_url = 'https://s0.rbk.ru/v6_top_pics/media/img/1/04/756529824000041.jpg'
TOKEN = '5654490469:AAHDq_XH3LRVpWfNFtEYz_2tfP9mGhI4l-4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton(text='Отправить картинку')
    btn2 = types.KeyboardButton(text='Отправить файл')
    btn3 = types.KeyboardButton(text='Ответить на вопрос')
    kb.add(btn2,btn1)
    kb.add(btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Отправить картинку':
        bot.send_photo(message.chat.id, photo=photo_url, caption='Это фото')
    elif message.text == 'Отправить файл':
        f = open('telegram-bot/file.txt', 'rb')
        bot.send_document(message.chat.id, document=f, caption='Очень важный файл')
    elif message.text == 'Ответить на вопрос':
        inlinekb= types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='2', callback_data='2')
        btn2 = types.InlineKeyboardButton(text='4', callback_data='4')
        btn3 = types.InlineKeyboardButton(text='6',callback_data='6')
        inlinekb.add(btn2, btn1, btn3)
        bot.send_message(message.chat.id, '2+2=?', reply_markup=inlinekb)

@bot.callback_query_handler(func=lambda call: True)
def getAnswer(call):
    if call.data == '4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы ответили верно!')
    elif call.data == '2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы ответили не верно!')
    elif call.data == '6':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вы ответили не верно!')



bot.polling(none_stop=True)