import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Mapeamento fixo Igorês <-> PT
mapa = {
    'a':'l','b':'v','c':'x','d':'s','e':'w','f':'d','g':'f','h':'g','i':'u',
    'j':'i','k':'o','l':'p','m':'z','n':'a','o':'k','p':'q','q':'p','r':'e',
    's':'d','t':'r','u':'y','v':'c','w':'t','x':'h','y':'n','z':'m'
}

# Traduz Igorês <-> PT automaticamente
def traduz(texto):
    texto = texto.lower()
    traduzido = ''
    for letra in texto:
        if letra in mapa:
            traduzido += mapa[letra]
        elif letra in mapa.values():
            # Inverte a tradução (PT <-> Igorês)
            for k, v in mapa.items():
                if v == letra:
                    traduzido += k
                    break
        else:
            traduzido += letra
    return traduzido

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    traduzido = traduz(message.text)
    bot.reply_to(message, traduzido)

print("🌿 Bot Igorês rodando como background worker...")
bot.polling()
