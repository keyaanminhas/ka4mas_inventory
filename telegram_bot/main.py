from telegram import KeyboardButton, ReplyKeyboardMarkup #upm package(python-telegram-bot)
from telegram.ext.updater import Updater #upm package(python-telegram-bot)
from telegram.update import Update #upm package(python-telegram-bot)
from telegram.ext.callbackcontext import CallbackContext #upm package(python-telegram-bot)
from telegram.ext.commandhandler import CommandHandler #upm package(python-telegram-bot)
from telegram.ext.messagehandler import MessageHandler#upm package(python-telegram-bot)
from telegram.ext.filters import Filters #upm package(python-telegram-bot)
from telegram.ext import ContextTypes #upm package(python-telegram-bot)
from telegram.ext import * #upm package(python-telegram-bot)
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup #upm package(python-telegram-bot)

from time import sleep
import threading

with open('config.txt', 'r') as f:
    x = f.readlines()
    token = x[0].strip()
    time1, time2  = (x[1].strip()).split(',')
updater = Updater(token,
                  use_context=True)
  
disp = updater.dispatcher

print(token, time1, time2)
def messagesender(update, context, MESSAGE):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id = chat_id,text = MESSAGE)


def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

# def start(update, context):
#     button = [[KeyboardButton("BTC MINING")], [KeyboardButton("CASINO")]]
#     context.bot.send_message(chat_id = update.effective_chat.id, text="CHOOSE A CATEGORY!", reply_markup = ReplyKeyboardMarkup(button))
#     chat_id = update.message.chat_id


def start(update,context):
    list_of_cities = ['BTC MINING', 'CASINO', 'ACCOUNT']
    button_list = []
    for each in list_of_cities:
        button_list.append(InlineKeyboardButton(each, callback_data = each, show_alert = True))
    reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('RacoonFury3.png', 'rb'), caption = 'WELCOME TO CASINO AND MINING SERVICE !!!')
    context.bot.send_message(chat_id=update.effective_chat.id,text = "CHOOSE A CATEGORY TO START EARNING", reply_markup=reply_markup)

def BTC_MINING(update, context):
    list_of_cities = ['Mining Plan Standard', 'Mining Plan Bronze', 'Mining Plan Silver', 'Mining Plan Gold', 'Mining Plan Diamond']
    button_list = []
    chat_id = update.effective_chat.id
    for each in list_of_cities:
        button_list.append(InlineKeyboardButton(each, callback_data = each, show_alert = True))
    reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows


    context.bot.send_message(chat_id=chat_id, text="SELECT A PACKAGE",reply_markup=reply_markup)



def Mining_Plan_Bronze(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('bronze.jpg', 'rb'), caption = 'Mining Plan Bronze - Deposit 0.00050000 BTC to earn 0.00100000 BTC in 6 Months. WALLET ADDRESS: 1PQhZjGYJrFEWgjMLm9ZXhq1qRE97HkVvb')

def Mining_Plan_Silver(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('silver.png', 'rb'), caption = 'Mining Plan Silver - Deposit 0.00100000 BTC to earn 0.00500000 BTC in 6 Months. WALLET ADDRESS: 1PQhZjGYJrFEWgjMLm9ZXhq1qRE97HkVvb')

def Mining_Plan_Gold(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('standard.jpg', 'rb'), caption = 'Mining Plan Gold - Deposit 0.00500000 BTC to earn 0.01000000 BTC in 6 Months. WALLET ADDRESS: 1PQhZjGYJrFEWgjMLm9ZXhq1qRE97HkVvb')

def Mining_Plan_Diamond(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('diamond.jpg', 'rb'), caption = 'Mining Plan Diamond - Deposit 0.01000000 BTC to earn 0.05000000 BTC in 6 Months. WALLET ADDRESS: 1PQhZjGYJrFEWgjMLm9ZXhq1qRE97HkVvb')

def Mining_Plan_Standard(update, context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo = open('gold.png', 'rb'), caption = 'Mining Plan Standard - Deposit 0.00010000 BTC to earn 0.001 BTC in 6 Months. WALLET ADDRESS: 1PQhZjGYJrFEWgjMLm9ZXhq1qRE97HkVvb')







with open('message.txt', 'r') as f:
    x = f.readlines()
    z = [y.strip() for y in x]



def CASINO(update, context):
    list_of_cities = ['ROLLER COIN', 'FREEBITCOIN', 'BISWAP', 'MOMOverse', 'BETFURY', 'BINANCE', 'COINBASE']
    button_list = []
    chat_id = update.effective_chat.id
    for each in list_of_cities:
        button_list.append(InlineKeyboardButton(each, callback_data = each, show_alert = True))
    reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows


    context.bot.send_message(chat_id=chat_id, text="SELECT A CASINO (FREE BONUSES)",reply_markup=reply_markup)
    




def ROLLER_COIN(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[0])

def FREEBITCOIN(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[1])

def BISWAP(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[2])

def MOMOverse(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[3])

def BETFURY(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[4])

def BINANCE(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[5])

def COINBASE(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = z[6])


def ACCOUNT(update, context):
    list_of_cities = ['My Balance', '', 'Mining Plan Silver', 'Mining Plan Gold', 'Mining Plan Diamond']
    button_list = []
    chat_id = update.effective_chat.id
    for each in list_of_cities:
        button_list.append(InlineKeyboardButton(each, callback_data = each, show_alert = True))
    reply_markup=InlineKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows


    context.bot.send_message(chat_id=chat_id, text="SELECT A PACKAGE",reply_markup=reply_markup)






disp.add_handler(CommandHandler('start', start))




categories = ['BTC MINING', 'CASINO', 'ACCOUNT']
disp.add_handler(CallbackQueryHandler(BTC_MINING, pattern='BTC MINING'))

disp.add_handler(CallbackQueryHandler(CASINO, pattern='CASINO'))

disp.add_handler(CallbackQueryHandler(CASINO, pattern='ACCOUNT'))


mining_plans = ['Mining Plan Bronce', 'Mining Plan Silver', 'Mining Plan Gold', 'Mining Plan Diamond', 'Mining Plan Standard']
disp.add_handler(CallbackQueryHandler(Mining_Plan_Bronze, pattern='Mining Plan Bronze'))
disp.add_handler(CallbackQueryHandler(Mining_Plan_Silver, pattern='Mining Plan Silver'))
disp.add_handler(CallbackQueryHandler(Mining_Plan_Gold, pattern='Mining Plan Gold'))
disp.add_handler(CallbackQueryHandler(Mining_Plan_Diamond, pattern='Mining Plan Diamond'))
disp.add_handler(CallbackQueryHandler(Mining_Plan_Standard, pattern='Mining Plan Standard'))



CASINO_LIST = ['ROLLER COIN', 'FREEBITCOIN', 'BISWAP', 'MOMOverse', 'BETFURY', 'BINANCE', 'COINBASE']

disp.add_handler(CallbackQueryHandler(ROLLER_COIN, pattern='ROLLER COIN'))
disp.add_handler(CallbackQueryHandler(FREEBITCOIN, pattern='FREEBITCOIN'))
disp.add_handler(CallbackQueryHandler(BISWAP, pattern='BISWAP'))
disp.add_handler(CallbackQueryHandler(MOMOverse, pattern='MOMOverse'))
disp.add_handler(CallbackQueryHandler(BETFURY, pattern='BETFURY'))
disp.add_handler(CallbackQueryHandler(BINANCE, pattern='BINANCE'))
disp.add_handler(CallbackQueryHandler(COINBASE, pattern='COINBASE'))

# disp.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
updater.idle()