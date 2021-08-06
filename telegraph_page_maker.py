from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='Artemii')



def create_page(header, content):
    response = telegraph.create_page(
        header,
        html_content=content,
        author_name='Jarvis',
        author_url=""

    )

    return 'https://telegra.ph/{}'.format(response['path'])
