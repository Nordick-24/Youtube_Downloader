from pytube import YouTube
from loguru import logger
import os
import telebot


logger.success("Bot Started and working!")
# When i start a program i don't see info about this

@logger.catch()


def downloadVideo(link: str, bot, message) -> str:
    """Find, Download and save Video from Youtube"""
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution()

    youtube_video.download(output_path="video/", filename="video.mp4")

    with open("video/video.mp4", 'rb') as donwloaded_video:
        bot.send_video(message.chat.id, donwloaded_video)

        with open("insutruction.png", 'rb') as inctruction: #  User needs to know hot to download this.
            bot.send_photo(message.chat.id, inctruction)


api_token = os.getenv('api_token')
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start', 'help'])
@logger.catch()


def start(message) -> None:
    """Get user link and use function 'Download_Video'"""
    bot.send_message(message.chat.id, "Hi, My name is Bot-Downloader, Send your link and i gonna do everythings myself!")

    @bot.message_handler()
    @logger.catch()
    def get_user_link(message):
        downloadVideo(message.text, bot, message)


@bot.message_handler(commands=['bug'])
@logger.catch()


def bug_report(message) -> None:
    bot.send_message(message.chat.id, "If you find some error, please let me know about this -> https://github.com/Nordick-24/Youtube_Downloader, Thank You!")


bot.polling()
logger.debug("Bot is disable by user")

