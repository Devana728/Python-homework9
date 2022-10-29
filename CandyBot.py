
import telebot
from random import randint

total_candy = int(2021)
def count_candy(candy):
    global n
    if int(candy) > 28 :
        return 'можно взять не больше 28 конфет'  
    if int(candy) > n :  
        return f'нельзя взять больше конфет,чем {n}'   
    n = n - int(candy)
    if n<=0:
        n = total_candy

        return "победил игрок!\n начинаем с начала"
    botcandy = randint (1,28)
    n = n - botcandy
    if n<=0:
        n = total_candy
        return "победил бот! \n начинаем с начала"
    
    return f"бот взял {botcandy} \n осталось конфет {n} "
n = total_candy
bot = telebot.TeleBot('5391583782:AAHUdvRJJE-O5lkTwd5KVRqHOfVE7lH6yeo')
@bot.message_handler(commands = ['старт'])
def send_welcome1(message):
	bot.reply_to(message, "Введите количество конфет от 1 до 28")
@bot.message_handler(func=lambda message: True)
def input(message2):
    
    bot.reply_to(message2, count_candy(message2.text))
    
bot.infinity_polling()