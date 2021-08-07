from aiogram.types import InputMediaDocument
from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='Artemii')


import io
import secrets
import typing

from . import base
from . import fields
from .input_file import InputFile
from .message_entity import MessageEntity

ATTACHMENT_PREFIX = 'attach://'


def create_page(header, content):
    response = telegraph.create_page(
        header,
        html_content=content,
        author_name='Jarvis',
        author_url="https://t.me/bruhGT_bot"

    )

    return 'https://telegra.ph/{}'.format(response['path'])


def attach_document(document):
    document = InputMediaDocument(

    )
