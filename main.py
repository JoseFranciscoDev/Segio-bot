import bot.commands as commands  # noqa: F401
from bot_instance import bot


@bot.message_handler(['start'])
def start(msg):
    bot.reply_to(msg, "Oieee")

bot.infinity_polling()