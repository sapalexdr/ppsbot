from collections import defaultdict
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, CallbackQuery
from datetime import datetime
from PIL import Image
import random
from datetime import datetime
from PIL import Image
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
import asyncio


API_TOKEN = "7084259947:AAE892TrZ7i2FBTrf1d2uBuFlOVAY8ITMFM"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage= storage)




async def set_default_commands(dp):
    await dp.bot.set_my_commands([types.BotCommand("start", "start")])


async def on_startup(dp):
    await set_default_commands(dp)
    print("App.py is running!")
    




emoji_list = [
    "🐀",
    "🐁",
    "🐂",
    "🐃",
    "🐄",
    "🐅",
    "🐆",
    "🐇",
    "🐈‍⬛",
    "🐈",
    "🐉",
    "🐊",
    "🐋",
    "🐌",
    "🐍",
    "🐎",
    "🐏",
    "🐐",
    "🐑",
    "🐒",
    "🐓",
    "🐔",
    "🐕‍🦺",
    "🐕",
    "🐖",
    "🐗",
    "🐘",
    "🐙",
    "🐚",
    "🐛",
    "🐜",
    "🐝",
    "🐞",
    "🐟",
    "🐠",
    "🐡",
    "🐢",
    "🐣",
    "🐤",
    "🐥",
    "🐦",
    "🐧",
    "🐨",
    "🐩",
    "🐪",
    "🐫",
    "🐬",
    "🐭",
    "🐮",
    "🐯",
    "🐰",
    "🐱",
    "🐲",
    "🐳",
    "🐴",
    "🐵",
    "🐶",
    "🐷",
    "🐸",
    "🐹",
    "🐺",
    "🐻‍❄️",
    "🐻",
    "🐼",
    "🐽",
    "🐾",
    "🐿️",
    "🦀",
    "🌳",
    "🌴",
    "🌻",
    "🌺",
]


b = KeyboardButton(text='кто я?')
c = KeyboardButton(text="фоточку!")
a = ReplyKeyboardMarkup(keyboard=[[b],[c]], resize_keyboard=True)


@dp.message_handler(Command("start"))
async def answer(message: types.Message):

    user_id = message.from_user.id


    if user_id == 238615190 or 1063083555:
        to_pin = await message.answer(
            text="привет, заечька!\n\nэтот бот будет показывать фотографии (почти четыре тыщи, и это только из нашей папочки и без видево), которые так или иначе связаны с нашим времяпрепровождением!\n\nа еще может всячеки называть тебя из почти 30 ласковых имен! слава богу теперь есть из чего выбирать, а не как в первое утро))\n"
            "\nжми кнопочьки!\n\nа из новых функций появилась новая команда /businka!\nраз на цветочке места не хватило, пусть будет тутб тогда!\nтупо может конечно, но мне понравился видосик сори(\n\n\n__\nа если кнопочьки пропали, то нажми еще раз /start", reply_markup=a
        )
        await bot.pin_chat_message(chat_id=user_id, message_id=to_pin.message_id)
        
    else:
        await message.answer(text="бот не для тебя(")
        
@dp.message_handler(commands=['businka'])
async def secret_commanddsf(message: types.Message):
    loveya = "hiiiii\n\nin case you haven't heard in a while\n\n\ni love you\n\n\ndo you hear me?\n\nuncoditionally\nand irrefutably\n\nand not just because you are hot+cool+smart+funny\n\ni love you because i see you and know you\n\nunderneath the mask\nunderneath society's expectations of what it takes to be 'conventionally loveable'\n\nyou don't have to do anything\nor be anythig\nfor me to love you\n\ni just do\n\nand i want us to get to share this weird cool mysterious existence\ntogether\n\n\nlove you businka\n\n"
    user_id = message.from_user.id
    if user_id == 238615190 or 1063083555:
        response = await message.answer(text=loveya)
        await asyncio.sleep(3.5)
        await response.delete()
        await message.delete()
        
        


