import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot("8510007013:AAG-7POxIC8waS5xO2lkTgXDiNS6qVTVDkQ")
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="Поднятия уровня в одиночку"url="https://t.me/+cRKDV07zuxViZWEy")
    b2 = InlineKeyboardButton(text="Баскетбол Куроко",,url="https://t.me/+_ONPr3J5OoI4MTZi")
    b3 = InlineKeyboardButton(text="Атака Титанов",,url="https://t.me/+ikAzKKs2ziM4MzMy")
    markup.add(b1)
    markup.add(b2)
    markup.add(b3)
    bot.send_message(message.chat.id, "Какой аниме хотите посмотреть?", reply_markup=markup)
bot.polling()
