import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

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
    global help_user_id
    help_user_id = message.from_user.id
    user_id = message.chat.id
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
            # a = telebot.types.ReplyKeyboardRemove()
            # bot.send_message(message.from_user.id, 'Что', reply_markup=a)
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


def pnone_number(message):
    user_data['phone'] = message.text
    if user_data[
        'phone'] != 'ГОТОВНОСТЬ АВТОМОБИЛЯ' and user_data['phone'] != 'ЗАПИСЬ НА ОСМОТР' and user_data[
        'phone'] != 'ЗАПИСЬ НА РЕМОНТ' and user_data['phone'] != 'СТАТУС ЗАКАЗА З/Ч' and user_data[
        'phone'] != 'НАШИ АКЦИИ' and user_data['phone'] != 'НАЧАТЬ ЗАНОВО':
        msg = bot.send_message(message.chat.id, 'ОТЛИЧНО! ТЕПЕРЬ НАПИШИТЕ СВОЁ ФИО')
        bot.register_next_step_handler(msg, name)
    else:
        msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СВОЙ НОМЕР ТЕЛЕФОНА')
        bot.register_next_step_handler(message, pnone_number)


def name(message):
    user_data['name'] = message.text
    if user_data['name'] != 'ГОТОВНОСТЬ АВТОМОБИЛЯ' and user_data['name'] != 'ЗАПИСЬ НА ОСМОТР' and user_data[
        'name'] != 'ЗАПИСЬ НА РЕМОНТ' and user_data['name'] != 'СТАТУС ЗАКАЗА З/Ч' and user_data[
        'name'] != 'НАШИ АКЦИИ' and user_data['name'] != 'НАЧАТЬ ЗАНОВО':
        msg = bot.send_message(message.chat.id, 'ПРИНЯТО! ТЕПЕРЬ УКАЖИТЕ ГОСНОМЕР СВОЕГО АВТОМОБИЛЯ')
        bot.register_next_step_handler(msg, car)
    else:
        msg = bot.send_message(message.chat.id, 'НАПИШИТЕ СВОЁ ФИО')
        bot.register_next_step_handler(message, name)


def car(message):
    user_data['car_number'] = message.text
    if user_data['car_number'] != 'ГОТОВНОСТЬ АВТОМОБИЛЯ' and user_data['car_number'] != 'ЗАПИСЬ НА ОСМОТР' and \
            user_data['car_number'] != 'ЗАПИСЬ НА РЕМОНТ' and user_data['car_number'] != 'СТАТУС ЗАКАЗА З/Ч' and \
            user_data['car_number'] != 'НАШИ АКЦИИ' and user_data['car_number'] != 'НАЧАТЬ ЗАНОВО':
        bot.send_message('@yam_chat_2',f'{message.chat.id}'+ ' ' +
                         user_data['Choice'] +
                         "\nклиент " + user_data['name'] +
                         "\nтелефон " + user_data['phone'] +
                         "\nгосномер " + user_data['car_number'])

        bot.send_message(message.chat.id,
                         'Ваша заявка принята - ожидайте ответа специалиста!'.format(message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=None)
        response(message)
    else:
        msg = bot.send_message(message.chat.id, 'УКАЖИТЕ ГОСНОМЕР СВОЕГО АВТОМОБИЛЯ')
        bot.register_next_step_handler(message, car)
    # RUN
def response(message):
    global user_id


    msg = bot.send_message('@yam_chat_2', 'введи ответ')
    bot.forward_message('@yam_chat_2', message.chat.id, message.message_id)
    bot.register_next_step_handler_by_chat_id(help_user_id, handle_text)

# def forward_usr_1(message):
#     global user_id
#     print('forward_usr_1')
#
#     print(message.chat.id)
#     bot.send_message(message.chat.id, '{}'.format(message))


@bot.message_handler(content_types=["text"])


def handle_text(message):
    global help_user_id
    print(help_user_id)
    print(message.chat.id)

   # здесь если чат id равен id чата поддержки, то отправить сообщение пользователю который задал вопрос
    if int(message.chat.id) == int(-1001610130184):
      bot.send_message(help_user_id, message.text)
    else:
        handle_text(message)



bot.polling(none_stop=True)
