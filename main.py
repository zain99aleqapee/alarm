import telebot
from telebot import types

Token = '2053131835:AAHzGgQq-tGTY411o_tBPdMZZde8ChhRbvE'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    custom = types.ReplyKeyboardMarkup()
    first_stage = types.KeyboardButton('first')
    second_stage = types.KeyboardButton('المرحلة الثانية')
    third_stage = types.KeyboardButton('المرحلة الثالثة')
    forth_stage = types.KeyboardButton('المرحلة الرابعة')
    custom.row(second_stage, first_stage)
    custom.row(forth_stage, third_stage)
    bot.send_message(chat_id, 'مرحبًا بكم في بوت حاسوبجي...', reply_markup=custom)


@bot.message_handler(commands=['first'])
def first_stage_Button(message):
    chat_id = message.chat.id
    custom = types.ReplyKeyboardMarkup()
    lectueres = types.KeyboardButton('المحاضرات')
    table = types.KeyboardButton('الجدول الإسبوعي')
    files = types.KeyboardButton('الملفات والبرامج المطلوبة')
    back = types.KeyboardButton('الرجوع')
    custom.row(lectueres)
    custom.row(table)
    custom.row(files)
    custom.row(back)
    bot.send_message(chat_id, 'مرحبًا بكم في بوت حاسوبجي...', reply_markup=custom)


bot.polling(non_stop=True, interval=0)
