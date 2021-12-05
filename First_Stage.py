import main
import telebot
from telebot import types

Token = '2053131835:AAHzGgQq-tGTY411o_tBPdMZZde8ChhRbvE'
bot = telebot.TeleBot(Token)





bot.polling(non_stop=True, interval=0)
