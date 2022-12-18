from pytube import YouTube
from loguru import logger
import os
import telebot


logger.success("Bot Started and working!") #  When i start a program i don't see info about this

@logger.catch()
def Download_Video(link, bot, message) -> str:
    """Find, Download and save Video from Youtube"""
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution()

    youtube_video.download(output_path="video", filename="video.mp4")

    with open("video/video.mp4", 'rb') as result:
        bot.send_video(message.chat.id, result)

        with open("insutruction.png", 'rb') as inctruction: #  User needs to know hot to download this.
            bot.send_photo(message.chat.id, inctruction)


api_token = os.getenv('api_token')
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start', 'help'])
@logger.catch()
def start(message) -> None:
    """Get user link and use function 'Download_Video'"""
    bot.send_message(message.chat.id, "Hello, it's downloader bot <;. Send Youtube link:")

    @bot.message_handler()
    @logger.catch()
    def user_link(message):
        Download_Video(message.text, bot, message)


@bot.message_handler(commands=['bug'])
@logger.catch()
def bug_report(message) -> None:
    bot.send_message(message.chat.id, "If you find some error, please let me know about this -> https://github.com/Nordick-24/Youtube_Downloader, Thank You!")


bot.polling()
logger.debug("Bot is disable by user")
