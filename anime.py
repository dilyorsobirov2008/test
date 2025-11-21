import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot("8510007013:AAG-7POxIC8waS5xO2lkTgXDiNS6qVTVDkQ")
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("Наруто",url="https://t.me/+cRKDV07zuxViZWEy")
    b2 = InlineKeyboardButton("Ван Пис",url="https://t.me/+_ONPr3J5OoI4MTZi")
    b3 = InlineKeyboardButton("Атака Титанов",url="https://t.me/+ikAzKKs2ziM4MzMy")
    markup.row(b1)
    markup.row(b2)
    markup.row(b3)
    reply_markup=markup
    bot.send_message(message.chat.id, "Какой аниме хотите посмотреть?")
bot.polling()
