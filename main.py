import telebot,time
from threading import Thread

bot = telebot.TeleBot('Вставьте токен')


users={}

#-------------------------------------------- THREAD--------------------------------

BOSS=[]



def Arej():
    global BOSS
    global hrams
    while True:
        if len (BOSS)==1:
            bot.send_message(BOSS[0],'ВСЁ ОК')
            time.sleep(60*60*24)
        else:
            continue

        
Thread(target=Arej).start()
#------------------------------------------------------DELETE FROM TALK------------------------------------------------   
def delet(message):
    global talk
    if message.chat.id in talk:
            del talk[message.chat.id]
    else:
        for i,number  in list(talk.items()):
            if talk.get(i)==message.chat.id:
                del talk[i]


#-------------------------------------------START OR HELP OR STOP---------------------------------------------------------------
@bot.message_handler(commands=['start','help'])

def start(message):

    markup=telebot.types.InlineKeyboardMarkup()
    
    markup.row(telebot.types.InlineKeyboardButton('Здравоохранение 🚑',callback_data='sos'))

    markup.row(telebot.types.InlineKeyboardButton('Общепит 🍽',callback_data='lunch'))

    markup.row(telebot.types.InlineKeyboardButton('Ночлег 🛌',callback_data='night'))

    markup.row(telebot.types.InlineKeyboardButton('Гид 🗺',callback_data='gid'))

    markup.row(telebot.types.InlineKeyboardButton('Справочники ℹ️',callback_data='info'))

    markup.row(telebot.types.InlineKeyboardButton('Чат 🤚',callback_data='chat'))
    delet(message)

    if message.from_user.last_name is None:
        bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)
        if message.chat.id not in users:
            users[message.chat.id]=f'{message.from_user.first_name}'
            print(users)
    else:
        bot.send_message(message.chat.id,f'Привет {message.from_user.first_name} {message.from_user.last_name}', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)
        if message.chat.id not in users:
            users[message.chat.id]=f'{message.from_user.first_name} {message.from_user.last_name}'
            print(users)




