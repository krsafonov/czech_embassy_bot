import logging
import typing

from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram import types

from handlers.users.news_parser import get_headers
from keyboards.inline.blanks import message
from keyboards.inline.calback_data import get_callback
from keyboards.inline.buttons import start, long_term, covid_measures, viza2_info, \
    chengen_back, viza_info, transformed_viza_info, viza_info2, get_notified, get_back_to_start, \
    get_back_to_start_from_covid, get_back_to_mailing, get_back_from_education, another1, back_to_another, \
    backtovizainfo1, back_to_long_term, get_back_from_covid, backtostart1
from loader import dp, bot

from keyboards.inline.covid_parser import list5
from keyboards.inline.cul_parser import cul
from keyboards.inline.events_parser import events
from keyboards.inline.polit_parser import polit
#from keyboards.inline.shengen_articles_parser import shengen_articels
from keyboards.inline.trade_parser import trade_articels

dp.message_handler()

latest_msg = None

@dp.message_handler(Command("start"))  # made introduction and logic of collecting user data
async def show_items(message: Message):
    f = open("log", "a", encoding='utf-8')
    f.write(str(message.chat.id) + " " + message.from_user.username + " " + message.from_user.first_name + "\n")
    f.close()
    global latest_msg
    latest_msg = await message.answer(
        text="Доброго времени суток, юзеры.\nДанный бот призван облегчить ваш процесс работы с посольством Чешской Республики в Москве \n"
             "Для начала работы выберете топик снизу", reply_markup=start)



@dp.callback_query_handler(text_contains="basic info")
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await latest_msg.delete_reply_markup()
    await call.message.answer(message,
                              reply_markup=backtostart1)



@dp.callback_query_handler(
    text_contains="main viza info")  # made callback for button which gives options of different types of vizas
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    #await latest_msg.delete_reply_markup()
    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)


@dp.callback_query_handler(text_contains="to subscribe")  # made callback for button which makes you notified
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы подписаны",
                              reply_markup=get_notified)


@dp.callback_query_handler(
    text_contains="long term viza")  # made callback for long term viza button which gives as set of buttons with types of long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)


@dp.callback_query_handler(text_contains="news_list")  # made call back for buttton which gives you list of news
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(get_headers(),
                              reply_markup=get_back_to_mailing)


@dp.callback_query_handler(text_contains="blanks")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=backtovizainfo1)


@dp.callback_query_handler(text_contains="aback1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)


@dp.callback_query_handler(text_contains="basic")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=backtovizainfo1)

@dp.callback_query_handler(text_contains="getbacklong")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)


@dp.callback_query_handler(text_contains="sport1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=back_to_long_term)


@dp.callback_query_handler(text_contains="family1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=back_to_long_term)


@dp.callback_query_handler(text_contains="how differ1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=back_to_long_term)

@dp.callback_query_handler(text_contains="56")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)



@dp.callback_query_handler(text_contains="subagain")  # made call back for buttton which gives you list of news
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы подписаны на рассылку новостей",
                              reply_markup=get_notified)


@dp.callback_query_handler(
    text_contains="get back to long viza")  # made callback for button which gets back to long viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Долгосрочная виза",
                              reply_markup=transformed_viza_info)



@dp.callback_query_handler(text_contains="covidback")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer('Выберете направление',
                              reply_markup=start)


@dp.callback_query_handler(text_contains="covid")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(list5,
                              reply_markup=get_back_from_covid)





@dp.callback_query_handler(text_contains="getback")  # made callback for button get back to start
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer('Выберете направление',
                              reply_markup=start)



@dp.callback_query_handler(text_contains="events")#made callback for button which gives event's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(events,
                              reply_markup=back_to_another)


@dp.callback_query_handler(text_contains="polit")#made callback for button which gives polit content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(polit,
                              reply_markup=back_to_another)


@dp.callback_query_handler(text_contains="trade")#made callback for button which gives trade's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(trade_articels(),
                              reply_markup=back_to_another)


@dp.callback_query_handler(text_contains="cul")#made callback for button which gives culture's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(cul,
                              reply_markup=back_to_another)

"""@dp.callback_query_handler(text_contains="war")#made callback for button which gives war's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(None,
                              reply_markup=back_to_another)
"""


"""@dp.callback_query_handler(text_contains="about")#made callback for button which gives about's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(None,
                              reply_markup=back_to_another)"""


@dp.callback_query_handler(text_contains="startback")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=start)




@dp.callback_query_handler(text_contains="aback")#made callback for all another buttons
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer('Выберете направление',
                              reply_markup=another1)


@dp.callback_query_handler(text_contains="get_back_to_start")  # made callback to start from getting notified
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы успешно отписались",
                              reply_markup=start)


@dp.callback_query_handler(
    text_contains="education_cz")  # made callback for button which gets you back from education to long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("educ_data.txt",
                              reply_markup=get_back_from_education)


@dp.callback_query_handler(
    text_contains="get back to viza info")  # made callback for button of educational purpose returns back to long term viza
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)



@dp.callback_query_handler(text_contains="basic")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(message,
                              reply_markup=backtovizainfo1)



@dp.callback_query_handler(text_contains="chengen back")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info2)


@dp.callback_query_handler(text_contains="another")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=another1)


@dp.callback_query_handler(text_contains="bs")#made c
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=start)


@dp.callback_query_handler(text_contains="bacs")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=start)


@dp.callback_query_handler(text_contains="vb")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info2)


@dp.callback_query_handler(text_contains="get_back")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=start)



"""@dp.callback_query_handler(
    text_contains="shengen")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(shengen_articels,
                              reply_markup=chengen_back)"""


@dp.callback_query_handler(
    text_contains="chengen back")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
