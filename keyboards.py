from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'ютуб',url = 'https://www.youtube.com')],
    [InlineKeyboardButton(text = 'дискорд',url = 'https://discord.com')],
    [InlineKeyboardButton(text = 'steam',url = 'https://store.steampowered.com/')]
])

kboard = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text = 'заметки')],
    [KeyboardButton(text = 'ссылки')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню.')