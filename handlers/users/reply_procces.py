import logging
import typing

import txt as txt
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram import types

from handlers.users.bis_parser import bis
from handlers.users.long_list_parser import long_list
from handlers.users.news_parser import text_link_headers
from keyboards.inline.blanks import message
from keyboards.inline.calback_data import get_callback
from keyboards.inline.buttons import start, long_term, covid_measures, viza2_info, \
    chengen_back, viza_info, transformed_viza_info, get_notified, \
    get_back_to_start_from_covid, get_back_to_mailing, another1, back_to_another, \
    backtovizainfo1, back_to_long_term, start2, menu, back_to_start, another2, get_back_from_education
from keyboards.inline.center import center, center_c
from keyboards.inline.constant_living_parser import constant
from keyboards.inline.country_list_parser import content, clist
from keyboards.inline.differ_parser import differ
from keyboards.inline.family_parser import family
from keyboards.inline.fee import fee_content, fee_list
from keyboards.inline.long_living_parser import long
from keyboards.inline.sport_paser import sport
from keyboards.inline.viza_info_parse import content_viza
from keyboards.inline.war_parser import c, content1
from loader import dp, bot

from keyboards.inline.covid_parser import list5
from keyboards.inline.cul_parser import cul
from keyboards.inline.events_parser import events
from keyboards.inline.polit_parser import polit
from keyboards.inline.shengen_articles_parser import shengen_articels
from keyboards.inline.trade_parser import trade_articels

dp.message_handler()

latest_msg = None

@dp.message_handler(Command("start"))  # made introduction and logic of collecting user's data
async def show_items(message: Message):
    global latest_msg
    latest_msg = await message.answer(
        text="Доброго времени суток, юзеры.\nДанный бот призван облегчить ваш процесс работы с посольством Чешской Республики в Москве \n"
             "Для начала работы выберете топик снизу", reply_markup=start)

"""@dp.message_handler(text_contains="1")
async def huge(message: Message):
    global latest_msg
    await latest_msg.delete_reply_markup()
    latest_msg = await message.answer('ну привет')"""








"""@dp.callback_query_handler(text_contains="basic info")
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await latest_msg.delete_reply_markup()
    await call.message.answer(content_viza,
                              reply_markup=backtostart1)
"""



@dp.callback_query_handler(
    text_contains="main viza info")  # made callback for button which gives options of different types of vizas
async def viza_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await latest_msg.delete_reply_markup()
    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)








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
    text = ""
    for i in text_link_headers:
        text+=i+"("+text_link_headers[i]+")"+"\n"+"\n"

    await call.message.answer(text,
                              reply_markup=get_back_to_mailing)

@dp.callback_query_handler(text_contains="subagain")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=get_notified)


@dp.callback_query_handler(text_contains="long_list")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in long_list:
        text+=i+"("+long_list[i]+")""\n""\n"
    await call.message.answer(text,
                              reply_markup=get_back_from_education)


@dp.callback_query_handler(text_contains="bis")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(bis,
                              reply_markup=get_back_from_education)



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

    await call.message.answer(content_viza,
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

    await call.message.answer(sport,
                              reply_markup=back_to_long_term)


@dp.callback_query_handler(text_contains="family1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(family,
                              reply_markup=back_to_long_term)


@dp.callback_query_handler(text_contains="how differ1")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(differ,
                              reply_markup=back_to_long_term)

@dp.callback_query_handler(text_contains="56")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Долгосрочная виза",
                              reply_markup=long_term)



@dp.callback_query_handler(text_contains="to subscribe")  # made call back for buttton which gives you list of news
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
                              reply_markup=long_term)



@dp.callback_query_handler(text_contains="back_to_start")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer('Выберете направление',
                              reply_markup=start)



@dp.callback_query_handler(text_contains="another2")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in list5:
        text += i +"("+ list5[i]+")\n"+'\n'

    await call.message.answer("Выберете направление",
                              reply_markup=another2)






@dp.callback_query_handler(text_contains="covid")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in list5:
        text += i +"("+ list5[i]+")\n"+'\n'
    await latest_msg.delete_reply_markup()
    await call.message.answer(text,
                              reply_markup=back_to_start)





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
    text1 = ""
    for i in polit:
        text1 += i + "(" + polit[i] + ")\n" + '\n'
    await call.message.answer(text1,
                              reply_markup=back_to_another)


@dp.callback_query_handler(text_contains="trade")#made callback for button which gives trade's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text1 = ""
    for i in trade_articels:
        text1 += i + "(" + trade_articels[i] + ")\n" + '\n'
    await call.message.answer(text1,
                              reply_markup=back_to_another)




@dp.callback_query_handler(text_contains="cul")#made callback for button which gives culture's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(cul,
                              reply_markup=back_to_another)

@dp.callback_query_handler(text_contains="war")#made callback for button which gives war's content
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(c,
                              reply_markup=back_to_another)



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
                              reply_markup=another2)


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

    await call.message.answer(content1,
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


@dp.callback_query_handler(text_contains="constant")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in constant:
        text+=i+"("+constant[i]+")"+"\n"+"\n"
    await call.message.answer(text,
                              reply_markup=chengen_back)


@dp.callback_query_handler(text_contains="long_live")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in long:
        text+=i+"("+long[i]+")"+"\n"+"\n"
    await call.message.answer(text,
                              reply_markup=chengen_back)


@dp.callback_query_handler(text_contains="country_list")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(clist,
                              reply_markup=chengen_back)


@dp.callback_query_handler(text_contains="fee")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(fee_list,
                              reply_markup=chengen_back)


@dp.callback_query_handler(text_contains="viza_center")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(center_c,
                              reply_markup=chengen_back)

@dp.callback_query_handler(text_contains="another")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await latest_msg.delete_reply_markup()
    await call.message.answer("Выберете направление",
                              reply_markup=another2)





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
                              reply_markup=viza_info)


@dp.callback_query_handler(text_contains="get_back")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Выберете направление",
                              reply_markup=start)



@dp.callback_query_handler(
    text_contains="shengen")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    text = ""
    for i in shengen_articels:
        text+=i+"("+shengen_articels[i]+")"+"\n"+"\n"
    await call.message.answer(text,
                              reply_markup=chengen_back)


@dp.callback_query_handler(
    text_contains="chengen back")  # made callback for shengen button gives us list of articels and has back button
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Визовая информация",
                              reply_markup=viza_info)
