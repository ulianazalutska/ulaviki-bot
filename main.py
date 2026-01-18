import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment variables")

CHAT_LINK = "https://t.me/ulaviki_chat"
CHANNEL_LINK = "https://t.me/ourquietmoments"
RULES_LINK = "https://telegra.ph/PRAVILA-CHATA-01-18-113"
TIKTOK_LINK = "https://www.tiktok.com/@wlwduo.vu"

bot = Bot(TOKEN)
dp = Dispatcher()

def menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Группа", url=CHAT_LINK),
            InlineKeyboardButton(text="Канал", url=CHANNEL_LINK),
        ],
        [
            InlineKeyboardButton(text="Правила", url=RULES_LINK),
            InlineKeyboardButton(text="TikTok", url=TIKTOK_LINK),
        ],
    ])

WELCOME_TEXT = (
    "Добро пожаловать в телеграмм канал Ули и Вики! 💋\n\n"
    "Перед началом общения в чате ознакомьтесь с правилами\n\n"
    f"Основной канал: {CHANNEL_LINK}"
)

# ловить автоматично пересланий пост з каналу в чат обговорення
@dp.message(F.is_automatic_forward == True)
async def on_channel_post_in_discussion(message: Message):
    await message.reply(
        WELCOME_TEXT,
        reply_markup=menu_keyboard(),
        disable_web_page_preview=True
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
