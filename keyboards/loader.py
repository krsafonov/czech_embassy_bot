import logging

from aiogram import Bot, Dispatcher, types

from config import *


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
