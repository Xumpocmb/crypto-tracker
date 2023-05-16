import telebot

# создаем объект бота
bot = telebot.TeleBot('')


# отправляем сообщение
def send_notify(message):
    bot.send_message(123456, message)
