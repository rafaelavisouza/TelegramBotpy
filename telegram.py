import telepot
from telepot.loop import MessageLoop
from chatbot import Chatbot

chaveApi = "COLOQUE_SUA_CHAVE_AQUI"
telegram = telepot.Bot(chaveApi)
bot = Chatbot("Vitoriamar")

def recebendoMsg(msg):
    # Verifica se a mensagem contém texto
    if 'text' in msg:
        chatID = msg["chat"]["id"]
        frase = msg["text"]
        resp = bot.pensa(frase)
        telegram.sendMessage(chatID, resp)

MessageLoop(telegram, recebendoMsg).run_as_thread()

# Mantém o script rodando
while True:
    pass
