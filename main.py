import configparser
import mysql.connector
import telebot
from dataclasses import dataclass
from datetime import datetime, timedelta

config = configparser.ConfigParser()
config.read('config.ini')

bot = telebot.TeleBot(config['BOT']['TOKEN'])

@bot.messageHandler(comands=['start'])
def start_handler(msg):
    bot.

con = mysql.connector.connect(host='192.168.0.2', user='root', password='194@d&bF@&f$bd#s')
cursor = con.cursor()
cursor.execute('CREATE DATABASE reqests')
print(cursor)

