import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "*YOUR TOKEN*"
bot = telebot.TeleBot(token)
registration_text=[]#список данных
#Below is an example of the structure, you can change the text, URL and number of buttons at your discretion
@bot.message_handler(commands=["start"])
def send(message):
    bot.send_message(message.chat.id, 'Приветствую вас в боте платформы Eduexp!\n🙏 Благодарим за Ваш интерес к повышению квалификации.На связи "ПРИУРАЛЬСКИЙ ЦЕНТР ДОПОЛНИТЕЛЬНОГО ПРОФЕССИОНАЛЬНОГО ОБРАЗОВАНИЯ". У нас более 100 онлайн-курсов. \n 📕 Выдаем документы установленного государством образца, действительные на всей территории РФ, с включением в реестр ФИС ФРДО.\n🎁 Наши ЦЕНЫ существенно НИЖЕ аналогов на рынке, а в июле СКИДКА 50% на ВСЕ ОНЛАЙН-курсы')
    keyboard1 = InlineKeyboardMarkup(row_width=2)
    key_first = InlineKeyboardButton(text='Пиво', callback_data='1')
    keyboard1.add(key_first)
    key_second = InlineKeyboardButton(text='Мясные продукты', callback_data='2')
    keyboard1.add(key_second)
    key_third = InlineKeyboardButton(text='Сыры', callback_data='3')
    keyboard1.add(key_third)
    key_5_kurs = InlineKeyboardButton(text='Овощи', callback_data='4')
    keyboard1.add(key_5_kurs)
    key_6_kurs = InlineKeyboardButton(text='Фрукты', callback_data='5')
    keyboard1.add(key_6_kurs)
    key_7_kurs = InlineKeyboardButton(text='Хлебобулочные изделия', callback_data='6')
    keyboard1.add(key_7_kurs)
    key_8_kurs = InlineKeyboardButton(text='Соки и воды', callback_data='7')
    keyboard1.add(key_8_kurs)
    bot.send_message(message.chat.id, '🏆🏆🏆 Наши направления подготовки:', reply_markup=keyboard1)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_kurses(call):
        if call.data == 'back':
            keyboard1 = InlineKeyboardMarkup(row_width=2)
            key_first = InlineKeyboardButton(text='Пиво', callback_data='1')
            keyboard1.add(key_first)
            key_second = InlineKeyboardButton(text='Мясные продукты', callback_data='2')
            keyboard1.add(key_second)
            key_third = InlineKeyboardButton(text='Сыры', callback_data='3')
            keyboard1.add(key_third)
            key_5_kurs = InlineKeyboardButton(text='Овощи', callback_data='4')
            keyboard1.add(key_5_kurs)
            key_6_kurs = InlineKeyboardButton(text='Фрукты', callback_data='5')
            keyboard1.add(key_6_kurs)
            key_7_kurs = InlineKeyboardButton(text='Хлебобулочные изделия и выпечка', callback_data='6')
            keyboard1.add(key_7_kurs)
            key_8_kurs = InlineKeyboardButton(text='Соки и воды', callback_data='7')
            keyboard1.add(key_8_kurs)
            bot.send_message(message.chat.id, '🏆🏆🏆 Наши направления подготовки:', reply_markup=keyboard1)
        elif call.data == "1":  # call.data это callback_data, которую мы указали при объявлении кнопки
            keyboard1x = InlineKeyboardMarkup(row_width=5)
            key_1x_kurs = InlineKeyboardButton(text='Балтика', url='')
            keyboard1x.add(key_1x_kurs)
            key_2x_kurs = InlineKeyboardButton(text='Клинское', url = '')
            keyboard1x.add(key_2x_kurs)
            key_3x_kurs = InlineKeyboardButton(text='Жигулевское', url = '')
            keyboard1x.add(key_3x_kurs)
            key_4x_kurs = InlineKeyboardButton(text='Amstel безалкогольный', url = '')
            keyboard1x.add(key_4x_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data= 'back')
            keyboard1x.add(back)
            bot.send_message(call.message.chat.id, 'Пиво', reply_markup= keyboard1x)
        elif  call.data == "2":
            keyboard1y = InlineKeyboardMarkup(row_width=4)
            key_1y_kurs = InlineKeyboardButton(text='Куриное филе', url='')
            keyboard1y.add(key_1y_kurs)
            key_2y_kurs = InlineKeyboardButton(text='Колбаса краковская', url='')
            keyboard1y.add(key_2y_kurs)
            key_3y_kurs = InlineKeyboardButton(text='Колбаса вареная', url='')
            keyboard1y.add(key_3y_kurs)
            key_4y_kurs = InlineKeyboardButton(text='Шпикачки', url='')
            keyboard1y.add(key_4y_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard1y.add(back)
            bot.send_message(call.message.chat.id, 'Мясные продукты', reply_markup=keyboard1y)
        elif  call.data == "3":
            keyboard1z = InlineKeyboardMarkup(row_width=6)
            key_1z_kurs = InlineKeyboardButton(text='Гауда', url='')
            keyboard1z.add(key_1z_kurs)
            key_2z_kurs = InlineKeyboardButton(text='Адыгейский', url='')
            keyboard1z.add(key_2z_kurs)
            bot.send_message(call.message.chat.id, 'Сыры', reply_markup=keyboard1z)
        elif  call.data == "4":
            keyboard1q = InlineKeyboardMarkup(row_width=6)
            key_1q_kurs = InlineKeyboardButton(text='Помидоры', url='')
            keyboard1q.add(key_1q_kurs)
            key_2q_kurs = InlineKeyboardButton(text='Огурцы', url='')
            keyboard1q.add(key_2q_kurs)
            key_3q_kurs = InlineKeyboardButton(text='Картофель', url='')
            keyboard1q.add(key_3q_kurs)
            key_4q_kurs = InlineKeyboardButton(text='Чеснок', url='')
            keyboard1q.add(key_4q_kurs)
            key_5q_kurs = InlineKeyboardButton(text='Лук репчатый', url='')
            keyboard1q.add(key_5q_kurs)
            key_6q_kurs = InlineKeyboardButton(text='Болгарский перец', url='')
            keyboard1q.add(key_6q_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard1q.add(back)
            bot.send_message(call.message.chat.id, 'Овощи', reply_markup=keyboard1q)
        elif  call.data == "5":
            keyboard1w = InlineKeyboardMarkup(row_width=6)
            key_1w_kurs = InlineKeyboardButton(text='Яблоки', url='')
            keyboard1w.add(key_1w_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard1w.add(back)
            bot.send_message(call.message.chat.id, 'Фрукты', reply_markup=keyboard1w)
        elif  call.data == "6":
            keyboard1e = InlineKeyboardMarkup(row_width=6)
            key_1e_kurs = InlineKeyboardButton(text='Бородинский хлеб', url='')
            keyboard1e.add(key_1e_kurs)
            key_2e_kurs = InlineKeyboardButton(text='Пшеничный хлеб', url='')
            keyboard1e.add(key_2e_kurs)
            key_3e_kurs = InlineKeyboardButton(text='Галеты с отрубями', url='')
            keyboard1e.add(key_3e_kurs)
            key_4e_kurs = InlineKeyboardButton(text='Пышка с чесноком', url='')
            keyboard1e.add(key_4e_kurs)
            key_5e_kurs = InlineKeyboardButton(text='Ватрушка с яблоком', url='')
            keyboard1e.add(key_5e_kurs)
            key_6e_kurs = InlineKeyboardButton(text='Учпочмак', url='')
            keyboard1e.add(key_6e_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard1e.add(back)
            bot.send_message(call.message.chat.id, 'Хлебобулочные изделия и выпечка', reply_markup=keyboard1e)
        elif  call.data == "7":
            keyboard1r = InlineKeyboardMarkup(row_width=6)
            key_1r_kurs = InlineKeyboardButton(text='Яблочный сок', url='')
            keyboard1r.add(key_1r_kurs)
            key_2r_kurs = InlineKeyboardButton(text='Негазированная вода', url='')
            keyboard1r.add(key_2r_kurs)
            key_3r_kurs = InlineKeyboardButton(text='Газированная вода', url='')
            keyboard1r.add(key_3r_kurs)
            key_4r_kurs = InlineKeyboardButton(text='Квас', url='')
            keyboard1r.add(key_4r_kurs)
            key_5r_kurs = InlineKeyboardButton(text='Помидорный сок', url='')
            keyboard1r.add(key_5r_kurs)
            back = InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard1r.add(back)
            bot.send_message(call.message.chat.id, 'Соки и воды', reply_markup=keyboard1r)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Данный бот был создан для быстрой и простой покупки, для связи с продавцом и покупки продуктов напрямую с Вашего устройства" )

@bot.message_handler(commands=['registration'])
def registration(message):


    keyboard2 = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text='Связаться напрямую с менеджером', url = '')  # кнопка «Да»
    keyboard2.add(yes)  # добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, "Начнем! Вы свяжетесь напрямую с продавом. Нажмите на кнопку ниже\n Вызовите /registration для регистрации на еще один курс\n",
                         reply_markup=keyboard2)


@bot.message_handler(func=lambda message: True, commands=['info'])
def info(message):
    keyboard = InlineKeyboardMarkup(row_width=4)
    key_about_company = InlineKeyboardButton(text='Что мы за компания?', callback_data='about') # кнопка «Да»
    keyboard.add(key_about_company)  # добавляем кнопку в клавиатуру
    key_registration = InlineKeyboardButton(text='Регистрация', callback_data='/registration')
    keyboard.add(key_registration)
    key_vigoda = InlineKeyboardButton(text='В чем примущество покупок у нас', callback_data='pluses')
    keyboard.add(key_vigoda)
    key_operator = InlineKeyboardButton(text='Cвязаться с продавцом',
                                            url='')
    keyboard.add(key_operator)
    bot.send_message(message.chat.id, "Я могу ответить на ваши вопросы. Они представлены ниже списком.\n"
                                      "Для вызова других фукнций бота воспользуйтесь меню рядом со строкой ввода",reply_markup=keyboard)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "about":  # call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'Сельпо у Альберта - самые свежие продукты с быстрой доставкой!')
        elif call.data == "/registration":
            bot.send_message (call.message.chat.id,'/registration')
        elif  call.data == "pluses":
            bot.send_message(call.message.chat.id,'1. Вы сможете приобрести через бота свежие продукты.\n '
                                                  '2. Оформление на сайте. Здесь сугубо список товаров.Сделали бота для того, чтобы было удобно с телефона заказывать продукты, а не мучаться в браузере\n'
                                                  '3. Доставка быстрая. ')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling(none_stop=True, interval=0)
