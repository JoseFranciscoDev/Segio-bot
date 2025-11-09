from datetime import datetime

import telebot

from bot_instance import bot

hora_atual = datetime.now()

@bot.message_handler(['hora_atual'])
def command_hora_atual(msg: telebot.types.Message):
    print(msg)
    bot.reply_to(msg, f"Agora é {hora_atual}")
    
@bot.message_handler(['quem é'])
def command_quem_voce_e(msg: telebot.types.Message):
    bot.reply_to(msg, "Eu sou o Sérgio Bot e fui feito pelo Zé pra ser seu escravo digital")
