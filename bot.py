import telebot
import string
import random

TOKEN = '8819315177:AAE6dWaygaDUoKBC_69gk8pW4IX-2tX-2cg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
 bot.reply_to(message, "Welcome to DeathCode")

@bot.message_handler(commands=['help'])
def help_message(message):
 bot.reply_to(message, "This is the help command.")

@bot.message_handler(commands=['generate_key'])
def generate_key(message):
 

