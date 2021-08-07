from aiogram.types import InputMediaDocument
from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='Artemii')



ATTACHMENT_PREFIX = 'attach://'


def create_page(header, content):
    response = telegraph.create_page(
        header,
        html_content=content,
        author_name='Jarvis',
        author_url="https://t.me/bruhGT_bot"

    )

    return 'https://telegra.ph/{}'.format(response['path'])


