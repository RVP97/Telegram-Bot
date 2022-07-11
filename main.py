import telebot
import os
import requests

bot = telebot.TeleBot(os.environ['TOKEN'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to the bot!")

@bot.message_handler(commands=['btc'])
def send_price(message):
    rate_list = [0]
    time_list = [0]
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    time = data['time']['updated']
    rate = data['bpi']['USD']['rate']
    bot.send_message(message.chat.id, f'''{time}
Rate: ${rate}''')

bot.infinity_polling()