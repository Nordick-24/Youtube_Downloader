from pytube import YouTube
from loguru import logger
import os
import telebot


@logger.catch()
def Download_Video(link, bot, message) -> str:
    """Find, Download and save Video from Youtube"""
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution()

    youtube_video.download(output_path="video", filename="video.mp4")

    with open("video/video.mp4", 'rb') as result:
        bot.send_video(message.chat.id, result)


api_token = os.getenv('api_token')
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start'])
@logger.catch()
def start(message):
    bot.send_message(message.chat.id, "Hello, it's downloader bot <;. Send Youtube link:")

    @bot.message_handler()
    @logger.catch()
    def user_link(message):
        Download_Video(message.text, bot, message)


bot.polling()
