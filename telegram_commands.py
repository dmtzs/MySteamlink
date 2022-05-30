try:
    import telebot
    import subprocess
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

API_TOKEN = ""

bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['help', 'start'])
@bot.message_handler(commands=["help"])
def send_welcome(message):
    message_to_send = ""
    bot.reply_to(message, message_to_send)

@bot.message_handler(commands=["shutdownrasp"])
def reboot_rasp(message):
    message_to_send = "Reiniciando raspberry"
    bot.reply_to(message, message_to_send)
    subprocess.Popen('shutdown now', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@bot.message_handler(commands=["iprasp"])
def ip_rasp(message):
    command = subprocess.Popen('hostname -I', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = command.communicate()[0]
    result = result.decode("ascii")
    bot.reply_to(message, result)

if __name__ == '__main__':
    bot.infinity_polling()