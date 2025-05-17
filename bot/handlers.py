from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, CallbackQuery

from bot.translate import translate_text
from bot.keyboards import get_language_keyboard
from config.settings import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Временное хранилище данных
user_data = {}


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Send the text you want to translate.")


@dp.message()
async def get_text(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {"text": message.text}
    await message.reply(
        "Select the source language:", reply_markup=get_language_keyboard()
    )


@dp.callback_query()
async def handle_language(callback: CallbackQuery):
    user_id = callback.from_user.id
    selected_lang = callback.data

    if "source_lang" not in user_data[user_id]:
        user_data[user_id]["source_lang"] = selected_lang
        await callback.message.edit_text(
            "Select target language:", reply_markup=get_language_keyboard()
        )
    else:
        user_data[user_id]["target_lang"] = selected_lang
        await callback.message.delete()

        text = user_data[user_id]["text"]
        src_lang = user_data[user_id]["source_lang"]
        tgt_lang = user_data[user_id]["target_lang"]

        translation = await translate_text(text, src_lang, tgt_lang)
        await callback.message.answer(f"Translation:\n\n{translation}")
