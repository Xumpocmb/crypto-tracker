import telebot

# создаем объект бота
bot = telebot.TeleBot('6113360297:AAGikeld4Us-q3B75l2SHZNuqDEPdKbsW9U')


# отправляем сообщение
def send_notify(message):
    bot.send_message(404331105, message)
