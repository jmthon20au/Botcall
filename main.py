import telebot

bot = telebot.TeleBot("6838907276:AAG-raevaCYPVazYBbgROgy3xqeRxUM-D1g")

@bot.message_handler(commands=['start'])
def pyroo(msg):
    bot.reply_to(msg, "ارسل اسمك حب")
    bot.register_next_step_handler(msg, robots)

def robots(msg):
    name = msg.text
    pyro = bot.reply_to(msg, "حسنا ارسل الان الرقم")
    bot.register_next_step_handler(pyro, phone, name)

def phone(pyro, name):
    
    phone_number = pyro.text
    bot.send_contact(pyro.from_user.id, phone_number, name)

bot.polling()

#follow us for more : https://t.me/mmaahg