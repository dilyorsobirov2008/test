import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot("8510007013:AAG-7POxIC8waS5xO2lkTgXDiNS6qVTVDkQ")
@bot.message_handler(commands=['start'])
def start(message):
    #
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="Поднятия уровня в одиночку", url="https://t.me/+vxrOVi2Kj2BmYmYy")
    b2 = InlineKeyboardButton(text="Баскетбол Куроко", url="https://t.me/+upBBVC1VzstiZTBi")
    b3 = InlineKeyboardButton(text="Атака Титанов", url="https://t.me/+tE6bHu5EfT0yODhi")
    b4 = InlineKeyboardButton(text="о моем перерождение в слизь", url="https://t.me/+QnpTh0gwTlc1N2I6")
    markup.add(b1)
    markup.add(b2)
    markup.add(b3)
    markup.add(b4)
    bot.send_message(message.chat.id, "Какой аниме хотите посмотреть?", reply_markup=markup)
bot.infinity_polling()