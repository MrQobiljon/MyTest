from telebot import TeleBot
from telebot.types import Message, InputMediaPhoto

bot = TeleBot("8132030030:AAGc9SUwncuAjENLYg4IIznJlDyn6HehIRc")


@bot.message_handler(content_types=['video_note', 'photo', 'image'])
def reaction_to_all_messages(message: Message):
    if message.content_type == 'video_note':
        print(message.video_note.file_id)
    elif message.content_type == 'photo':
        print(message.photo[-1].file_id)


@bot.message_handler(commands=['photo'])
def photo(message: Message):
    chat_id = message.chat.id
    bot.send_photo(chat_id, "AgACAgQAAxkBAAMHZ40fzBkg3FIITxqQ2FNY_32uujcAAgvLMRttK2lQuVYseVdwzakBAAMCAAN5AAM2BA")

    media = [
        InputMediaPhoto("AgACAgQAAxkBAAMIZ40jQovpSAYLkgkJGRc-f2MnFAgAAhDLMRttK2lQ2-cIWCzssB4BAAMCAAN5AAM2BA"),
        InputMediaPhoto("AgACAgQAAxkBAAMJZ40jYIuxAoYjZZYKi2hbTlyEEMEAAhHLMRttK2lQh-JFPsqilvYBAAMCAAN5AAM2BA")
    ]

    bot.send_media_group(chat_id, media)


bot.infinity_polling()