import telebot
import os

TOKEN = os.getenv("7600077413:AAEzsysN_deTX9KC--3dbBNuo0fjQJ6rQsY")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "هلا 🙋‍♂️! أني بوت شغال 24 ساعة 🔥")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"انت كتبت: {message.text}")

print("🚀 البوت اشتغل بنجاح!")
bot.infinity_polling()
