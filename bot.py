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
    itembtna = types.KeyboardButton('شبکه نمایش')
    itembtnv = types.KeyboardButton('شبکه نسیم')
    itembtnc = types.KeyboardButton('شبکه یک')
    itembtnd = types.KeyboardButton('شبکه دو')
    itembtne = types.KeyboardButton('شبکه سه')
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
    name_a1=[]
    name_a =[]
    zaman1=[] 
    count=0
    count1=0
    url = "https://tvnasim.ir/conductor"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    name1 = soup.findAll(class_="program-name")
    for i in name1:
        name_a.append(i.findChildren('a',title=True))
    for x in name_a: 
        name_a1.append(x[0].attrs['title'])
    zaman = soup.findAll(class_="text-center")
    for z in zaman:
        if count !=0 and count!=1:
            zaman1.append(z.text)
        count+=1
    str2=""
    for j in name_a1:
        if count1!=0:
            str2+="\n"
        str2+=zaman1[count1]+": "
        str2+=j
        count1+=1


    if message.text=="شبکه نمایش":
        bot.reply_to(message, str1)
    if message.text=="شبکه نسیم":
        bot.reply_to(message, str2)

bot.infinity_polling()
