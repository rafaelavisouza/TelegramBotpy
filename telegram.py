import telepot
from chatbot import Chatbot

telegram = telepot.Bot("7472309964:AAFOWTCdhh3a1KDue87jWwQI5gFXVHvBUhY")
bot = Chatbot("Vitoriamar")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg["text"])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg["chat"]["id"]
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
    pass