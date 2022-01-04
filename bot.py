from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types


API_TOKEN = '5006682486:AAEm7d2K-rtX31y6OJjH26VsQjsFD2gJ3t8'

bot = telebot.TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('shabake tamasha')
    itembtnv = types.KeyboardButton('shabake namayesh')
    itembtnc = types.KeyboardButton('shabakeye 1')
    itembtnd = types.KeyboardButton('shabakeye 2')
    itembtne = types.KeyboardButton('shabakeye 3')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    cid = message.chat.id
    msg = bot.send_message(cid, "Choose one letter:", reply_markup=markup)



@bot.message_handler(func=lambda message: True)
def echo_message(message):
    


    url = "http://namayeshtv.ir/public/jadvalpakhsh/site"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    ul = soup.find(class_="featured")

    li = ul.findChildren("li")

    ultime = soup.find(class_="last_col")
    time = ultime.findChildren("li")

    str1= ""
    count = 1
    for i in li:
        if count != 1:
            str1+=")"
        str1+="\n"
        
        
        str1 +=time[count-1].text + ": "
        str1+="("
        count +=1
        for x in(i.contents):
            str1 +=  x

    bot.reply_to(message, str1)

bot.infinity_polling()
