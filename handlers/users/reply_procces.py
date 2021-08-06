import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from handlers.users.bis_parser import bis
from handlers.users.long_list_parser import long_list
from handlers.users.news_parser import text_link_headers
from keyboards.inline.about_parser import about_content
from keyboards.inline.blanks import message

from keyboards.inline.buttons import start, long_term, chengen_back, viza_info, get_notified, \
    get_back_to_mailing, back_to_another, \
    backtovizainfo1, back_to_long_term, menu, back_to_start, another2, get_back_from_education, backtostart1
from keyboards.inline.center import center_c
from keyboards.inline.constant_living_parser import constant
from keyboards.inline.country_list_parser import clist
from keyboards.inline.differ_parser import differ
from keyboards.inline.fee import fee_list
from keyboards.inline.long_living_parser import long
from keyboards.inline.sport_paser import sport

from loader import dp

from keyboards.inline.covid_parser import list5, get_covid_article
from keyboards.inline.cul_parser import cul
from keyboards.inline.events_parser import events
from keyboards.inline.polit_parser import polit
from keyboards.inline.trade_parser import trade_articels
from keyboards.inline.shengen_articles_parser import shengen_articels


dp.message_handler()

latest_msg = None


@dp.callback_query_handler(text_contains="education_cz")  # made callback for button which gets you back from education to long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    d = "https://telegra.ph/Obuchenie-08-05-3"
    msg = await call.message.answer(d, reply_markup=get_back_from_education)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")



@dp.message_handler(Command("start"))  # made introduction and logic of collecting user's data
async def show_items(message: Message):
    msg = await message.answer(
        text="Доброго времени суток, юзеры.\nДанный бот призван облегчить ваш процесс работы с посольством Чешской Республики в Москве \n"
             "Для начала работы выберете топик снизу", reply_markup=start)
    global latest_msg
    latest_msg = msg


@dp.callback_query_handler(text_contains="basic info")
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    basic_content2 = "https://telegra.ph/Konsulskij-otdel-08-06"
    text = basic_content2
    msg = await call.message.answer(text, reply_markup=backtostart1)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="main viza info")  # made callback for button which gives options of different types of vizas
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="long term viza")  # made callback for long term viza button which gives as set of buttons with types of long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="news_list")  # made call back for buttton which gives you list of news
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for i in text_link_headers:
        text += i + "(" + text_link_headers[i] + ")" + "\n" + "\n"

    msg = await call.message.answer(text,
                              reply_markup=get_back_to_mailing)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="subagain")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=get_notified)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="backrt")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="long_list")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for i in long_list:
        text += i + "(" + long_list[i] + ")""\n""\n"

    msg = await call.message.answer(text,
                              reply_markup=get_back_from_education)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="bis")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(bis,
                              reply_markup=get_back_from_education)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="blanks")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(message,
                              reply_markup=backtovizainfo1)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="aback1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="getbacklong")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="sport1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(sport,
                              reply_markup=back_to_long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="family1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    family = "https://telegra.ph/S-celyu-soedineniya-semi-08-06"
    msg = await call.message.answer(family, reply_markup=backtovizainfo1)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="how differ1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(differ,
                              reply_markup=back_to_long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="56")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="to subscribe")  # made call back for buttton which gives you list of news
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Вы подписаны на рассылку новостей",
                              reply_markup=get_notified)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="get back to long viza")  # made callback for button which gets back to long viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="back_to_start")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer('Выберете направление',
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="another2")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=another2)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="covid")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for n, i in enumerate(list5):
        text += str(n + 1) + ". " + i + "\n(" + list5[i] + ")" + "\n\n"
    msg = await call.message.answer(text,
                              reply_markup=back_to_start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="getback")  # made callback for button get back to start
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer('Выберете направление',
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="events")  # made callback for button which gives event's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(events,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="polit")  # made callback for button which gives polit content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text1 = ""
    for i in polit:
        text1 += i + "(" + polit[i] + ")\n" + '\n'
    msg = await call.message.answer(text1,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="trade")  # made callback for button which gives trade's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text1 = ""
    for i in trade_articels:
        text1 += i + "(" + trade_articels[i] + ")\n" + '\n'
    msg = await call.message.answer(text1,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="cul")  # made callback for button which gives culture's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(cul,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="war")  # made callback for button which gives war's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    fr = "https://telegra.ph/CHehi-vo-vtoroj-mirovoj-vojne-08-05"
    msg = await call.message.answer(fr,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="about")  # made callback for button which gives about's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(about_content,
                              reply_markup=back_to_another)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="startback")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="aback")  # made callback for all another buttons
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer('Выберете направление',
                              reply_markup=another2)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="get_back_to_start")  # made callback to start from getting notified
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Вы успешно отписались",
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="get back to viza info")  # made callback for button of educational purpose returns back to long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="basic")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    basic_content = "https://telegra.ph/Osnovnaya-vizovaya-informaciya-08-06"
    msg = await call.message.answer(basic_content, reply_markup=backtovizainfo1)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="constant")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for i in constant:
        text += i + "(" + constant[i] + ")" + "\n\n"
    msg = await call.message.answer(text,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="long_live")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for i in long:
        text += i + "(" + long[i] + ")" + "\n" + "\n"
    msg = await call.message.answer(text,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="country_list")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(clist,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="fee")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(fee_list,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="viza_center")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer(center_c,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="another")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=another2)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="bacs")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="vb")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(text_contains="get_back")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Выберете направление",
                              reply_markup=start)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="shengen")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    text = ""
    for i in shengen_articels:
        text += i + "(" + shengen_articels[i] + ")" + "\n" + "\n"
    msg = await call.message.answer(text,
                              reply_markup=chengen_back)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")


@dp.callback_query_handler(
    text_contains="chengen back")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)

    msg = await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
    global latest_msg
    try:
        await latest_msg.delete()
        latest_msg = msg
    except Exception as e:
        logging.warning(f"During {call.data} there was exception {e}")
