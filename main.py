from telebot.async_telebot import AsyncTeleBot
import telebot
import asyncio
bot = AsyncTeleBot('All right, then. Keep your secrets')


@bot.message_handler(commands=['start'])
async def send_start(message):
    await bot.reply_to(message, """\
Send /help command for more info and botay!\
""")


@bot.message_handler(commands=['channel'])
async def channel(message):
    await bot.send_message(message.chat.id, "https://www.youtube.com/@user-sg8rx3ms4y/featured")


@bot.message_handler(commands=['articles'])
async def articles(message):
    await bot.send_message(message.chat.id, "https://vk.com/@prikazbotat")


@bot.message_handler(commands=['book'])
async def book(message):
    await bot.send_message(message.chat.id, "https://www.dropbox.com/sh/thxwormjhy6ojc4/AABgmk329Bsp5TGmKIsAB7kAa?dl=0")


@bot.message_handler(commands=["help"])
async def send_help(message):
    await bot.reply_to(message, """\
Available commands:
/start
/help
/channel
/articles
/book\
""")


bot.add_custom_filter(telebot.asyncio_filters.ChatFilter())

asyncio.run(bot.polling())