def dms_to_dd(d, m, s, ref):
    d = float(d)
    m = float(m)
    s = float(s)
    dd = d + m / 60 + s / 3600
    if ref in ['S', 'W']:
        dd *= -1
    return dd



@dp.message_handler(text="фоточку!")
async def sendphoto(message: types.Message, state: FSMContext):
    user_id = message.from_user.id


    if user_id == 238615190 or user_id == 1063083555:
        emoji_string = " ".join(random.sample(emoji_list, 2))
        pic_id = random.randint(1, 2818)
        photo_path = f"output_folder/img_{pic_id}.jpg"

        try:
            img = Image.open(photo_path)
            exif_data = img._getexif()
            date = exif_data.get(36867)
            person = exif_data.get(272)

            if date:
                date = datetime.strptime(
                    date, "%Y:%m:%d %H:%M:%S").strftime("%d %B, %H:%M")
                
                
                
            gps_info = exif_data.get(34853)
            if gps_info:
                
                gps_latitude = gps_info.get(2)
                gps_latitude_ref = gps_info.get(1)
                gps_longitude = gps_info.get(4)
                gps_longitude_ref = gps_info.get(3)

                latitude = dms_to_dd(
                    gps_latitude[0], gps_latitude[1], gps_latitude[2], gps_latitude_ref)
                longitude = dms_to_dd(
                    gps_longitude[0], gps_longitude[1], gps_longitude[2], gps_longitude_ref)
                geo_send = InlineKeyboardMarkup()
                geo_suggest = InlineKeyboardButton(text='ой а где это?', callback_data='где')
                geo_send.add(geo_suggest)
                await state.set_data([latitude, longitude])
                
                



            if person == 'iPhone 11':
                person = 'фото с каришкиного телефона'
            elif person == 'iPhone 12':
                person = 'фото с сашиного телефона'

            caption = f"{emoji_string}\n{date}\n{person}"
            with open(photo_path, "rb") as photo:
                await bot.send_photo(user_id, photo, caption=caption, reply_markup=geo_send)

        except (FileNotFoundError, KeyError):
            await message.answer(text="ой, чето не получилось, нажми еще раз плиз бейб")
    else:
        await message.answer(text="бот не для тебя(")


shown_names = defaultdict(set)

@dp.callback_query_handler(text = "где")
async def send_geo(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await dp.bot.send_location(chat_id= call.from_user.id, latitude=data[0], longitude=data[1])
    

@dp.message_handler(text="кто я?")
async def answer(message: types.Message):
    user_id = message.from_user.id
    pretty_names = [
        "сильная и крутая!",
        "мощный котенок с огромными лапищами"
        "милашка",
        "зая",
        "балбесина)",
        "балбеска))",
        "котя",
        "бейба))",
        "секси крошка.",
        "хорошуля!",
        "карина шихгасанова.",
        "кариша!",
        "кариночка...",
        "заечка!!",
        "заечька",
        "пупс",
        "пупсик из пупсиков",
        "кариночька",
        "каришка",
        "сладуся",
        "любимка",
        "пупупуня",
        "солнышко",
        "детка бейба",
        "соска нереалка",
        "любимочка",
        "малышкабейба", 
        "... неважно как тебя назовет бот сейчас, важно как ты будешь стонать когда я буду трахать тебя в [name the city babe]",
        "морковкина",
        "любимкина",
        "\любимкаю тебя. ой не совсем имя)))"
    ]

    if user_id == 238615190 or user_id == 1063083555:
        available_names = list(set(pretty_names) - shown_names[user_id])

        if not available_names:
            shown_names[user_id].clear()
            available_names = pretty_names

        if available_names:
            chosen_name = random.choice(available_names)
            shown_names[user_id].add(chosen_name)

            await message.answer(text=f"ты {chosen_name}")
        else:
            await message.answer(text="Something went wrong. Please try again.")
    else:
        await message.answer(text="бот не для тебя(")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)