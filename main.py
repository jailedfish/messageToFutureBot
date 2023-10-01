import configparser
import mysql.connector
import telebot
from datetime import datetime, timedelta

config = configparser.ConfigParser()
config.read('config.ini')

bot = telebot.TeleBot(config['BOT']['TOKEN'])

table_main_query = '''CREATE TABLE req (
   msgId INT AUTO_INCREMENT UNIQUE,
   tgId INT NOT NULL ,
   text VARCHAR(255),
   time TIMESTAMP(10)
   PRIMARY KEY (tgId)
)'''

table_intent_query = '''CREATE TABLE intent (
    tgId INT NOT NULL UNIQUE
    FOREIGN KEY (author_id) REFERENCES req(tgID)
)'''


def post_init_transaction(cur):
    cur.execute('CREATE DATABASE main')
    cur.execute(table_main_query)
    cur.execute(table_intent_query)
    cur.commit()


def init():
    global con, cursor
    con = mysql.connector.connect(host='192.168.0.2', user='root', password='194@d&bF@&f$bd#s', database='requests')
    cursor = con.cursor()
    post_init_transaction(cursor)


@bot.message_handler(comands=['start'])
def start_handler(msg):
    bot.send_message(msg.chat.id, f'''hello, {msg.from_user.first_name}, ''')  # TODO: write greeting text

@bot.message_handler(comands=['new_message']):
    bot.send_message(msg.chat.id)
def



#cursor.execute('CREATE DATABASE requests')
#print(cursor)
