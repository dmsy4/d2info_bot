import telebot
import parsing

bot = telebot.TeleBot('config.token')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Чтобы посмотреть доступные функции напиши /help')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/MMR_ladder', '/counter_picks')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('/Europe', '/SE_Asia', '/Americas', '/China')

@bot.message_handler(commands=['help'])
def abilities(message):
    bot.send_message(message.chat.id, 'На цифровой клавиатуре отображены доступные функции', reply_markup=keyboard1)

@bot.message_handler(commands=['MMR_ladder'])
def foo_ladder(message):
     bot.send_message(message.chat.id, 'Выбери регион', reply_markup=keyboard2)

@bot.message_handler(commands=['Europe', 'SE_Asia', 'Americas', 'China'])
def foo_ladder_region(message):
     answer = parsing.region_ladder((message.text[1:]).lower())
     bot.send_message(message.chat.id, answer)





bot.polling()