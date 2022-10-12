import telebot
from telebot import types
from collections import defaultdict
import config

bot = telebot.TeleBot(config.TOKEN)
callback_data = ''
number = ''
# user_by_messages = defaultdict(list)
# messages = []
# text = ''
discount = '1. Окраска одной детали 9 500 руб.* (без учета расходных материалов и доп работ по детали).\n2. Акция - "Заяви страховой случай по УУУ (СК: Ингосстрах, РЕСО, ВСК, АльфаСтрахование), выбери подарок":\n           А. Карта постоянного клиента GOLD (скидка: работы - 10%, З/Ч - 10%);\n          Б. Озонированние.\n3. Удаление вмятин без окраски  от 999 руб.\n4. Керамическое покрытие кузова от 19 900 руб.'
user_data = {
    'Choice': '',
    'name': '',
    'phone': '',
    'car_number': ''
}


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('ГОТОВНОСТЬ АВТОМОБИЛЯ')
    item2 = types.KeyboardButton('ЗАПИСЬ НА ОСМОТР')
    item3 = types.KeyboardButton('ЗАПИСЬ НА РЕМОНТ')
    item4 = types.KeyboardButton('СТАТУС ЗАКАЗА З/Ч')
    item5 = types.KeyboardButton('НАШИ АКЦИИ')
    item6 = types.KeyboardButton('НАЧАТЬ ЗАНОВО')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id,
                     "Компания Вист-Авто приветствует Вас, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный специально для Вас.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'ГОТОВНОСТЬ АВТОМОБИЛЯ':
            user_data['Choice'] = message.text
            msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
            bot.register_next_step_handler(message, pnone_number)
        elif message.text == 'ЗАПИСЬ НА ОСМОТР':
            user_data['Choice'] = message.text
            msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
            bot.register_next_step_handler(message, pnone_number)
        if message.text == 'ЗАПИСЬ НА РЕМОНТ':
            user_data['Choice'] = message.text
            msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
            bot.register_next_step_handler(message, pnone_number)
        if message.text == 'СТАТУС ЗАКАЗА З/Ч':
            user_data['Choice'] = message.text
            msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
            bot.register_next_step_handler(message, pnone_number)
        if message.text == 'НАЧАТЬ ЗАНОВО':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ГОТОВНОСТЬ АВТОМОБИЛЯ')
            item2 = types.KeyboardButton('ЗАПИСЬ НА ОСМОТР')
            item3 = types.KeyboardButton('ЗАПИСЬ НА РЕМОНТ')
            item4 = types.KeyboardButton('СТАТУС ЗАКАЗА З/Ч')
            item5 = types.KeyboardButton('НАШИ АКЦИИ')
            item6 = types.KeyboardButton('НАЧАТЬ ЗАНОВО')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id,
                             "Компания Вист-Авто приветствует Вас, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный специально для Вас.".format(
                                 message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        if message.text == 'НАШИ АКЦИИ':
            bot.send_message(message.chat.id, discount)

        else:
            pass

# def call_back_func(call):
#     menu1 = telebot.types.InlineKeyboardMarkup()
#     menu1.add(telebot.types.InlineKeyboardButton(text='ЗАКАЗАТЬ ОБРАТНЫЙ ЗВОНОК', callback_data='first'))
#     if callback_data == 'first':
#         #user_data['Choice'] = call.text
#         msg = bot.send_message(call.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
#         bot.register_next_step_handler(call, pnone_number)
#    else:
   #     pass


def pnone_number(message):
    user_data['phone'] = message.text
    msg = bot.send_message(message.chat.id, 'НАПИШИТЕ СВОЁ ФИО')
    bot.register_next_step_handler(msg, name)


def name(message):
    user_data['name'] = message.text
    msg = bot.send_message(message.chat.id, 'УКАЖИТЕ ГОСНОМЕР СВОЕГО АВТОМОБИЛЯ')
    bot.register_next_step_handler(msg, car)


def car(message):
    user_data['car_number'] = message.text
    bot.send_message('@yam_cha',
                     user_data['Choice'] +
                     "\nклиент " + user_data['name'] +
                     "\nтелефон " + user_data['phone'] +
                     "\nгосномер " + user_data['car_number'])
    bot.send_message(message.chat.id,
                     'Ваша заявка принята - ожидайте ответа специалиста!'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=None)

    # RUN


bot.polling(none_stop=True)
