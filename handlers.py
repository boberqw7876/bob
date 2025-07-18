import os
import asyncio
import random
import keyboards as kb
from aiogram import Router,Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, CommandObject
from dotenv import load_dotenv
from aiogram.enums import ChatAction
from aiogram.types import InputMediaPhoto, InputMediaVideo,Contact,Message, CallbackQuery
from datetime import datetime
router = Router()
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(text = 'привет это бот помошник Джарвис')
    func_n = '''
    список команд бота джарвис
    /тут команды должны быть!!!!!!!
    /тут команды должны быть!!!!!!!
    /тут команды должны быть!!!!!!!
    '''
    await message.answer(func_n,reply_markup= kb.kboard)
    
@router.message(F.text == 'ссылки')
async def links(message:Message):
    await message.answer(text = 'вот ваши ссылки',reply_markup= kb.main)

@router.message(F.text == 'заметки')
async def note(message:Message):
    await message.answer(text = 'вы сохранили этот текст')