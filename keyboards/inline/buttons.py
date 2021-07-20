from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

from keyboards.inline.calback_data import get_callback


start = InlineKeyboardMarkup(row_width=2)#made the first keyboard for buttons with the begging buttons

start_viza = InlineKeyboardButton(text="визы и консульская информация", callback_data=get_callback.new(item_name="basic info"))
start.insert(start_viza )

subscribe = InlineKeyboardButton(text="подписаться на рассылку новостей с сайта посольства", callback_data=get_callback.new(item_name="to subscribe"))
start.insert(subscribe)

viza2_info = InlineKeyboardButton(text="визовая информация", callback_data=get_callback.new(item_name="main viza info"))
start.insert(viza2_info)

covid_measures = InlineKeyboardButton(text="Covid-19", callback_data=get_callback.new(item_name="covid"))
start.insert(covid_measures)







viza_info = InlineKeyboardMarkup(row_width=2)




long_term = InlineKeyboardButton(text="долгосрочная виза", callback_data=get_callback.new(item_name="long term viza"))
viza_info.insert(long_term)

shengen = InlineKeyboardButton(text="шенгенская виза", callback_data=get_callback.new(item_name="shengen"))
viza_info.insert(shengen)

blanks = InlineKeyboardButton(text="бланки", callback_data=get_callback.new(item_name="6"))
viza_info.insert(blanks)

basic = blanks = InlineKeyboardButton(text="основная информация", callback_data=get_callback.new(item_name="5"))
viza_info.insert(basic)





viza_info2 = InlineKeyboardMarkup(row_width=2)#made modified keyboard for buttons for getting back from shengen


long_term = InlineKeyboardButton(text="долгосрочная виза", callback_data=get_callback.new(item_name="long term viza"))
viza_info2.insert(long_term)

shengen = InlineKeyboardButton(text="шенгенская виза", callback_data=get_callback.new(item_name="shengen"))
viza_info2.insert(shengen)

blanks1 = InlineKeyboardButton(text="бланки", callback_data=get_callback.new(item_name="6"))
viza_info2.insert(blanks1)

basic = InlineKeyboardButton(text="основная информация", callback_data=get_callback.new(item_name="5"))
viza_info2.insert(basic)

get_back_to_start = InlineKeyboardButton(text="Вернуться в начало", callback_data=get_callback.new(item_name="get_back"))
viza_info2.insert(get_back_to_start)







get_notified = InlineKeyboardMarkup(row_width=2)#made keyabord for buttons which make you notified and gives option to cancel or get list of news

unsubscribe = InlineKeyboardButton(text="Отменить", callback_data=get_callback.new(item_name="get_back_to_start"))
get_notified.insert(unsubscribe)

news_list = InlineKeyboardButton(text="Список новостей", callback_data=get_callback.new(item_name="news_list"))
get_notified.insert(news_list)




long_term = InlineKeyboardMarkup(row_width=2)#made keyboard for buttons for viza info

educ = InlineKeyboardButton(text="С целью обучения", callback_data=get_callback.new(item_name="education_cz"))
long_term.insert(educ)



f = InlineKeyboardButton(text="С целью соединения семьи", callback_data=get_callback.new(item_name="family1"))
long_term.insert(f)



g = InlineKeyboardButton(text="С целью спорта/культуры", callback_data=get_callback.new(item_name="sport1"))
long_term.insert(g)



t = InlineKeyboardButton(text="Разница между долгосрочной и краткосрочной", callback_data=get_callback.new(item_name="how differ1"))
long_term.insert(t)




get_back_to_start_from_covid = InlineKeyboardMarkup(row_width=2)#made button for getting back from covid to start
back = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="getback"))
get_back_to_start_from_covid.insert(back)





get_back_from_education= InlineKeyboardMarkup(row_width=2)
back = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="get back to long viza"))
get_back_from_education.insert(back)










get_back_to_mailing = InlineKeyboardMarkup(row_width=2)#made button which gwts back to subcribe prosses
back1 = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="subagain"))
get_back_to_mailing.insert(back1)



chengen_back = InlineKeyboardMarkup(row_width=2)#made back button for shengen serves for returning back to viza info
back12 = InlineKeyboardButton(text="Вернуться назад", callback_data=get_callback.new(item_name="chengen back"))
chengen_back.insert(back12)












transformed_viza_info = InlineKeyboardMarkup(row_width=2)#made keyboards for buttons which gets back in educational purpose with get back to viza info




educ = InlineKeyboardButton(text="С целью обучения", callback_data=get_callback.new(item_name="education"))
transformed_viza_info.insert(educ)



family = InlineKeyboardButton(text="С целью соединения семьи", callback_data=get_callback.new(item_name="family"))
transformed_viza_info.insert(family)



sport = InlineKeyboardButton(text="С целью спорта/культуры", callback_data=get_callback.new(item_name="sport aim"))
transformed_viza_info.insert(sport)



diff = InlineKeyboardButton(text="Разница между долгосрочной и краткосрочной", callback_data=get_callback.new(item_name="how differ"))
transformed_viza_info.insert(diff)


get_back = InlineKeyboardButton(text="Вернуться в визовую информцию", callback_data=get_callback.new(item_name="get back to viza info"))
transformed_viza_info.insert(get_back)