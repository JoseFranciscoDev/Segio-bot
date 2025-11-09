import bot.commands as commands  # noqa: F401
from bot_instance import bot, telebot


@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, "Oieee")

bot.infinity_polling()