#---------------------------------------------------------------CALLBACK----------------------------------------------------
hrams={}
@bot.callback_query_handler(func=lambda callback:True)
def on_click(callback):
    global talk
    global hrams

    if callback.data=='sos':
        delet(callback.message)
        bot.send_message(callback.message.chat.id, f'Что случилось, {users.get(callback.message.chat.id)}?😨\n'
        +'‼️Скорей обращайся по адрессу ниже, со здоровьем не шутят\n\n'

        +'Краевая клиническая больница №1\n'
        + '☎️ +7 (861) 252‒73‒41\n' 
        +'📍ул. 1 Мая, 167\n\n'

        +'Клиническая больница скорой медицинской помощи\n' 
        +'☎️ +7 (861) 252‒16‒79\n'
        +'📍ул. 40-летия победы. 14\n\n'

       + 'Специализированная клиническая инфекционная больница\n'
       +'☎️ +7 (861) 255‒45‒69\n'
        +'📍ул. Седина, 204\n\n'

       + 'Детская краевая клиническая больница \n'
       +'☎️ +7 (861) 290‒00‒95\n'
        +'📍ул. Постовая, 18\n\n'

        +'Краевая клиническая больница №2\n '
        +'☎️ +7 (861) 222‒00‒02\n'
       + '📍ул. Красных Партизан, 6/2',reply_markup=telebot.types.ReplyKeyboardRemove())
    elif callback.data=='lunch':
        delet(callback.message)
        buton=telebot.types.InlineKeyboardMarkup()
        buton.row(telebot.types.InlineKeyboardButton('Рестораны',url='https://www.tripadvisor.ru/FindRestaurants?geo=298532&establishmentTypes=10591&broadened=true'))
        buton.row(telebot.types.InlineKeyboardButton('Кафе',url='https://www.tripadvisor.ru/Restaurants-g298532-c8-Krasnodar_Krasnodar_Krai_Southern_District.html'))
        buton.row(telebot.types.InlineKeyboardButton('Десерты',url='https://www.tripadvisor.ru/FindRestaurants?geo=298532&establishmentTypes=9909&broadened=false'))
        bot.send_message(callback.message.chat.id,f'Привет {users.get(callback.message.chat.id)}!',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(callback.message.chat.id,'Хочешь вкусно и недорого поесть?',reply_markup=buton)
    elif callback.data=='night':
        delet(callback.message)
        bot.send_message(callback.message.chat.id,'Ищешь где остановиться?',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(callback.message.chat.id,'Смело преходи по ссылке ниже👇',reply_markup=telebot.types.InlineKeyboardMarkup().add(telebot.types.InlineKeyboardButton('Tripadvisor.ru',url='https://www.tripadvisor.ru/Hotels-g298532-Krasnodar_Krasnodar_Krai_Southern_District-Hotels.html')))
    elif callback.data=='gid':
        delet(callback.message)
        inline=telebot.types.InlineKeyboardMarkup()
        inline.row(telebot.types.InlineKeyboardButton('Парк им. Галицкого', url='https://youtu.be/4eOq09v4pIM?si=znrvYYyc2p3eiNjR'))
        inline.row(telebot.types.InlineKeyboardButton('Парк им. Галицкого. Японский сад', url='https://youtu.be/ev68wGbdOwc?si=doJqcTfjJN9bFWa9'))
        inline.row(telebot.types.InlineKeyboardButton('Парк им. Галицкого', url='https://youtu.be/4eOq09v4pIM?si=znrvYYyc2p3eiNjR'))
        inline.row(telebot.types.InlineKeyboardButton('Экскурсия', callback_data='add'))
        bot.send_message(callback.message.chat.id,f'{users.get(callback.message.chat.id)}, что тебя интересует? Выбирай!',reply_markup=inline)
        # bot.send_message(callback.message.chat.id,'Ищешь где остановиться?',reply_markup=telebot.types.ReplyKeyboardRemove())
    elif callback.data=='info':
        delet(callback.message)
        info=telebot.types.InlineKeyboardMarkup()
        b1=telebot.types.InlineKeyboardButton('Транспорт',url='http://krd.rusavtobus.ru/')
        b2=telebot.types.InlineKeyboardButton('Аэропорт',url='https://krr.aero/flights/online-schedule/')
        b3=telebot.types.InlineKeyboardButton('Поезда',url='https://www.tutu.ru/poezda/station_d.php?nnst=2064788')
        b4=telebot.types.InlineKeyboardButton('TEST',url='https://www.pythonanywhere.com/user/NekN/consoles/34113814/')
        info.row(b1)
        info.row(b2)
        info.row(b3)
        info.row(b4)
        bot.send_message(callback.message.chat.id,'Что тебя интересует?',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(callback.message.chat.id,'Выберите из списка ниже',reply_markup=info)
    elif callback.data=='chat':
        markup=telebot.types.InlineKeyboardMarkup()
        markup.row(telebot.types.InlineKeyboardButton('Начать поиск',callback_data='next'))
        bot.send_message(callback.message.chat.id,'Подключение к чату....',reply_markup=markup)
        bot.register_next_step_handler(callback.message,find)
    elif callback.data=='next':
        bot.send_message(callback.message.chat.id,'Выполняется поиск......',reply_markup=telebot.types.ReplyKeyboardMarkup().add(telebot.types.KeyboardButton('отмена')))
        time.sleep(2)
        bot.register_next_step_handler(callback.message,start)
        find(callback.message) 
    elif callback.data=='add':
        btn=telebot.types.InlineKeyboardMarkup()
        btn.row(telebot.types.InlineKeyboardButton('Церкви Краснодара',callback_data='hram'))
        bot.send_message(callback.message.chat.id,f'{users.get(callback.message.chat.id)} Выбери из списка ниже',reply_markup=btn)
    elif callback.data=='hram':
        btn=telebot.types.InlineKeyboardMarkup()
        btn.row(telebot.types.InlineKeyboardButton('Я на месте',callback_data='hram2'))
        file=open('st.jpg','rb')
        bot.send_photo(callback.message.chat.id,file)
        bot.send_message(callback.message.chat.id, 'Первое место назначения Свято-Георгиевский храм, \nрасположенный по адрусу [ул. Митрофана Седина, 170](https://2gis.ru/krasnodar/firm/3237490513164152?m=39.149897%2C44.971854%2F11)',
                         parse_mode='Markdown',disable_web_page_preview=True,reply_markup=btn)
    elif callback.data=='hram2':
        btn=telebot.types.InlineKeyboardMarkup()
        btn.row(telebot.types.InlineKeyboardButton('Я на месте',callback_data='hram3'))
        bot.send_message(callback.message.chat.id,f'Отлично {users.get(callback.message.chat.id)}! Гуляй и наслаждайся!\n Обязательно посмотри видео-экскурсию!')
        bot.send_message(callback.message.chat.id,'https://youtu.be/SrQjWd1mzzs?si=GZOsYA72j-2TMLw_')
        bot.send_message(callback.message.chat.id, 'Затем посети Храм Архистратига Михаила, \nрасположенный по адрусу [ул. Березанская, 89/1](https://2gis.ru/krasnodar/firm/3237490513465492?m=38.998839%2C45.040553%2F16)',
                         parse_mode='Markdown',disable_web_page_preview=True,reply_markup=btn)
    elif callback.data=='hram3':
        bot.send_message(callback.message.chat.id,f'Отлично {users.get(callback.message.chat.id)}! Гуляй и наслаждайся!\n Обязательно посмотри видео-экскурсию!')
        bot.send_message(callback.message.chat.id,'https://youtu.be/3-lWObhRQpQ?si=2cwWycRlLCEqAPBg')


        


#------------------------------------------------ANON CHAT---------------------------------------------------------------------------
talk={}
flag=[]
def find(message):
    global talk
    global flag
    print(message.chat.id)
    if len(talk)!=0:
        for i,n in list(talk.items()):
            if talk.get(i)==None and i!=message.chat.id and message.chat.id in flag:
                but=telebot.types.ReplyKeyboardMarkup()
                but.row(telebot.types.KeyboardButton('stop'))
                bot.send_message(i,"Собеседник найден!!!",reply_markup=but)
                bot.send_message(message.chat.id,"Собеседник найден!!!",reply_markup=but)
                print(talk.get(i),n,i,message.chat.id)
                talk[i]=message.chat.id
                break
        else:
            talk[message.chat.id]=None
   
    else:
        talk[message.chat.id]=None
@bot.message_handler()
def sell(message):
    global talk
    global BOSS
    global spiski
    global registration
    
 
    if message.text=='stop' and len(talk)!=0:
        print(f'{message.chat.id} stop')
        markup=telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('ДА',callback_data='next'))

        if message.chat.id in talk and talk[message.chat.id]!=None:
            bot.send_message(message.chat.id,"Собеседник покинул чат:(",reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(talk.get(message.chat.id),"Собеседник покинул чат:(",reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id,"Продолжить поиск?",reply_markup=markup)
            bot.send_message(talk.get(message.chat.id),"Продолжить поиск?",reply_markup=markup)
            del talk[message.chat.id]
        else:
            for i,number  in list(talk.items()):
                if talk.get(i)==message.chat.id:
                    bot.send_message(message.chat.id,"Собеседник покинул чат:(",reply_markup=telebot.types.ReplyKeyboardRemove())
                    bot.send_message(i,"Собеседник покинул чат:(",reply_markup=telebot.types.ReplyKeyboardRemove())
                    bot.send_message(message.chat.id,"Продолжить поиск?",reply_markup=markup)
                    bot.send_message(i,"Продолжить поиск?",reply_markup=markup)
                    del talk[i]

    elif message.text=="NekNArej.4606":
        print(BOSS)
        if len(BOSS)==0:
            BOSS.append(message.chat.id)
            print('BOSS в чате',BOSS)
    elif message.text=='stop boss':
        BOSS.clear()
    


    else :

        if message.chat.id in talk and talk[message.chat.id]!=None:
            print(f"{message.chat.id} talk to {talk.get(message.chat.id)}")
            bot.send_message(talk.get(message.chat.id),message.text)
        else:
            for i in talk:
                if talk.get(i)==message.chat.id:
                 
                    print(f"{message.chat.id} talk to {i}")
              
                    bot.send_message(i,message.text)
    







#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------





bot.infinity_polling(none_stop=True)









