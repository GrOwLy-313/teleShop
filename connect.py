import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('7621765087:AAFBNoGy0mXEu4qgEs7UCD4HhH--KxZq7oE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://growly-313.github.io/teleShop')))
    markup.add(KeyboardButton('хвхвхвхв', callback_data="menu_shop"))
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)